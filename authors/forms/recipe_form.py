from collections import defaultdict

from django import forms
from django.core.exceptions import ValidationError

from recipes.models import Recipe


class AuthorRecipeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

    class Meta:
        model = Recipe
        fields = 'title', 'description', 'preparation_time', \
                 'preparation_time_unit', 'servings', 'servings_unit', \
                 'preparation_steps', 'cover'

    title = forms.CharField(required=True, label='Título',
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Digite seu título',
                            }),
                            )

    description = forms.CharField(required=True, label='Descrição',
                                  widget=forms.TextInput(attrs={
                                      'class': 'form-control',
                                      'placeholder': 'Digite seu título',
                                  }),
                                  )

    preparation_time = forms.CharField(required=True, label='Tempo de preparo',
                                       widget=forms.TextInput(attrs={
                                           'class': 'form-control',
                                           'placeholder': 'Digite seu título',
                                       }),
                                       )

    preparation_time_unit = forms.CharField(required=True, label='Unidade de tempo de preparo',
                                            widget=forms.Select(
                                                attrs={
                                                    'class': 'form-select',
                                                    'placeholder': 'Digite seu título',
                                                },
                                                choices=(
                                                    ('Minutos', 'Minutos'),
                                                    ('Horas', 'Horas'),
                                                )),

                                            )

    servings = forms.CharField(required=True, label='Serve',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Digite seu título',
                               }),
                               )

    servings_unit = forms.CharField(required=True, label='Unidade',
                                    widget=forms.Select(
                                        attrs={
                                            'class': 'form-select',
                                            'placeholder': 'Digite seu título',
                                        },
                                        choices=(
                                            ('Porções', 'Porções'),
                                            ('Pedaços', 'Pedaços'),
                                            ('Pessoas', 'Pessoas'),
                                        )),
                                    )

    preparation_steps = forms.CharField(required=True, label='Passo a passo',
                                        widget=forms.Textarea(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Digite seu título',
                                        }),
                                        )

    cover = forms.CharField(required=True, label='Cover',),

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cd = self.cleaned_data
        title = cd.get('title')

        if len(title) < 5:
            self._my_errors['title'].append('Deve ter ao menos 5 caracteres')

        if self._my_errors:
            raise ValidationError(self._my_errors)

        return super_clean
