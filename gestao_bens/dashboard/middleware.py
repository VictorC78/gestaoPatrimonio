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

        # Verifica se a requisição é para a API e se o usuário não é superusuário ou não está autenticado
        if request.path.startswith('/api/'):

            # Se o usuário não for superusuário ou não estiver autenticado
            if not request.user.is_authenticated or not request.user.is_superuser:
                return JsonResponse({'error': 'Forbidden: You must be a superuser to access this API.'}, status=403)

        allowed_paths = ['/usuarios/login/', '/usuarios/register/']
        
        # Se o usuário não estiver autenticado e não estiver acessando as páginas de login ou registro
        if not request.user.is_authenticated and request.path not in allowed_paths:
            return redirect('/usuarios/login/')
        
        return self.get_response(request)
