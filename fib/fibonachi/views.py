from django.shortcuts import render
from .forms import FibForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse


def stop_vib(n1, n2, numb):
    if numb == 0:
        return 0
    elif n1 == numb or numb - n1 < n2 - numb:
        return n1
    elif n2 == numb or n2 - numb < numb - n1:
        return n2
    elif numb - n1 == n2 - numb:
        return n1


def fibonachi(number):
    number = int(number)
    numb = 0
    n1 = 0
    n2 = 1
    while number >= numb:
        numb = n1 + n2
        n1 = n2
        n2 = numb
    return stop_vib(n1, n2, number)


def index(request):
    number = 15
    number = int(request.POST.get("number_input"))
    fib_form = FibForm(request.POST or None)
    if number < 0:
        return HttpResponse("Число должно быть положительным")
    if request.method == "POST":
        fibonachi_number = fibonachi(number)
        if fib_form.is_valid():
            fib = fib_form.save(commit=False)
            fib.number_output = fibonachi_number
            fib.save()
            return HttpResponse(fibonachi_number)
    else:
        fib_form = FibForm()
    return render(request, "index.html", {"form": fib_form})
