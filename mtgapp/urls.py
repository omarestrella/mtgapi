from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from mtgapp import views

router = DefaultRouter()
router.register(r'cards', views.CardViewSet, 'card')
router.register(r'decks', views.DeckViewSet, 'deck')
router.register(r'card-colors', views.CardColorViewSet, 'card-color')
router.register(r'card-sets', views.CardSetViewSet, 'card-set')
router.register(r'card-subtypes', views.CardSubtypeViewSet, 'card-subtype')
router.register(r'card-types', views.CardTypeViewSet, 'card-type')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/$', views.AuthenticationView.as_view(), name='token_auth_view'),
    url(r'^auth/logout/$', views.LogoutView.as_view(), name='logout_view'),
    url(r'^auth/register/$', views.RegistrationView.as_view(), name='registration_view'),
]
