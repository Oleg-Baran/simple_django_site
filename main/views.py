from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request): # request - запит (обов'язково)
    data = {
        'title': 'Main page!',
        'values': ['Some', 'Hello', '123'],
        'obj':{
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request): # request - запит (обов'язково)
    return render(request, 'main/about.html')
