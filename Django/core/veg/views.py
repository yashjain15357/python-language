from django.shortcuts import render, redirect, get_object_or_404 # Django shortcuts for common tasks like rendering templates and redirecting.
from veg.models import * # Imports all models from the veg app, like the Recp model.
from django.contrib import messages  # Django's messaging framework for showing one-time notifications (flash messages).
from django.contrib.auth.models import User # Django's built-in User model for authentication.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout # Core authentication functions.
from django.contrib.auth.decorators import login_required # A decorator to restrict access to views to logged-in users.

# The @login_required decorator ensures that only authenticated users can access this view.
# If a user is not logged in, they will be redirected to the URL specified in `login_url`.
@login_required(login_url="/login/")
def recp(request):
    # `request.method` checks the HTTP method used for the request. Here, we check for "POST".
    if request.method == "POST":
        # `request.POST` is a dictionary-like object containing all parameters from a POST request.
        form_type = request.POST.get("form_type")
        if form_type == "add_recipe":
            data = request.POST
            recp_name = data.get("recp_name")
            recp_decp = data.get("recp_decp")
            # `request.FILES` contains all uploaded files. Use .get() to access a specific file.
            recp_img = request.FILES.get("recp_img")
            
            # `Recp.objects.create(...)` is a Django ORM method to create and save a new model instance in one step.
            Recp.objects.create(
                user = request.user, # Associate the recipe with the currently logged-in user.
                recp_name=recp_name, 
                recp_decp=recp_decp, 
                recp_img=recp_img
                )
            # `messages.success()` adds a success-level message to be displayed on the next page.
            messages.success(request, "Recipe added successfully!")
            # `redirect()` returns an HTTP 302 response to the browser, telling it to go to a new URL.
            return redirect(to="/recipes")
        elif form_type == "search":
            query = request.POST.get("search_query")
            # `Recp.objects.filter()` retrieves objects from the database that match the given criteria.
            # `recp_name__icontains` is a field lookup that performs a case-insensitive "contains" search.
            # `recp_name__icontains` is a powerful field lookup (operator) that performs a case-insensitive "contains" search.
            all_data = Recp.objects.filter(recp_name__icontains=query)
            # `render()` combines a template with a context dictionary and returns an HttpResponse object.
            return render(request, "recp.html", context={'datas': all_data})

    # `Recp.objects.all()` is a Django ORM method to retrieve all objects from the Recp table.
    all_data=Recp.objects.all()
    return render(request,"recp.html" ,context={'datas' : all_data} )


def delete_recp(request, id):
    # `get_object_or_404()` is a shortcut to get an object or raise an Http404 (Not Found) error if it doesn't exist.
    query = get_object_or_404(Recp, id=id)
    if query.recp_img:
        # This deletes the actual image file from your media directory.
        query.recp_img.delete(save=False)
    # This deletes the database record for the recipe.
    query.delete()
    messages.success(request, "Recipe deleted successfully!")
    return redirect("/recipes")

def update_recp(request , id):
    # `Recp.objects.get()` retrieves a single object from the database matching the criteria.
    change = Recp.objects.get(id=id)
    if request.method =='POST':
        data = request.POST
        change.recp_name = data.get("recp_name")
        change.recp_decp = data.get("recp_decp")
        # Check if a new file was uploaded in the form.
        if request.FILES.get("recp_img") :
            change.recp_img = request.FILES.get("recp_img")
        # `change.save()` saves the changes made to the model instance back to the database.
        change.save()
        return redirect(to="/recipes")
    # For a GET request, render the update form with the existing recipe data.
    return render(request ,"update.html" ,context={'data' :change })


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
 
        try:
            # Retrieve the user object based on the provided email.
            user_obj = User.objects.get(email=email)
            # `authenticate()` checks credentials. It returns a user object if they are valid.
            user = authenticate(request, username=user_obj.username, password=password)
            
            if user is not None:
                # `auth_login()` logs the user in by creating a session for them.
                auth_login(request, user) 
                messages.success(request, f"Welcome back, {email}!")
                return redirect(to='/recipes')
            else:
                # Password was incorrect
                messages.error(request, "Invalid email or password.")
        # This `except` block catches the error if no user with the given email is found.
        except User.DoesNotExist:
            # User with this email does not exist
            messages.error(request, "Invalid email or password.")
            return redirect('/login')
 
 
    return render(request , 'login.html')
 
def logout_page(request):
    # `auth_logout()` removes the session data for the user, effectively logging them out.
    auth_logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Basic validation to ensure no fields are empty.
        if not all([username, email, password]):
            messages.error(request, "All fields are required.")
            return redirect('/register')

        # `User.objects.filter(...).exists()` is an efficient way to check if any records match the query.
        if User.objects.filter(username=username).exists():
            messages.error(request, f"Username '{username}' is already taken.")
            return redirect('/register')
        
        # Check if a user with the same email already exists.
        if User.objects.filter(email=email).exists():
            messages.error(request, f"An account with email '{email}' already exists.")
            return redirect('/register')

        # `User.objects.create_user()` is a helper method that creates a new user and hashes the password.
        user = User.objects.create_user(username=username, email=email, password=password)
        # The user is already saved by `create_user`, but calling save() again is harmless.
        user.save() 
        messages.success(request, "Registration successful! Please log in.")
        return redirect('/login' )

    return render(request ,'register.html')

from django.db.models import Q

def get_student(request):
    queryset = Student.objects.all()
    if request.GET.get("search"):
        search = request.GET.get("search")
        # Use Q objects to create a more complex query.
        # This searches for the 'search' term in either the student_name OR the department.
        # Note: This assumes your Student model has a 'department' field.
        queryset = queryset.filter(
            # The double underscore (__) tells Django: "Look inside the model that the first department field points to."

            Q(student_name__icontains=search) | Q(department__department__icontains=search)| Q(student_id__student_id__icontains=search) | Q(student_age__icontains=search))
    return render(request , 'report/student.html' , {'queryset' : queryset})

def get_report(request , student_id):
    # Since student_id is the primary key of the Student model, we can query it directly.
    # This gets all marks for the student with the given student_id.
    # .select_related('student', 'subject') optimizes the query by fetching related objects in a single database hit.
    student_marks = Subject_M.objects.filter(student__student_id=student_id).select_related('student', 'subject')
    total_marks = sum(i.marks for i in student_marks)
    result = "Pass"
    for i in student_marks:
        if i.marks<40:
            result = "Fail"

    return render(request ,"report/student_mark.html",{'data' : student_marks , 'total' : total_marks , 'result' :result})
