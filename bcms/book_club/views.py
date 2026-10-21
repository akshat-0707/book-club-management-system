from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import User, Club, Membership

def index(request):
    joined_club_names = []
    if request.user.is_authenticated:
        joined_club_names = Membership.objects.filter(user=request.user).values_list('club__name', flat=True)
    return render(request, "book_club/index.html", {
        "clubs": list(joined_club_names)
    })

def club_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        try:
            Club.objects.create(name=name, description=description, created_by=request.user)
            return render(request, 'book_club/index.html')
        except IntegrityError:
            message = "club with this name aready exists,please choose another name."
            return render(request, 'book_club/create_club.html',{
                "message" : message
            })
    else:
        return render(request, 'book_club/create_club.html')

@login_required
def join_club(request, club_id):
    if request.method == "POST":
        club = get_object_or_404(Club, id=club_id)
        # Safely creates a membership if it doesn't already exist
        Membership.objects.get_or_create(
            user=request.user, 
            club=club, 
            defaults={'role': 'member'}
        )
    return HttpResponseRedirect(reverse("clubs"))

def club_list(request):
    all_clubs = Club.objects.all()
    
    joined_club_ids = []
    if request.user.is_authenticated:
        joined_club_ids = Membership.objects.filter(user=request.user).values_list('club_id', flat=True)
        
    return render(request, 'book_club/clubs.html', {
        "clubs": all_clubs,
        "joined_club_ids": list(joined_club_ids), 
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        return render(request, "book_club/login.html", {
            "message": "Invalid username and/or password."
        })
    return render(request, "book_club/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            return render(request, "book_club/register.html", {
                "message": "Passwords do not match."
            })
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return render(request, "book_club/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "book_club/register.html")