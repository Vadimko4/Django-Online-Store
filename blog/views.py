from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog_record


class RecordListView(ListView):
    model = Blog_record

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class RecordDetailView(DetailView):
    model = Blog_record


class RecordCreateView(CreateView):
    model = Blog_record
    fields = ("title", "content", "preview", "published")
    success_url = reverse_lazy('blog:record_list')


class RecordUpdateView(UpdateView):
    model = Blog_record
    fields = ("title", "content", "preview", "published")
    success_url = reverse_lazy('blog:record_list')


class RecordDeleteView(DeleteView):
    model = Blog_record
    success_url = reverse_lazy('blog:record_list')
