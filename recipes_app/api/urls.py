from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'recipes', basename='recipe')

urlpatterns = [
   path('', include(router.urls)),
]