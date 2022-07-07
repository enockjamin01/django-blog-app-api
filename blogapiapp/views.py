from rest_framework.filters import SearchFilter
from blogapiapp import models
from blogapiapp.serializers import BlogUserSerialize
from blogapiapp.serializers import BlogPostSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from blogapiapp import permissions
from rest_framework.settings import api_settings

# Create your views here.
#BlogUserProfileView
class BlogUserProfileView(ModelViewSet):

    #Serializer Class object
    serializer_class=BlogUserSerialize
    queryset=models.BlogUserModel.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.BlogUserPermission,)
    filter_backends=(SearchFilter,)
    search_fields=('name','userid','id','email',)

#User Login View
class BlogUserLogin(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

#User Post View
class BlogPostView(ModelViewSet):

    #Serializer Class object
    serializer_class=BlogPostSerializer
    queryset=models.BlogPostModel.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.BlogPostPermission,IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(post_profile=self.request.user)