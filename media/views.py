from django.shortcuts import render
from .models import Image
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404

# Create your views here.
def gallery(request):
    categories = Image.objects.distinct().values_list('category__name', flat=True)
    locations = Image.objects.distinct().values_list('location__name', flat=True)
    try:
        images = Image.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'gallery.html', {'images': images, 'locations':locations, 'categories': categories})
def search_images(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET('image')
        searched_images = Image.search_by_name(search_term)
        message = f'{search_term}'
        return render(request, 'search.html', {'message': message, 'images': searched_images})
    else:
        message = "You have not searched for any term"
        return render(request, 'search.html', {'message': message})
def home(request):
    
    return render(request, 'media/home.html')
