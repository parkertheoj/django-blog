from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     # template = loader.get_template('blogging/list.html')
#     context = {'posts': posts}
#     # body = template.render(context)
#     return render(request, 'blogging/list.html', context)

class BlogListView(ListView):
    model = Post
    template_name = 'blogging/list.html'
    context_object_name = 'post_list'
    queryset = Post.objects.order_by('-created_date')
    #if i add in .filter(published_date=True) it tells me published_date
    #isnt defined and im not sure why.

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    def blog(self, request, *args, **kwargs):
        post = self.get_object()
        context = {'post': post}
        return render(request, "blogging/detail.html", context)

# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)
