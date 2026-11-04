from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control my-2 form-box',
                'placeholder': 'نام...', 'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control my-2 form-box',
                'placeholder': 'ایمیل...', 'required': True,
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control my-2 form-box',
                'placeholder': 'موضوع...',
            }),
            'message': forms.Textarea(attrs={
                'class': 'my-2 w-100 form-box',
                'placeholder': 'پیام...', 'rows': 3, 'required': True,
            }),
        }

    def save(self, commit=True, kind=ContactMessage.KIND_CONTACT):
        instance = super().save(commit=False)
        instance.kind = kind
        if commit:
            instance.save()
        return instance


class ProjectRequestForm(ContactForm):
    def save(self, commit=True):
        return super().save(commit=commit, kind=ContactMessage.KIND_PROJECT)