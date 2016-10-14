from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
	"""docstring for SignUpForm"forms.ModelFormf __init__(self, arg):
		super(SignUpForm,forms.ModelForm.__init__()
		self.arg = arg
		"""
		
	class Meta:
		model = SignUp
		fields = ['email', 'full_name']

	def clean_email(self):
		email = self.cleaned_data.get('email')

		# validation code for cleaning email
		email_base, provider = email.split("@")
		domain, extention = provider.split('.')
		#if not domain == "sjsu":
		#	raise forms.ValidationError("Please use a SJSU email address")

		if not extention == "edu":
			raise forms.ValidationError("Please use a valid .EDU email address")

		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		# validation code for cleaning fullname
		return full_name

