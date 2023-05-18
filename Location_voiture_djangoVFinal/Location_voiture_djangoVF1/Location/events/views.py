from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import *
from .forms import updatecarForm
from .forms import addcarForm
from .forms import LoginForm
from .forms import ReservationForm
from .forms import adduserForm
from .forms import updateuserForm
from .forms import RegistrationForm
from events import forms





def home(request):
       
        listcars= car.objects.all()

        return render(request, 'home.html', {'data' : listcars})

# def find_cars_by_name(request,name):
       
#         findcars= car.objects.filter(name=name)

#         return render(request, 'cars_name.html', {'data' : findcars})


def find_by_id(request,id):
       
        findcar= car.objects.get(id=id)

        return render(request, 'car_id.html', {'data' : findcar})

def update_car(request,id):
        findCar=get_object_or_404(car, id=id)
        form=updatecarForm(instance=findCar)
        if request.method=='POST':
            form=updatecarForm(request.POST, instance=findCar, files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'update_car.html', {'form' : form})

def delete_car(request,id):
        findCar=get_object_or_404(car, id=id)
        if findCar:
              car.delete(findCar)
        return redirect('home')

def search(request):
    filter = request.GET.get('filter')
    query = request.GET.get('query')
    cars = []

    if filter == 'name':
        cars = car.objects.filter(name__icontains=query)
    elif filter == 'model':
        cars = car.objects.filter(model__icontains=query)
    elif filter == 'price':
        cars = car.objects.filter(price__icontains=query)
    elif filter == 'description':
        cars = car.objects.filter(description__icontains=query)
    elif filter == 'distance':
        cars = car.objects.filter(distance__lt=query)

    return render(request, 'home.html', {'data': cars})

def addcar(request):
      form=addcarForm()
      if request.method=='POST':
            form=addcarForm(request.POST, files=request.FILES)
            if form.is_valid():
                  form.save()
                  return redirect('home')
        
            
      return render(request, 'addcar.html', {'form' : form})


def login_user(request):
    
        if request.method == 'POST':
                form=LoginForm(request.POST)
                if form.is_valid():
                        cd=form.cleaned_data
                        user=authenticate(request, username=cd['email'], password=cd['password'])
                        if user is not None:
                                if user.is_active:
                                        login(request, user)
                                        return redirect('home')
                                else:
                                        
                                        HttpResponse('Disabled account')
                                        return redirect('login')
                        else:
                            HttpResponse('Invalid login')
                            return redirect('login')
                            
                else:
                        form=LoginForm()
                        return render(request, 'login_user.html', {'form': form})
        form=LoginForm()
        return render(request, 'login_user.html', {'form': form})


def users(request):

        listusers= user.objects.all()
        return render(request, 'users.html', {'data' : listusers})

# @login_required
def reserve_car(request):


        if request.method == 'POST':
                form = forms.ReservationForm(request.POST)
                if form.is_valid():
                        selected_car = form.cleaned_data['car']
                        selected_user = form.cleaned_data['user']
                        reservation_date = form.cleaned_data['reservation_date']
                        return_date = form.cleaned_data['return_date']
                        reservation = Reservation.objects.create(user=selected_user, car=selected_car, reservation_date=reservation_date, return_date=return_date)
                        return redirect('reservations')
        else:
                form = ReservationForm()
        return render(request, 'make_reservation.html', {'form': form})


def reservations(request):
        reservations = Reservation.objects.all()
        return render(request, 'reservations.html', {'data': reservations})


def find_reservation_by_id(request, id):
               findreservation = Reservation.objects.get(id=id)
               
               return render(request, 'reservation_id.html', {'data': findreservation})       

def delete_reservation(request,id):

        findreservation=get_object_or_404(Reservation, id=id)
        if findreservation:
              Reservation.delete(findreservation)
        return redirect('reservations')     

def update_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations')
    else:
        form = ReservationForm(instance=reservation)
    
    return render(request, 'update_reservation.html', {'data': reservation, 'form': form})

       
def search_reservations(request):
    
    filter = request.GET.get('filter')
    query = request.GET.get('query')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if filter == 'car':
        reservations = Reservation.objects.filter(car__icontains=query, reservation_date__range=(start_date, end_date))
    elif filter == 'user':
        reservations = Reservation.objects.filter(user__icontains=query, reservation_date__range=(start_date, end_date))
    elif filter == 'date':
        reservations = Reservation.objects.filter(reservation_date__range=(start_date, end_date))
    else:
        reservations = Reservation.objects.all()

    return render(request, 'reservations.html', {'reservations': reservations})
                

def add_user(request):
        form=adduserForm()
        if request.method=='POST':
                form=adduserForm(request.POST, files=request.FILES)
                if form.is_valid():
                        form.save()
                        return redirect('users')
          
                
        return render(request, 'adduser.html', {'form' : form})

def update_user(request,id):
        findUser=get_object_or_404(user, id=id)
        form=updateuserForm(instance=findUser)
        if request.method=='POST':
            
            form=updateuserForm(request.POST, instance=findUser, files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect('users')
        return render(request, 'update_user.html', {'form' : form})

def delete_user(request,id):
        findUser=get_object_or_404(user, id=id)
        if findUser:
              user.delete(findUser)
        return redirect('users')

def find_user_by_id(request,id):
       
        finduser= user.objects.get(id=id)

        return render(request, 'user_id.html', {'data' : finduser})

def research_user(request):
        filter_by = request.GET.get('filter')
        query = request.GET.get('query')
        
        if filter_by == 'name':
                users = user.objects.filter(name__icontains=query)
        elif filter_by == 'email':
                users = user.objects.filter(email__icontains=query)
        elif filter_by == 'city':
                users = user.objects.filter(city__icontains=query)
        else:
                users = user.objects.none()

        return render(request, 'users.html', {'data': users})


              
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the desired page after logout


#add signUp
def register_user(request):
    if request.method == "GET":
        form2 = RegistrationForm(request.GET)
        if form2.is_valid():
            form2.save()
            HttpResponse("data saved")
            return redirect('login')
    else:
        form2 = RegistrationForm()
    return render(request, 'register_user.html', {
            'form_data' : form2,
        })