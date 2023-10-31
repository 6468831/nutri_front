
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('foods/', include(('foods.urls', 'foods'), namespace='foods')),
    path('recipes/', include(('recipes.urls', 'recipes'), namespace='recipes')),
    path('diaries/', include(('diaries.urls', 'diaries'), namespace='diaries')),
    path('utils/', include(('utils.urls', 'utils'), namespace='utils')),
    path('', index, name='index'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)