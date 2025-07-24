from django.shortcuts import render

from django.views.generic import ListView, DetailView
from blog.models import Blog_record


# class ContactsView(TemplateView):
#     template_name = 'catalog/contacts.html'


class RecordListView(ListView):
    model = Blog_record


class RecordDetailView(DetailView):
    model = Blog_record
