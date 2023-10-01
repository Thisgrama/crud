from django.urls import path, include
from .views import (
    index,
    create_post,
    edit_post,
    login_view,
    delete_post,
    register_view,
    logout_view,
    details_post
)


urlpatterns = [
    path('', index, name='index'),
    path('auth/', include([
        path('register/', register_view, name='register'),
        path('login/', login_view, name='login'),
        path('logout/', logout_view, name='logout'),
        ])),
    path('post/', include([
        path('create/', create_post, name='create post'),
        path('<int:pk>/', include([
            path('details/', details_post, name='details post'),
            path('edit/', edit_post, name='edit post'),
            path('delete/', delete_post, name='delete post')
        ]))
    ]))
]
