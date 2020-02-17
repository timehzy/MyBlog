from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    # return HttpResponse("Hello, world!")
    # artical = models.Artical.object.get(pk = 1)
    all_artical = models.Artical.object.all()
    return render(request, 'blog/index.html', {"articals": all_artical})

def artical_page(request, artical_id):
    artical = models.Artical.object.get(pk=artical_id)
    return render(request, 'blog/artical_page.html', {"artical": artical})

def edit_page(request, artical_id):
    if str(artical_id) == '0':
        return render(request, 'blog/edit_page.html')
    else:
        artical = models.Artical.object.get(pk=artical_id)
        return render(request, 'blog/edit_page.html', {'artical': artical})

def edit_submit(request):
    title = request.POST.get('title', 'default')
    content = request.POST.get('content', 'default')
    artical_id = request.POST.get('id', '0')
    if artical_id == '0':
        models.Artical.object.create(title=title, content=content)
        all_artical = models.Artical.object.all()
        return render(request, 'blog/index.html', {"articals": all_artical})
    else:
        artical = models.Artical.object.get(pk=artical_id)
        artical.title = title
        artical.content = content
        artical.save()
        return render(request, 'blog/artical_page.html', {"artical": artical})

