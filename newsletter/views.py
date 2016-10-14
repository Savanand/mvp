from django.shortcuts import render

from .forms import SignUpForm

# Create your views here.
def home(request):
	form = SignUpForm(request.POST or None)
	title = "Welcome Guest"  # view function variable
	# if request.user.is_authenticated():
	# 	title = "My Title. Welcome %s" %(request.user)

	#add form here
	# if request.method == "POST":
	# 	print request.POST
	context = {
		"title" : title,  #template context variable
		"form" : form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.full_name:
			instance.full_name = "DefaultAniket"
		instance.save()
		context = {
			"title" : "Thank You"
		}
		# print instance.email
		# print instance.timestamp	 

	return render(request, "home.html", context)