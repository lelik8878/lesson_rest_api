from django import forms

from lesson_signal.models import Sun


class SunForm(forms.ModelForm):
    class Meta:
        model = Sun
        fields = '__all__'
