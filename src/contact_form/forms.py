from django import forms
CHOICES= [
    ('website', 'WebSite'),
    ('Photography', 'Wedding Photography'),
    ('Photography', 'Pre Wedding Photography'),
    ('Photography', 'Maternity Photography'),
    ('Photography', 'Portfolio'),
    ('Application Development','Android Application'),
    ('Application Development','Ios Application'),
    ]

class ContactForm(forms.Form):
	first_name=forms.CharField(label='Your First Name',max_length=100)
	last_name=forms.CharField(label='Your Last Name',max_length=100)
	email=forms.EmailField(label='Email id')
	message=forms.CharField(label='Messgae for us',required=False,widget=forms.Textarea)
	CHOICES=forms.CharField(label='I am looking for',widget=forms.Select(choices=CHOICES))




	 