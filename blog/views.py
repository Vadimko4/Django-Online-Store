from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog_record


class RecordListView(ListView):
    model = Blog_record

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(published=True)


class RecordDetailView(DetailView):
    model = Blog_record

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class RecordCreateView(CreateView):
    model = Blog_record
    fields = ("title", "content", "preview", "published")
    success_url = reverse_lazy('blog:record_list')


class RecordUpdateView(UpdateView):
    model = Blog_record
    fields = ("title", "content", "preview", "published")
    success_url = reverse_lazy('blog:record_list')

    def get_success_url(self):
        return reverse('blog:record_detail', args=[self.kwargs.get('pk')])


class RecordDeleteView(DeleteView):
    model = Blog_record
    success_url = reverse_lazy('blog:record_list')
