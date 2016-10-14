from django.shortcuts import render

# Create your views here.
def home(request):
	title = "Welcome Guest"  # view function variable
	if request.user.is_authenticated():
		title = "My Title. Welcome %s" %(request.user)

	#add form here
	context = {
		"title" : title,  #template context variable
	}
	return render(request, "home.html", context)