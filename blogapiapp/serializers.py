from rest_framework.serializers import ModelSerializer
from blogapiapp import models

#class to serialize the BlogUserModel
class BlogUserSerialize(ModelSerializer):

    #Meta Class
    class Meta:
        model=models.BlogUserModel
        fields=('id','userid','email','name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{
                    'input_type':'password'
                }
        }
    }

    #To create a serialized user
    def create(self, validated_data):
        email=validated_data['email']
        name=validated_data['name']
        userid=validated_data['userid']
        password=validated_data['password']
        blog_user=models.BlogUserModel.objects.create_user(
            email=email,
            userid=userid,
            name=name,
            password=password
        )

        return blog_user
    
    #To Update a serialized user
    def update(self, instance, validated_data):

        if 'password' in validated_data:
            password=validated_data.pop('password')

        instance.set_password(password)

        return instance

#Blog Post Serializer
class BlogPostSerializer(ModelSerializer):

    class Meta:
        model=models.BlogPostModel
        fields=('id','post_profile','title','post')
        extra_kwargs={
            'post_profile':{
                'read_only':True
            }
        }
