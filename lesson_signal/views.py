from django.shortcuts import render

from lesson_signal.forms import SunForm


def get_sun(request):
    form = SunForm()
    if request.method == 'POST':
        received_form = SunForm(request.POST)
        if received_form.is_valid():
            print(received_form.cleaned_data)
            received_form.save()
    context = {'form': form}
    return render(request, "sun.html", context)
