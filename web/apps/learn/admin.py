from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from django import forms
from django.contrib import admin

from apps.learn.models import Object, Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = "__all__"
        widgets = {
            "description": WysiwygWidget(),
        }


@admin.register(Object)
class ObjectAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Material)
class MaterialAdmin(ModelAdmin):
    form = MaterialForm
    list_display = ("name", "object", "description_short",)
    list_filter = ("object",)
    search_fields = ("name", "object__name",)

    @admin.display(description="Описание")
    def description_short(self, obj):
        return obj.description[:50] + "..." if len(
            obj.description) > 50 else obj.description
