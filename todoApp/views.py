from django.shortcuts import redirect

def index(request):
    return redirect('/todos')

def test(request):
    pass