from django.shortcuts import render
from .models import User, Client

b = Client.objects.all()
n = len(b)
u = {}
for i in range(0, n):
    u[b[i].email] = b[i].password

def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")

def signin(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    passwordagain = request.GET.get("passwordagain")

    if password == passwordagain:
        b = Client()
        b.email = email
        b.password = password
        b.save()
        return render(request, "index.html")

    return render(request, "signup.html")

def isloggedin(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    e = email
    p = password
    print(email, password)
    b = Client.objects.all()
    
    print(b[0].email)
    if email not in u and password not in u[email]:
        # messages.info("Not a valid user try again")
        return render(request, "login.html")
    else:
        return render(request, "index.html")


def index(request):
    return render(request, "index.html")


def records(request):
    emailaddress = request.GET.get('emailaddress')
    startdate = request.GET.get('startdate')
    dates = request.GET.get('dates')
    shift = request.GET.get('shift')
    starttime = request.GET.get('starttime')
    endtime = request.GET.get('endtime')
    days = request.GET.get('days')
    weekdays = {'1': "Monday", '2': "Tuesday", '3': "Wednesday", '4': "Thursday", '5': "Friday", '6': "Saturday", '7': "Sunday"}
    # print(date, days)

    if days in weekdays:
        days = weekdays[days]
    # print(days)
    a = User()
    a.emailaddress = emailaddress
    a.startdate = startdate
    a.dates = dates
    a.shift = shift
    a.starttime = starttime
    a.endtime = endtime
    a.days = days
    a.save()

    all = User.objects.all()
    p = {'item':all}
    
    return render(request, "records.html", p)