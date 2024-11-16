from django.contrib.auth import authenticate, login as auth_login

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                # Automatically log in the user
                auth_login(request, user)
                messages.success(request, 'Account created successfully! You are now logged in.')
                return redirect('courses')  # Redirect to the courses page or homepage
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'accounts/register.html')
