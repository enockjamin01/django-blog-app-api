from django.contrib import admin
from blogapiapp import models

# Register your models here.
admin.site.register(models.BlogUserModel)
admin.site.register(models.BlogPostModel)