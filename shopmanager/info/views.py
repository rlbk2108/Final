from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Info


class InfoListView(ListView):
    model = Info
    context_object_name = 'information'
    template_name = 'info/info.html'


class InfoDetailView(DetailView):
    model = Info
    context_object_name = 'detailinfo'
    template_name = 'info/info_detail.html'