from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()




class ContactForms(forms.Form):
    full_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 
                "placeholder": "Your full name"
                }
            )
        )
    email=forms.EmailField(
         widget=forms.EmailInput(
            attrs={
                "class": "form-control", 
                "placeholder": "Your email"
                }
            )
        )
    content=forms.CharField(
         widget=forms.Textarea(
            attrs={
                "class": "form-control", 
                "placeholder": "enter content"
                }
            )
    )
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

# class loginForm(forms.Form):
   
#     username=forms.CharField(
#          widget=forms.TextInput(
#             attrs={
#                 "class": "form-control", 
#                 "placeholder": "enter user name"
#                 }
#             )
#     )
#     password=forms.CharField(
#          widget=forms.PasswordInput(
#               attrs={
#                 "class": "form-control", 
#                 "placeholder": "Password"
#                 }
#         )
#     )


# class RegisterForm(forms.Form):
#     username = forms.CharField(
#           widget=forms.TextInput(
#             attrs={
#                 "class": "form-control", 
#                 "placeholder": "enter user name"
#                 }
#             )
#     )
#     email    = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "form-control", 
#                 "placeholder": "Your email"
#                 }
#             )
#     )
#     password = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         qs = User.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError("Username is taken")
#         return username

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("email is taken")
#         return email

#     def clean(self):
#         data = self.cleaned_data
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
#         if password2 != password:
#             raise forms.ValidationError("Passwords must match.")
#         return data

