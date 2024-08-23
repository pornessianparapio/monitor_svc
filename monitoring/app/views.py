

# Create your views here.
from django.http import JsonResponse, HttpResponseBadRequest,HttpResponseRedirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AdminSerializer
from .models import Admin
import random
import string
class AdminRegisterView(APIView):
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            admin = serializer.save()
            return Response({'name': admin.admin_name, 'email': admin.admin_email,'password': admin.admin_password},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminView(APIView):
    def post(self,request):
        email = request.data.get('admin_email')
        password = request.data.get('admin_password')
        print(email,password)
        admin = Admin.objects.filter(admin_email=email,admin_password=password).values()
        print(admin)
        if admin:
            return Response({'detail': 'Admin Login successful'})
        else:
            return Response({'detail': 'Invalid credentials'})

# class Employee(APIView):
#     def post(self,request):
#         e_name = request.POST['e_name']
#         e_contact = request.POST['e_contact']
#         e_email = request.POST['e_email']
#         e_password = request.POST['e_password']
#         employee = Employee.objects.filter(employee_name=e_ename,employee_password=e_password)

def admin_forgot_password(request):
    if request.method == 'POST':
        admin_email = request.data.get('admin_email')

        if not admin_email:
            return HttpResponseBadRequest("e_email parameter is required.")

        admin_details = Admin.objects.filter(admin_email=admin_email).first()

        if admin_details:
            otp = ''.join(random.choices(string.digits, k=6))  # Generate OTP
            # Update the employee's record with the generated OTP (assuming there's an e_otp field)
            admin_details.admin_otp = otp
            admin_details.save()
            return JsonResponse({
                                    "message": "OTP generated successfully.This step will be takes place when email creadentials are fullfill.",
                                    "otp": otp})
        else:
            return JsonResponse({"error": "Admin not found."}, status=404)

    return HttpResponseBadRequest("Only POST method is allowed.")


