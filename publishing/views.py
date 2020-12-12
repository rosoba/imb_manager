from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)

from .forms import PublicationForm
from .models import Publication


class PublicationCreateView(CreateView):
    template_name = 'publishing/publication_create.html'
    form_class = PublicationForm
    queryset = Publication.objects.all()  # <blog>/<modelname>_list.html

    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
       return '/'


class PublicationListView(ListView):
    template_name = 'publishing/publication_list.html'
    queryset = Publication.objects.all()  # <blog>/<modelname>_list.html


class PublicationDetailView(DetailView):
    template_name = 'publishing/publication_detail.html'

    # queryset = Publication.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Publication, id=id_)


class PublicationUpdateView(UpdateView):
    template_name = 'publishing/publication_create.html'
    form_class = PublicationForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Publication, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class PublicationDeleteView(DeleteView):
    template_name = 'publishing/publication_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Publication, id=id_)

    def get_success_url(self):
        return reverse('publishing:publication-list')
