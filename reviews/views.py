from django.views.generic import ListView, CreateView
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.core.urlresolvers import reverse


class ReviewListView(ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'reviews/reviews.html'

    def get_template_names(self):
        request = self.request
        if request.is_ajax():
            return 'reviews/review_page.html'
        else:
            return 'reviews/reviews.html'

    def get_queryset(self):
        return super(ReviewListView, self).get_queryset()


class ReviewCreateView(CreateView):
    form_class = ReviewForm
    template_name = 'reviews/create_review.html'

    def get_success_url(self):
        return reverse('reviews:review_add_success')


class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'reviews/create_comment.html'

    def get_success_url(self):
        return reverse('reviews:comment_add_success')

    def get_initial(self):
        return {'review': self.kwargs['pk']}

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['review'] = Review.objects.get(pk=self.kwargs['pk'])
        return context