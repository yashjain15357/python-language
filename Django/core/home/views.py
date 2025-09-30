from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    people = [
        {"name": "yash" , "age":233,"city":"jbp"},
        {"name": "Riya" , "age":23,"city":"jsdf"},
        {"name": "Raksha" , "age":232,"city":"jwe"},
        {"name": "Riya" , "age":4534,"city":"jbwe"},
        {"name": "yRaksha" , "age":43,"city":"dds"},
        {"name": "Riya" , "age":45,"city":"jsd"}
    ]

    
    return render(request, "index.html" , context={'peoples':people})

def about(request):
    # print("*" * 10)
    return render(request, "about.html")
def contact(request):
    # print("*" * 10)
    return render(request, "contact.html")
