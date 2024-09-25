from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore


# Create your views here.
def UserLogin(request):

    
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        captcha_key = request.POST.get("captcha_0")  # Captcha key
        captcha_value = request.POST.get("captcha_1")  # User-entered captcha text

        # Validate CAPTCHA
        try:
            captcha_obj = CaptchaStore.objects.get(hashkey=captcha_key)
            # Case-insensitive comparison
            if captcha_obj.response.lower() != captcha_value.lower():
                messages.error(request, "Invalid CAPTCHA.")
                return redirect("captcha-login")
        except CaptchaStore.DoesNotExist:
            messages.error(request, "Invalid CAPTCHA.")
            return redirect("captcha-login")

        # Authenticate user
        user_auth = authenticate(request, username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("captcha-login")

    # Generate CAPTCHA for GET requests
    captcha_key = CaptchaStore.generate_key()
    captcha_image = captcha_image_url(captcha_key)

    context = {"captcha_image": captcha_image, "captcha_key": captcha_key}

    return render(request, "login.html", context)


@login_required(login_url="/", redirect_field_name="authentication_required")
def dashboard(request):

    return render(request, 'dashboard.html')

def render_logout(request):

    logout(request)

    return redirect("captcha-login")