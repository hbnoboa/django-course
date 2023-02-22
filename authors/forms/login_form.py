from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(required=True, label='Login',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Digite seu nome de usuário',
                               }),
                               )

    password = forms.CharField(required=True, label='Senha',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Digite sua senha',
                               }),
                               )
