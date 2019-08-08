from django.shortcuts import render
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new

from .forms import ModelsForm, PhotoForm
from .models import Models, Photo


class ModelsPageView(ListView):
    model = Models
    template_name = 'model/model.html'
    paginate_by = 4
    queryset = Models.objects.all()

    def get_queryset(self, *args, **kwargs) :
        if self.kwargs :
            return Models.objects.filter(category=self.kwargs['category']).order_by('-id')
        else :
            query = Models.objects.all().order_by('-id')
            return query


class CreateModelsView(CreateView) :
    model = Models
    form_class = ModelsForm
    template_name = 'model/model_post.html'
    success_url = reverse_lazy('model')


def detail(request, model_id):
    post_detail = Models.objects.get(pk=model_id)
    return render(request, 'model/model_detail.html', {'post_detail': post_detail})


def filter_orient(request):
    post_orient = Models.objects.filter(category="동양풍")
    return render(request, 'model/filter_orient.html', {'post_orient': post_orient,})


def filter_western(request):
    post_western = Models.objects.filter(category="서양풍")
    return render(request, 'model/filter_western.html', {'post_western':post_western,})


def filter_classic(request):
    post_classic = Models.objects.filter(category="고전")
    return render(request, 'model/filter_classic.html', {'post_classic':post_classic,})


def filter_modern(request):
    post_modern = Models.objects.filter(category="현대")
    return render(request, 'model/filter_modern.html', {'post_modern':post_modern,})


class PhotoPageView(ListView):
    model = Photo
    template_name = 'photo/photo.html'
    paginate_by = 4
    queryset = Photo.objects.all()

    def get_queryset(self, *args, **kwargs):
        if self.kwargs :
            return Photo.objects.filter(category=self.kwargs['category']).order_by('-id')
        else :
            query = Photo.objects.all().order_by('-id')
            return query


class PhotoCreatePostView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photo/photo_post.html'
    success_url = reverse_lazy('photo')


def photo_detail(request, photo_id):
    photo_post_detail = Photo.objects.get(pk=photo_id)
    return render(request, 'photo/photo_detail.html', {'photo_post_detail':photo_post_detail})


def photo_filter_orient(request):
    photo_post_orient = Photo.objects.filter(category="동양풍")
    return render(request, 'photo/photo_filter_orient.html', {'photo_post_orient': photo_post_orient,})

def photo_filter_western(request):
    photo_post_western = Photo.objects.filter(category="서양풍")
    return render(request, 'photo/photo_filter_western.html', {'photo_post_western':photo_post_western,})

def photo_filter_classic(request) :
    photo_post_classic = Photo.objects.filter(category="고전")
    return render(request, 'photo/photo_filter_classic.html', {'photo_post_classic':photo_post_classic,})

def photo_filter_modern(request) :
    photo_post_modern = Photo.objects.filter(category="현대")
    return render(request, 'photo/photo_filter_modern.html', {'photo_post_modern':photo_post_modern,})



