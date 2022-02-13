from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'app'

router = DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('portfolio', views.PortfolioViewSet)
router.register('like', views.LikeViewSet)
router.register('comment', views.CommentViewSet)

urlpatterns = [
    path('myprofile/', views.MyProfileListView.as_view(), name='myprofile'),
    path('', include(router.urls))
]
