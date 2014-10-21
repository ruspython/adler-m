from django.views.generic import DetailView, View, CreateView, DeleteView, UpdateView
from .models import Collection, CollectionItem, UploadedCollectionItem
from .forms import UploadCollectionItemForm
from catalog.models import Item
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse


class CollectionDetailView(DetailView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collection/detail.html'


class MyCollectionView(CollectionDetailView):
    template_name = 'collection/my.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(MyCollectionView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        collection, created = Collection.objects.get_or_create(user=self.request.user)
        return collection


class Add2Collection(View):

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        active_collection, created = Collection.objects.get_or_create(user=user)
        try:
            catalog_product = Item.objects.get(pk=kwargs['pk'])
            CollectionItem.objects.get_or_create(
                collection=active_collection,
                catalog_product=catalog_product
            )
        except Item.DoesNotExist:
            pass
        return redirect('collection:my')


class CreateCollectionItemView(CreateView):
    form_class = UploadCollectionItemForm
    template_name = 'collection/create_collection_item.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(CreateCollectionItemView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('collection:my')

    def form_valid(self, form):
        instance = form.save(commit=False)
        active_collection, created = Collection.objects.get_or_create(user=self.request.user)
        instance.collection = active_collection
        instance.save()
        return redirect(self.get_success_url())


class UpdateCollectionItemView(UpdateView):
    form_class = UploadCollectionItemForm
    template_name = 'collection/update_collection_item.html'
    model = UploadedCollectionItem

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateCollectionItemView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('collection:my')


class DeleteItem(DeleteView):
    model = CollectionItem
    template_name = 'collection/delete_collection_item.html'
    context_object_name = 'item'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteItem, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('collection:my')


class DeleteUploadedItem(DeleteView):
    model = UploadedCollectionItem
    template_name = 'collection/delete_collection_item.html'
    context_object_name = 'item'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteUploadedItem, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('collection:my')