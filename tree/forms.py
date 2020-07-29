from django import forms
from .models import Node


class AddForms(forms.Form):
    # Form used for adding new nodes
    name_add = forms.CharField(required=True, max_length=20, label='Nazwa', error_messages={'required': 'Wymagane!'})
    value_add = forms.IntegerField(required=True, label='Wartość', error_messages={'required': 'Wymagane!'})

    def clean_value_add(self, *args, **kwargs):
        # Overriding cleaning value function for proper validation
        value = self.cleaned_data.get("value_add")

        if value < 0:
            raise forms.ValidationError(
                "Wartość nie może być mniejsza od zera!"
            )
        if Node.objects.filter(value=value).exists():
            raise forms.ValidationError(
                "Taka wartość już istnieje!"
            )

        return value

    def clean_name_add(self, *args, **kwargs):
        # Overriding cleaning name function for proper validation
        name = self.cleaned_data.get("name_add")

        if Node.objects.filter(name=name).exists():
            raise forms.ValidationError(
                "Taka nazwa już istnieje!"
            )

        return name


class DeleteForms(forms.Form):
    # Form used for deleting any node from tree
    name_delete = forms.ModelChoiceField(required=True, queryset=Node.objects.all(), label='Nazwa')


class EditForms(forms.Form):
    # Form used for editing any node from tree
    id_edit = forms.ModelChoiceField(required=True, queryset=Node.objects.all(), label='Węzeł')
    name_edit = forms.CharField(required=False, max_length=20, label='Nazwa',)
    value_edit = forms.IntegerField(required=False, label='Wartość')

    def clean(self):
        # Overriding cleaning main function for proper validation
        cleaned_data = super().clean()

        id = cleaned_data.get("id_edit")
        name = cleaned_data.get("name_edit")
        value = cleaned_data.get("value_edit")

        if not name and not value or not id:
            raise forms.ValidationError(
                "Przynajmniej jeden atrybut musi być wybrany!"
            )
        return self.cleaned_data

    def clean_name_edit(self, *args, **kwargs):
        # Overriding cleaning name function for proper validation
        name = self.cleaned_data.get("name_edit")

        if Node.objects.filter(name=name).exists():
            raise forms.ValidationError(
                "Taka nazwa już istnieje!"
            )

        return name

    def clean_value_edit(self, *args, **kwargs):
        # Overriding cleaning vale function for proper validation
        value = self.cleaned_data.get("value_edit")

        if value:
            if value < 0:
                raise forms.ValidationError(
                    "Wartość nie może być mniejsza od zera!"
                )
        if Node.objects.filter(value=value).exists():
            raise forms.ValidationError(
                "Taka wartość już istnieje!"
            )

        return value


class SortForms(forms.Form):
    # Form used for sorting tree
    sort_all = forms.BooleanField(required=False, label='Sortuj')
