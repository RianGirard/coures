from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('courses/destroy/<int:id>', views.destroy),
    path('courses/destroy/confirm_destroy', views.confirm_destroy),
    path('courses/comment/<int:id>', views.comment),
    path('courses/comment/add_comment/<int:id>', views.comment_add),
]