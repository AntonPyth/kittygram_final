from cats.views import AchievementViewSet, CatViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from djoser.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Регистрация пользователя
    path('api/users/register/', UserViewSet.as_view({'post': 'create'}), name='user-register'),
    # Токены
    path('api/auth/', include('djoser.urls.authtoken')),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('api/users/', include('djoser.urls')),
#     # path('api/users/', include('djoser.urls')),  # Работа с пользователями
#     # path('api/users/', include('djoser.urls.authtoken')),  # Работа с токенами
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
