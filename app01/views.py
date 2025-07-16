from django.shortcuts import render
def lista_frutas(request):
    frutas = ['Banana', 'Maçã', 'Abacaxi', 'Laranja','Morango']
    return render(request, 'lista_frutas.html', {'frutas': frutas})
   

