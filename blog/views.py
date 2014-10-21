from django.views.generic import ListView, DetailView
from .models import Blog


class BlogListView(ListView):
    model = Blog
    context_object_name = "blog"
    template_name = "blog/article-list.html"

    def get_queryset(self):
        queryset = super(BlogListView, self).get_queryset()
        tag = self.request.GET.get('tag', None)
        if tag:
            queryset = queryset.filter(tags__tag=tag)
        return queryset


class BlogYearListView(BlogListView):

    def get_queryset(self):
        return super(BlogYearListView, self).get_queryset().filter(date__year=self.kwargs['year'])


class BlogMonthListView(BlogListView):

    def get_queryset(self):
        return super(BlogMonthListView, self).get_queryset().filter(
            date__year=self.kwargs['year'],
            date__month=self.kwargs['month'],
        )


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = "blog"
    template_name = "blog/article-detail.html"
