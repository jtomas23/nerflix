# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nerflix.models import Movie
from django.shortcuts import render, get_object_or_404
from nerflix.forms import MovieForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def movie_list(request):
    data = {}

    data['object_list'] = Movie.objects.all().order_by('-id')


    template_name = 'movie/movie_list.html'
    return render(request, template_name, data)


def movie_form(request):

    template_name = 'movie/movie_form.html'
    form = MovieForm(request.POST or None)

    if form.is_valid() :
        form.save()
        return HttpResponseRedirect(reverse('movie_list'))

    return render(request, template_name, {'form': form})

def movie_update(request, pk) :
    template_name = 'movie/movie_form.html'
    # movie = Movie.objects.get(pk=pk)
    movie = get_object_or_404(Movie, pk=pk)
    # select * from movie WHERE id = xx

    form = MovieForm(request.POST or None, instance=movie)

    if form.is_valid() :
        form.save()
        return HttpResponseRedirect(reverse('movie_list'))

    return render(request, template_name, {'form': form})



def movie_delete(request, pk) :
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return HttpResponseRedirect(reverse('movie_list'))
