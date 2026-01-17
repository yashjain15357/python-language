from django.http import HttpResponse , JsonResponse


def home_page(request):
    print("hii i am a yash jain")
    friends_API = ["yash" , "Riya" , "shivangi" , "prasoon"]
    # return HttpResponse("asdfsdfsdf")
    return JsonResponse(friends_API , safe=False)
