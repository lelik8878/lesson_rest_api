from django import forms


class SaveDataForm(forms.Form):
    name = forms.CharField()
    price = forms.DecimalField(max_digits=5, decimal_places=2)
    image = forms.ImageField()