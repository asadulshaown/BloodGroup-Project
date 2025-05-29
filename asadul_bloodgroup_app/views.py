from django.shortcuts import render, redirect
from .models import blooddonation

# Create your views here.

def Home(request):
  return render(request, 'home.html')

def Registar(request):
  if request.method == 'POST':
    user_name = request.POST['name']
    user_number = request.POST['number']
    user_address = request.POST['address']
    blood_group = request.POST['blood_group']
    donation_date = request.POST['donation_date']
    
    user_all_info = blooddonation(name=user_name, number=user_number, address=user_address, blood_group=blood_group, donation_date=donation_date)
    user_all_info.save()
    return redirect('/')
  else:
    return render(request, 'registar.html')

def display_data(request):
  user_all_data = blooddonation.objects.all()
  send_data = {'data':user_all_data}
  return render(request, 'display_data.html', send_data)