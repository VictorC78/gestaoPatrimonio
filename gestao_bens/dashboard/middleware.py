
import sys
from django.shortcuts import redirect
from django.http import JsonResponse

class LoginRequiredMiddleware:
    """Middleware para exigir login em todas as páginas do site, exceto nas páginas de login e registro."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Ignorar middleware durante os testes
        if 'test' in sys.argv:
            return self.get_response(request)

        # Permitir requisições internas do próprio servidor (como no caso do requests.get)
        if request.path.startswith('/api/') and not request.user.is_superuser:
            if request.META.get('HTTP_REFERER') and '127.0.0.1:8000' in request.META['HTTP_REFERER']:
                # Permite requisições internas, como as feitas pelo próprio servidor
                return self.get_response(request)

            return JsonResponse({'error': 'Forbidden: You must be a superuser to access this API.'}, status=403)

        allowed_paths = ['/usuarios/login/', '/usuarios/register/']
        
        # Se o usuário não estiver autenticado e não estiver acessando as páginas de login ou registro
        if not request.user.is_authenticated and request.path not in allowed_paths:
            return redirect('/usuarios/login/')
        
        return self.get_response(request)
