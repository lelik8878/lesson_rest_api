from django.contrib import admin

from .models import CategoryOfService, TypeOfService, TypeOfSubService

admin.site.register(CategoryOfService)
admin.site.register(TypeOfService)
admin.site.register(TypeOfSubService)


