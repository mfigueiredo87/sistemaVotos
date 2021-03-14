from django.shortcuts import render

#definindo a pagina inicial
def index(request):
    return render(request, 'pages/index.html')
