from django.shortcuts import render

# Create your views here.
def about(request):
    days=[
{'name': 'ahmad', 'age': 27},
{'name': 'musa', 'age': 28},
{'name': 'abdullah', 'age': 29},
]
    return render(request,('about.html'),{'days':days})

def contact(request):
    return render(request,('contact.html'))