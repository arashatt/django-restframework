from django.urls import path
from .views import PostList, PostDetail
urlpatterns = [
path('<int:pk>/', PostDetail.as_view()),
path('', PostList.as_view()),
]
"""
from rest_framework.routers import SimpleRouter                                
router = SimpleRouter()                                                        
router.register('users')                                                       
router.register('')                                                             
                      
"""
