from .models import Article
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = 'index.html'
    model = Article
    ordering = ['-create_time']
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(status=0)


class DetailView_(DetailView):
    model = Article
    template_name = 'detail.html'