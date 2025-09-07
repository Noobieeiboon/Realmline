from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

@login_required
@api_view(["GET", "POST"])
def index(request):
    """
    This should basically return call the chat rooms but as of now just retrun hello, will come back to it later
    """
    return Response(f"Hello {request.user}", status=status.HTTP_200_OK)



@api_view(["GET", "POST"])
def signin(request):
    """
    Login page, just return the confirmation of login
    """
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response("Logged in!!!s", status=status.HTTP_200_OK)
    else:
        return Response("Unable to login, please try again", status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def signup(request):
    email = request.data.get("email")
    username = request.data.get("username")
    user_age = request.data.get("user_age")
    user_bio = request.data.get("user_bio")
    password = request.data.get("password")

    if User.objects.filter(email=email).exists():
        return Response("Sorry Mate :( , Account already exists , try logging in...",
            status=status.HTTP_401_UNAUTHORIZED
        )

    user = User.objects.create_user(
        email=email,
        username=username,
        user_age=user_age,
        user_bio=user_bio,
        password=password
    )


    return Response("User account successfully created!!!", status=status.HTTP_201_CREATED)



@csrf_exempt
@api_view(["GET", "POST"])
def signout(request):
    """
    Signout
    """
    if request.user.is_authenticated:
        logout(request)
        return Response("Signed-out successfully!!!", status=status.HTTP_201_CREATED)
    else:
        return Response("You are not logged in yet, to logout", status=status.HTTP_400_BAD_REQUEST)
