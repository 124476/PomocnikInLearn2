import random

import django.shortcuts
from django.views.generic import View, ListView, DetailView
from django.shortcuts import get_object_or_404
from django.utils.html import strip_tags

from apps.learn.models import Object, Material


class ThemeListView(ListView):
    model = Object
    template_name = 'learn/objects.html'
    context_object_name = 'themes'

    def get_queryset(self):
        return Object.objects.all().order_by('name')


class MaterialListView(ListView):
    template_name = 'learn/materials.html'
    context_object_name = 'materials'

    def get_queryset(self):
        self.theme = get_object_or_404(Object, pk=self.kwargs['object_id'])
        return Material.objects.filter(object=self.theme).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['theme'] = self.theme
        return context


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'learn/material.html'
    context_object_name = 'material'
    pk_url_kwarg = 'material_id'


class InfoView(ListView):
    template_name = 'learn/info.html'
    context_object_name = 'materials'

    def get_queryset(self):
        self.theme = get_object_or_404(Object, pk=self.kwargs['object_id'])

        materials = Material.objects.filter(object_id=self.theme.id)

        materials = [f"{i.name}\n##########\n\n{strip_tags(i.description)}" for i in materials]

        self.text_download = "\n@@@@@@@@@@\n\n\n".join(materials)

        return Material.objects.filter(object=self.theme).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['theme'] = self.theme
        context['text_download'] = self.text_download
        return context


class RandomView(View):
    def get(self, request, object_id=None):
        if object_id is not None:
            theme = get_object_or_404(Object.objects.prefetch_related('material_set'), pk=object_id)
            themes = [theme]
            page_title = f"Случайные материалы по теме: {theme.name}"
        else:
            themes = list(Object.objects.prefetch_related('material_set').all())
            page_title = "Случайные материалы по всем темам"

        random.shuffle(themes)
        for theme in themes:
            materials = list(theme.material_set.all())
            random.shuffle(materials)
            theme.shuffled_materials = materials

        return django.shortcuts.render(
            request,
            "learn/random.html",
            {
                "themes": themes,
                "page_title": page_title,
                "is_single_theme": object_id is not None
            }
        )
