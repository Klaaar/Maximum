from django.urls import path
from .views import index, top_sellers, advertisements_post

urlpatterns = [
    path('',index, name='mane-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisements-post/', advertisements_post, name='adv-post')
]
