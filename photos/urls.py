from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('search/', views.search_images, name='search_results'),
    path('image/<int:image_id>', views.get_image, name='image_results'),
    path('new/image$', views.new_image, name='new-image'),
    path('accounts/profile/',views.user_profiles, name='profile'),
    path('like/<int:image_id>', views.like_image, name='like_image'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

