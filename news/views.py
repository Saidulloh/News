from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.db.models import Q

from news.models import *
from .form import * 

from services.send_email import send_email


class HomeListView(generic.ListView):
    model = News
    template_name = 'include/main.html'

    def get_context_data(self, *, object_list = None ,**kwargs):
        context = super().get_context_data(**kwargs)
        context['world_news_slider'] = News.objects.filter(category='2')[:3]
        context['news_all'] = News.objects.all()
        context['news_slider'] = News.objects.all()[:3]
        context['category_all'] = Category.objects.all()[:4]
        context['news_tags'] = Tag.objects.all()
        return context


def news_views(request):
    if 'search_button' in request.GET:
        word = request.GET.get('search_word')
        news_all = News.objects.filter(Q(title__icontains = word))
        return render(request, 'include/category.html', locals())
    else:
        news_all = News.objects.all()
        news_slider = News.objects.all()[:3]
        world_news_slider = News.objects.filter(category='2')[:3]
        category_all = Category.objects.all()[:4]
        news_tags = Tag.objects.all()
        return render(request, 'include/main.html', locals())


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'include/category.html'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_all'] = Category.objects.all()
        context['news_all'] = News.objects.all()
        return context

 
class CategoryIdListView(generic.ListView):
    model = Category
    template_name = 'include/category.html'
    context_object_name = 'news_all'

    def get_context_data(self,*, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_all'] = Category.objects.all()
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['cat_id'])


class PostDetailView(generic.DetailView):
    model = News
    template_name = 'include/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_tags'] = Tag.objects.all()
        context['category'] = Category.objects.all()
        context['all_info'] = Comment.objects.filter(post_id=self.kwargs['post_id'])
        return context


class TagsIdListView(generic.ListView):
    model = News
    template_name = 'include/tag_page.html'
    context_object_name = 'news_tags_id'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_tags'] = Tag.objects.all()
        return context

    def get_queryset(self):
        return News.objects.filter(tags = self.kwargs['tag_id'])

        
class ContactsFormView(generic.FormView):
    model = ContactForm
    template_name = 'contacts.html'
    context_object_name = 'all_us'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        send_email(
            form.cleaned_data['name'],
            form.cleaned_data['email'],
            form.cleaned_data['subject'],
            form.cleaned_data['message'],
        )
        return super().form_valid(form) 


class NewsCreateView(generic.CreateView):
    form_class = AddPostsForm
    template_name = 'include/add_news.html'
    success_url = reverse_lazy('homepage')
    context_object_name = 'form'  


def update_news(request, id):
    if request.method == 'POST':
        ins = News.objects.get(id = id)
        form = AddPostsForm(request.POST or None, request.FILES, instance = ins)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = AddPostsForm()
    return render(request, 'include/add_news.html', locals())


def delete_news(request, id):
    del_new = News.objects.get(id = id)
    del_new.delete()
    return HttpResponseRedirect('/')


def add_comm(request, id):
    if request.method == 'POST':
        ind = News.objects.get(id = id)
        form = CommentForm(request.POST or None, instance = ind)
        if form.is_valid(): 
            form.save()
            return redirect('homepage')
    else:
        form = CommentForm()
    return render(request, 'include/post.html', locals())

