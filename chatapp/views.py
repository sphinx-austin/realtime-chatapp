from django.shortcuts import render

# Create your views here.
def test(request):
    name = f"Hello"

    context = {
        name : 'Austine',


    }

    return render(request, 'chatapp/index.html', context)