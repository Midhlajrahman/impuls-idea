from django import forms
from . models import Contact, Newsletter

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control from-input", "placeholder": "Your name:"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control required email from-input",
                    "placeholder": "Your Mail:",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control required from-input",
                    "placeholder": "Enter Your Subject:",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control required from-input",
                    "rows": 5,
                    "placeholder": "Your Massage:",
                }
            ),
        }
        
        
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        exclude = ()

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address",
                }
            ),
        }