from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)

    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'type':'text', 'class':'contactus', 'name':'first_name', 'placeholder':'Enter Your First Name'})
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'type':'text', 'class':'contactus', 'name':'last_name', 'placeholder':'Enter Your Last Name'})
    )
    email = forms.EmailField(
        label="Email ",
        widget=forms.TextInput(attrs={'type':'email', 'class':'contactus', 'name':'email', 'placeholder':'Enter Your Email Address'})
    )
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'type':'text', 'class':'contactus', 'name':'username', 'placeholder':'Enter Your Username',  'autofocus': False})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
        attrs={
            'class':'contactus',
            'name':'password',
            'type':'password',
            'placeholder': 'Enter Your Password'
        }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
        attrs={
            'class':'contactus',
            'name':'password',
            'type':'password',
            'placeholder': 'Enter Your Password Again'
        }
        )
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        )



class UpdateUserForm(UserChangeForm):
    password = None

    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'type':'text', 'class':'contactus', 'name':'first_name', 'placeholder':'Your First Name'})
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'type':'text', 'class':'contactus', 'name':'last_name', 'placeholder':'Your Last Name'})
    )
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'type':'text', 'class':'contactus', 'name':'username', 'placeholder':'Your Username', 'autofocus': False})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'type':'email', 'class':'contactus', 'name':'email', 'placeholder':'Your Email Address'})
    )

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')



class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'contactus',
                'name':'password',
                'type':'password',
                 'placeholder': 'Enter Your New Password'
            }
        )
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'contactus',
                'name':'password',
                'type':'password',
                'placeholder': 'Enter Your New Password Again'
            }
        )
    )

    class Meta:
        model = User
        fields = ('new_password1','new_password2')

