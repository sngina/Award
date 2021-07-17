from project.forms import ProfileForm, ReviewForm
from django.shortcuts import render 
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse ,Http404 
from .models import Project ,Profile ,Review
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url= '/accounts+/login/')
def post_project(request):
    all_images = Project.objects.all()
    review = Review.objects.all()
    if request.method == 'Post':
        form = ProfileForm(request.Post , request.FILES)
        if form.is_valid():
            form.save()
    c_form = ReviewForm()
    form = ProfileForm()
    return render(request , 'profile/index.html' , {"all_images":all_images , "profileform":form , "c_form":c_form , "review":review})
    