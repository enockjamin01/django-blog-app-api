import rest_framework.routers
from blogapiapp import views
from django.urls import include
from django.urls import path

router=rest_framework.routers.DefaultRouter()
router.register('bloguser',viewset=views.BlogUserProfileView)
router.register('blogpost',viewset=views.BlogPostView)

urlpatterns=[
    path('',include(router.urls)),
    path('login/',views.BlogUserLogin.as_view())
]