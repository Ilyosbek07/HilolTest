from django.contrib import admin

from appp.models import Category, Users, Quetions

# @admin.sit
# class QuetionsAdmin(admin.ModelAdmin):
#     list_filter = ['created_at']
#     search_fields = '__all__'


admin.site.register(Quetions)
admin.site.register(Category)
admin.site.register(Users)
