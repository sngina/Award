from django.contrib import admin
from .models import Profile, Project ,Review
# Register your models here.

class ReviewAdmin (admin.ModelAdmin):
    list_display = ('name' ,'post' ,'body')
    actions = ['allow_review']

    def allow_reviews(self , request , queryset):
        queryset.update(active = True)

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('image' ,)


admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Review)