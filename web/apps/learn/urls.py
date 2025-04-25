import django.urls

import apps.learn.views

app_name = "learn"
urlpatterns = [
    django.urls.path('', apps.learn.views.ThemeListView.as_view(), name='objects'),
    django.urls.path('theme/<int:object_id>/', apps.learn.views.MaterialListView.as_view(), name='materials'),
    django.urls.path('material/<int:material_id>/', apps.learn.views.MaterialDetailView.as_view(), name='material'),
    django.urls.path('info/<int:object_id>/', apps.learn.views.InfoView.as_view(), name='info'),
    django.urls.path('random/<int:object_id>/', apps.learn.views.RandomView.as_view(), name='random'),
]