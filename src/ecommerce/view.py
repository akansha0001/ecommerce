from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import ContactForms
from django.contrib.auth import authenticate, login ,get_user_model

from carts.models import Cart

from products.models import Product


def home_page(request):
    queryset = Product.objects.all()
    a = {
        "title":"welcome to Ecommerce website!",
        "content":" Welcome to the homepage.",
        "Premium_content":"yeaah",
        'object_list': queryset
    }
    print(len(queryset))
    if request.user.is_authenticated:
        a["Premium_content"]="yeaah"
    return render(request,"home_page.html",a)



def contact_page(request):
    contact_form = ContactForms(request.POST or None)
    context = {
        "title":"Contact page",
        "content":" Welcome to the contact page",
        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if(request.method=='POST'):
    #     print(request.POST)
    #     print(request.POST.get('full_name'))
    return render(request,"contact/view.html",context)


# def login_page(request):
#     form = loginForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     print("User logged in")
#     #print(request.user.is_authenticated())
#     if form.is_valid():
#         print(form.cleaned_data)
#         username  = form.cleaned_data.get("username")
#         password  = form.cleaned_data.get("password")
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         print(request.user.is_authenticated)
#         if user is not None:
#             #print(request.user.is_authenticated())
#             login(request, user)
#             # Redirect to a success page.
#             #context['form'] = LoginForm()
#             return redirect("/")
#         else:
#             # Return an 'invalid login' error message.
#             print("Error")

#     return render(request, "auth/login.html", context)

# User = get_user_model()
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         print(form.cleaned_data)
#         username  = form.cleaned_data.get("username")
#         email  = form.cleaned_data.get("email")
#         password  = form.cleaned_data.get("password")
#         new_user  = User.objects.create_user(username, email, password)
#         print(new_user)

#     return render(request, "auth/register.html", context)
