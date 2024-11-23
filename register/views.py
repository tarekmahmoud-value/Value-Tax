from django.shortcuts import render, redirect
from django.contrib import messages  # Import for displaying messages
from login.models import value_db  # Assuming your model is named 'value_db'
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def is_valid_email(email):
    try:
        validate_email(email)  # تحقق من صحة البريد
        return True
    except ValidationError:
        return False

def register_index(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")  # استخدم .get لتجنب الأخطاء إذا كانت القيم غير موجودة
        full_name = request.POST.get("full_name")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        Re_password = request.POST.get('re_password')

        # التحقق من صحة البريد الإلكتروني
        if not is_valid_email(mail):
            messages.warning(request, "Invalid email format")
            return redirect('register_index')

        # تحقق من وجود البريد الإلكتروني
        if value_db.objects.filter(mail__iexact=mail).exists():
            messages.warning(request, "This email already exists")
            return redirect('register_index')

        # Validate password match
        if password != Re_password:
            messages.warning(request, "Passwords do not match")
            return redirect('register_index')

        # Create new user instance with proper field names
        db = value_db()
        db.mail = mail
        db.full_name = full_name
        db.password = password
        db.phone = phone
        db.save()

        messages.success(request, "You have successfully registered")
        return redirect('/')  # Redirect to the home page after successful registration

    else:
        return render(request, 'register/index.html')
