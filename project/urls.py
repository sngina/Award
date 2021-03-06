from django.conf.urls import url , include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.post_project , name= 'homepage'),
    url('^user/' , views.userpage , name='username'),
    url('^review/' , views.review_project , name ='review'),
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'^api/profile/$' , views.ProfileList.as_view())

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
