from django.shortcuts import render, get_object_or_404
from pages.models import Page
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

def home(request):
    return HttpResponse("You're looking at a page :) {% url 'index' %}")

def index(request):
    latest_page_list = Page.objects.all().order_by('-pub_date')[:5]
    context = {'latest_page_list': latest_page_list}
    return render(request, 'pages/index.html', context)

def pageid(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    context = {'page': page}
    return render(request, 'pages/detail.html', context)
# 
# def words(request, page_word):
#     return HttpResponse("You're looking at page %s." % page_word)
# 
def words(request, page_word):
    try:
        instance = Page.objects.get(word=page_word)
        page = get_object_or_404(Page, word=page_word)
        context = {'page': page}
    except Page.DoesNotExist:
        return HttpResponseRedirect("/pages/post-page/") 
    return render(request, 'pages/detail.html', context)

def edit(request, word_edit):
    return HttpResponse("editing page %s" % word_edit)

def about(request, page_word):
    return render(request, 'pages/about.html')

class EditPageView(UpdateView):
    model = Page
    fields = ['word','definition']
    template_name = 'pages/edit.html'

class PostPageView(CreateView):
    model = Page
    fields = ['word','definition','pub_date']
    template_name = 'pages/newpage.html'
    

class DeletePageView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:index')
