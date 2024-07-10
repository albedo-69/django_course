from django import forms
from django.contrib.auth import get_user_model


class UserLogin(forms.Form):
    username = forms.CharField(label='Логин', 
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', 
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    
class UserRegister(forms.ModelForm):
    username = forms.CharField(label='Логин', 
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    password = forms.CharField(label='Пароль', 
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    password2 = forms.CharField(label='Повтор пароля', 
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        labels = {
            'username': 'Имя пользователя',
            'password': 'Пароль'
        }
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли должны быть одинаковыми')
        return cd['password']
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует.')
        return username
    
        
        