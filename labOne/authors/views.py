from django.shortcuts import render

# Create your views here.


def list_authors(request):
    authors = ['WilliamShakspeare', 'JKRowling',
               'AgathaCristie', 'NaguibMahfouz']
    context = {
        "list": authors
    }
    return render(request, "authors.html", context)


def view_author(request, name):
    context = {"author_name": name}
    return render(request,"oneauthor.html",context)

def view_harrypotter(request):
    return render(request,"HarryPotter.html")