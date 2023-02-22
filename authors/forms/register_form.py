from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from utils.django_forms import strong_password


class RegisterForm(forms.ModelForm):

    first_name = forms.CharField(required=True, label='Nome',
                                 error_messages={
                                     'required': 'Esse campo precisa estar preenchido'},  # noqa: E501
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Digite seu nome',
                                 })
                                 )

    last_name = forms.CharField(required=True, label='Sobrenome',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Digite seu Sobrenome',
                                })
                                )

    username = forms.CharField(required=True, label='Login',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Digite seu nome de usuário',
                               })
                               )

    email = forms.CharField(required=True, label='E-Mail',
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Digite seu e-mail',
                            })
                            )

    password = forms.CharField(required=True, label='Senha',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Digite sua senha',
                               }),
                               validators=[strong_password],
                               )

    confirm_password = forms.CharField(required=True, label='Confirmar Senha',
                                       widget=forms.PasswordInput(attrs={
                                           'class': 'form-control',
                                           'placeholder': 'confirme sua senha',
                                       }),
                                       )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'E-Mail já cadastrado',
                code='invalid',
            )

        return email

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        exists = User.objects.filter(username=username).exists()

        if exists:
            raise ValidationError(
                'Nome de usuário já cadastrado',
                code='invalid',
            )

        return username

    def clean_password(self):
        data = self.cleaned_data.get('password')

        if 'atenção' in data:
            raise ValidationError(
                'Não digite %(value)s no campo password',
                code='invalid',
                params={'value': '"atenção"'}
            )

        return data

    def clean(self):
        cleand_data = super().clean()
        password = cleand_data.get('password')
        confirm_password = cleand_data.get('confirm_password')

        if password != confirm_password:
            password_confirmation_error = ValidationError(
                'As senhas devem ser iguais',
                code='invalid',
            )

            raise ValidationError({
                'password': password_confirmation_error,
                'confirm_password': [
                    password_confirmation_error,
                ],
            })
