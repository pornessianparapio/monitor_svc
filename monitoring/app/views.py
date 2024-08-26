
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import check_password, make_password
from .models import Admin
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AdminSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def admin_login_or_register_view(request):
    if request.method == 'GET':
        # Check if any admin exists
        if Admin.objects.exists():
            return render(request, 'LoginPage.html')  # If admin exists, render the login page
        else:
            return render(request, 'RegistrationPage.html')  # If no admin exists, render the register page

        
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Check if the email and password match an existing admin
        admin = Admin.objects.filter(admin_email=email, admin_password=password).first()
        if admin:
            # Redirect to some admin dashboard or other secure page after successful login
            return JsonResponse({'detail': 'Admin Login successful'})
        else:
            return render(request, 'LoginPage.html', {'error': 'Invalid credentials.'})  # Re-render login page with error
            # return HttpResponseRedirect('templates/LoginPage.html')

class AdminRegisterView(APIView):
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            admin = serializer.save()
            return Response({'name': admin.admin_name, 'email': admin.admin_email,'password': admin.admin_password},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def forgot_password(request):
    if request.method == 'POST':
        email = request.data.get('admin_email')
        print(email)
        try:
            admin = Admin.objects.filter(admin_email=email).values()
            print(admin)
            if admin:
                token = get_random_string(50)  # Generate a random token
                reset_link = request.build_absolute_uri(reverse('reset_password', kwargs={'token': token}))
                print(reset_link)
                # Store the token in the session or the database as per your logic
                request.session['reset_token'] = token
                request.session['reset_email'] = email

                # Send email
                try:
                    send_mail(
                        'Password Reset Request',
                        f'Click the link to reset your password: {reset_link}',
                        'svcwrkofc123@gmail.com',
                        [email],
                        fail_silently=False,
                    )
                except Exception as e:
                    return HttpResponse(f"can not send email {e}")
                return HttpResponse("Password reset link sent to your email.")
        except Admin.DoesNotExist:
            return HttpResponse("This email is not registered.")

    # return render(request, 'forgot_password.html')


def reset_password(request, token):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            email = request.session.get('reset_email')
            try:
                admin = Admin.objects.get(admin_email=email)
                if request.session.get('reset_token') == token:
                    admin.admin_password = make_password(new_password)
                    admin.save()
                    return HttpResponse("Password has been reset successfully.")
            except Admin.DoesNotExist:
                return HttpResponse("Invalid reset link.")

        return HttpResponse("Password do not match.")

    # return render(request, 'reset_password.html', {'token': token})

# class AdminRegistration(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = AdminSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         #     return Response({"message": "Admin created successfully"}, status=status.HTTP_201_CREATED)
#         # return Response(serializer.errors, status=
#             return redirect('LoginPage.html')
#         return render(request, 'RegistrationPage.html', {'errors': serializer.errors})
