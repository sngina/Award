from django.core.checks import messages
from project.forms import ProfileForm, ReviewForm ,ProjectForm, UserForm
from django.shortcuts import render 
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse ,Http404 
from .models import Project ,Profile ,Review
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url= '/accounts/login/')
def post_project(request):
    all_projects = Project.objects.all()
    review = Review.objects.all()
    print("niko hapaa juu")
    if request.method == 'POST':
        print("digehota")
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            pform = form.save()
            pform.user= request.user
            pform.save()
            return redirect('homepage')
    c_form = ReviewForm()
    form = ProjectForm()
    return render(request , 'profile/index.html' , {"all_projects":all_projects , "projectform":form , "c_form":c_form , "review":review})
def userpage(request):
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request,"profile.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })
#search project
def search(request):
    if 'project' in request.GET and request.GET ["project"]:
        search_term = request.GET.get("project")
        search_project = Project.search_project(search_term)
        message = f"{search_term}"
        return render(request , 'profile/search.html' , {"message":message, "search_project" :search_project})

    else:
        message = "You haven't searched for any project" 
        return render(request , 'profile/search.html')

#review functiom
def review_project(request):
    if request.method == 'POST':
        review_form = ReviewForm(data = request.POST)
        if review_form.is_valid():
            pro_id = int(request.POST.get('projectid'))
            project = Project.objects.get(id=pro_id)
            new_review = review_form.save(review = False)
            new_review.name = request.user
            new_review.post = project
            new_review.save()

        return redirect('homepage')

