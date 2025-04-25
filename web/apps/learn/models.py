import django.db.models


class Object(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name="название",
        max_length=150,
        null=False,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = 'тема'
        verbose_name_plural = 'темы'

    def __str__(self):
        return self.name


class Material(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name="название",
        max_length=150,
        null=False,
    )
    description = django.db.models.CharField(
        verbose_name="описание",
        max_length=150,
        null=False,
    )
    object = django.db.models.ForeignKey(
        Object,
        verbose_name="тема",
        on_delete=django.db.models.CASCADE,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'

    def __str__(self):
        return self.name
