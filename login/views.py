from django.shortcuts import render, redirect
from .models import value_db
from django.contrib import messages

def login_index(request):
    if request.method == 'POST':

        mail = request.POST.get('mail', '').strip()
        password = request.POST.get('password', '').strip()

        user = value_db.objects.filter(mail=mail, password=password).first()
        admin = (mail == "tarek.mahmoud@value.com", password == "0103651254")

        if admin == (True,True):
            return redirect('admin/')
        else:
            if user:
                if user.approval == 1:
                    request.session["mail"] = mail
                    return render(request, 'home/index.html')
                else:
                    messages.warning(request, "Please contact the admin at (01143839788) to grant permission")

                    return redirect('login_index')
            else:
                messages.error(request, "incorrect email or password")
                return redirect('login_index')

    return render(request, 'login/index.html')
