from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from tracker.auth_views import signup, signin


def health_check(request):
    """Root endpoint for API health check."""
    return JsonResponse({
        'status': 'ok',
        'message': 'MediSure Health API is running',
        'version': '1.0.0',
    })


urlpatterns = [
    path('', health_check, name='health_check'),
    path('admin/', admin.site.urls),
    path('api/', include('tracker.urls')),
    path('api/auth/signup/', signup, name='signup'),
    path('api/auth/signin/', signin, name='signin'),
]