from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import RecommendationViewSet

router = DefaultRouter()
router.register(r'recommendations', RecommendationViewSet)

urlpatterns = [
    path('search/', views.search_view, name='search'),
    path('recommendations/', views.recommendations_view, name='recommendations'),
    path('submit_recommendations/', views.submit_recommendations, name='submit_recommendations'),
    path('', include(router.urls)),
]+ router.urls
