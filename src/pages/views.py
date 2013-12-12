from django.shortcuts import render, get_object_or_404

# Create your views here.
from pages.models import Page
from django.http import HttpResponse, Http404

def index(request):
    latest_page_list = Page.objects.all().order_by('-pub_date')[:5]
    context = {'latest_page_list': latest_page_list}
    return render(request, 'pages/index.html', context)

def detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'pages/detail.html', {'page': page})
# 
# def words(request, page_word):
#     return HttpResponse("You're looking at page %s." % page_word)
# 
def words(request, page_word):
    page = get_object_or_404(Page, word=page_word)
    return render(request, 'pages/detail.html', {'page': page})

def get_absolute_url(self):
    return reverse("word", args=(self.words,))