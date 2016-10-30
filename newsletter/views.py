from django.conf import settings #if to import something from settings.py
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm, SignUpForm
from .models import SignUp

# Create your views here.
def home(request):
	form = SignUpForm(request.POST or None)
	title = "Sign up now"  # view function variable
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

	if request.user.is_authenticated() and request.user.is_staff:
		#print(SignUp.objects.all())
		
		# i =1 	
		# for instance in SignUp.objects.all():
		# 	print(i)
		# 	print(instance)
		# 	print(instance.full_name)
		# 	i += 1

		# queryset = SignUp.objects.all().order_by('-timestamp')
		queryset = SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains="a")
		# queryset = SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Maya")
		print(SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains="a").count())
		context = {
			"queryset" : queryset
		}	
	return render(request, "home.html", context)

# defining a view for contactform

def contact(request):   # this is a way to deal with form wihtout using any model
	title = 'Contact Us'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		#print form.cleaned_data   # can not put form.save as above cause this is not a model,
		# this is just a simple form

		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")

		# print email, message, full_name

		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'aniketpsavanand@gmail.com']
		contact_message = """
		%s: %s via %s
		"""%(form_full_name, form_message, form_email)

		send_mail(subject, contact_message, from_email, to_email, fail_silently=True)

		#fail_silently make it true if we want to save our data in the database permanently other wise keep it false

		# for key in form.cleaned_data:
		# 	print key
		# 	print form.cleaned_data.get(key)

		#simpler form than above

		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value


	context = {
		"form" : form,
		"title" : title,
	}

	return render(request, "forms.html", context)