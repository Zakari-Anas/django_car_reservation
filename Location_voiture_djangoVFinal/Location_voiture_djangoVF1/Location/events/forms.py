from .models import *
from django.forms import ModelForm, NumberInput
from django import forms
from django.utils import timezone
from django.forms.widgets import TextInput, EmailInput, FileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class updatecarForm(ModelForm):
    class Meta:
        model=car
        fields=[
                'name',
                'model',
                'price',
                'description',
                'distance',
                'image'
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car name'}),
            'model': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car model'}),
            'price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter car price'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car description'}),
            'distance': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter car distance'}),
            'image': FileInput(attrs={'class': 'form-control'})
}

class addcarForm(ModelForm):
    class Meta:
        model=car
        fields=[
                'name' ,
                'model',
                'price',
                'description',
                'distance',
                'image'
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car name'}),
            'model': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car model'}),
            'price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter car price'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car description'}),
            'distance': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter car distance'}),
            'image': FileInput(attrs={'class': 'form-control'})
        }

class LoginForm(forms.Form):
    
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class adduserForm(ModelForm):
    class Meta:
        model = user
        fields = ['name', 'email', 'city', 'image']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'image': FileInput(attrs={'class': 'form-control'})

        }
#         , 'style': 'width: 60%; font-size: 16px; font-family: Arial; display: inline-block; float: center;'
#         , 'style': 'width: 60%; font-size: 16px; font-family: Arial; display: inline-block; float: center;'
# , 'style': 'width: 60%; font-size: 16px; font-family: Arial; display: inline-block; float: center;left:35px;'
# , 'style': 'width: 60%; font-size: 16px; font-family: Arial; display: inline-block; margin: 15px;'

class updateuserForm(ModelForm):
    class Meta:
        model=user
        fields = ['name', 'email', 'city', 'image']
        widgets = {
             'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city' }),
            'image': FileInput(attrs={'class': 'form-control', })
}

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['car', 'user', 'reservation_date', 'return_date']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'return_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }
        initial = {
            'reservation_date': timezone.now(),
            'return_date': timezone.now() + timezone.timedelta(days=7)
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].queryset = car.objects.all()
        self.fields['user'].queryset = user.objects.all()


#add
class RegistrationForm(UserCreationForm):
      username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
      first_name =forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
      last_name =forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
      email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))

      class Meta:
         model=User
         fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


      def __init__(self, *args, **kwargs):
                super(RegistrationForm, self).__init__(*args, **kwargs)

                self.fields['password1'].widget.attrs['class'] = 'form-control'
                self.fields['password2'].widget.attrs['class'] = 'form-control'
                self.fields['password1'].help_text=None
                self.fields['password2'].help_text=None


