from rest_framework.routers import DefaultRouter

from mtgapp import views

router = DefaultRouter()
router.register(r'card', views.CardViewSet)
urlpatterns = router.urls
