from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter

import socketio.sdjango

from mtgapp import views

router = DefaultRouter()
router.register(r'card', views.CardViewSet)
router.register(r'deck', views.DeckViewSet)
urlpatterns = router.urls

socketio.sdjango.autodiscover()

urlpatterns += patterns('',
    url("^socket\.io", include(socketio.sdjango.urls)),
)

urlpatterns += patterns('',
    url(r'^auth/$', views.AuthenticationView.as_view(), name='token_auth_view'),
    url(r'^auth/logout/$', views.LogoutView.as_view(), name='logout_view'),
    url(r'^auth/register/$', views.RegistrationView.as_view(), name='registration_view'),
)
