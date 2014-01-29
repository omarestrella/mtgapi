from django.conf.urls import patterns, url

from rest_framework.routers import DefaultRouter

from mtgapp import views

router = DefaultRouter()
router.register(r'card', views.CardViewSet)
router.register(r'deck', views.DeckViewSet)
urlpatterns = router.urls

urlpatterns += patterns('',
    url(r'^sse/test/$', views.SSETestView.as_view(), name='sse_test_view'),
)
