from django.shortcuts import render

from .forms import ContactForm, SignUpForm

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

# defining a view for contactform

def contact(request):   # this is a way to deal with form wihtout using any model

	form = ContactForm(request.POST or None)
	if form.is_valid():
		#print form.cleaned_data   # can not put form.save as above cause this is not a model,
		# this is just a simple form

		# email = form.cleaned_data.get("email")
		# message = form.cleaned_data.get("message")
		# full_name = form.cleaned_data.get("full_name")

		# print email, message, full_name

		# for key in form.cleaned_data:
		# 	print key
		# 	print form.cleaned_data.get(key)

		#simpler form than above

		for key, value in form.cleaned_data.iteritems():
			print key, value


	context = {
		"form" : form
	}

	return render(request, "forms.html", context)