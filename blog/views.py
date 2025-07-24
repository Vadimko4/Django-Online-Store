from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView
from blog.models import Blog_record


# class ContactsView(TemplateView):
#     template_name = 'catalog/contacts.html'


class RecordListView(ListView):
    model = Blog_record


class RecordDetailView(DetailView):
    model = Blog_record


class RecordCreateView(CreateView):
    model = Blog_record
    fields = ("title", "content", "preview", "published")
    success_url = reverse_lazy('blog:record_list')
