from django.shortcuts import render, redirect, get_object_or_404
from veg.models import *
from django.contrib import messages  # Add this import
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.
def recp(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "add_recipe":
            data = request.POST
            recp_name = data.get("recp_name")
            recp_decp = data.get("recp_decp")
            recp_img = request.FILES.get("recp_img")
            # print(f"The recipe name is {recp_name} and descriptions is {recp_decp} and image name is {recp_img}")
            Recp.objects.create(
                recp_name=recp_name, 
                recp_decp=recp_decp, 
                recp_img=recp_img
                )
            messages.success(request, "Recipe added successfully!")  # Flash message
            return redirect(to="/recipes")
        elif form_type == "search":
            query = request.POST.get("search_query")
            # __icontains is used to search for partial matches in a field, without caring about uppercase/lowercase.
            all_data = Recp.objects.filter(recp_name__icontains=query)
            return render(request, "recp.html", context={'datas': all_data})

        
    
    all_data=Recp.objects.all()
    print(all_data)
    return render(request,"recp.html" ,context={'datas' : all_data} )


def delete_recp(request, id):
    query = get_object_or_404(Recp, id=id)
    if query.recp_img:
        query.recp_img.delete(save=False)  # This deletes the file from media/
    query.delete()
    messages.success(request, "Recipe deleted successfully!")
    return redirect("/recipes")

def update_recp(request , id):
    change = Recp.objects.get(id=id)
    if request.method =='POST':
        data = request.POST
        change.recp_name = data.get("recp_name")
        change.recp_decp = data.get("recp_decp")
        if request.FILES.get("recp_img") :
            change.recp_img = request.FILES.get("recp_img")
        change.save()
        return redirect(to="/recipes")
    return render(request ,"update.html" ,context={'data' :change })


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.get(email=email)
        
        if user and user.check_password(password):
            
            messages.success(request, f"Welcome back, {email}!")
            return redirect(to='/recipes')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/login')

    return render(request , 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not all([username, email, password]):
            messages.error(request, "All fields are required.")
            return redirect('/register')

        if User.objects.filter(username=username).exists():
            messages.error(request, f"Username '{username}' is already taken.")
            return redirect('/register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, f"An account with email '{email}' already exists.")
            return redirect('/register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('/login' )

    return render(request ,'register.html')
