from django.shortcuts import render

# Create your views here.
def usuario(request):
    print("Login")
    return render(
        request,
        'usuario/login.html'
)