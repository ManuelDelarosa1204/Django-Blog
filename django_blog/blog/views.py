from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostCreationForm, CommentCreationForm
from user.models import User


class Index(ListView):
    """View to display posts on the index page"""

    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"

    queryset = Post.objects.filter(status=Post.Status.PUBLIC)


class CreatePost(CreateView):
    """View to create post"""

    model = Post
    template_name = "blog/create-post.html"
    form_class = PostCreationForm

    def get_success_url(self) -> str:
        return reverse_lazy("user:profile", args=[self.request.user.slug])

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetail(DetailView):
    """
    View to display posts

    This is used as the `GET` view for ReadPost.
    """

    model = Post
    template_name = "blog/read-post.html"
    context_object_name = "posts"

    def get_context_data(self, *args, **kwargs):
        """
        Get the form for comment creation and
        get the comments that the comments that
        go with the post.
        """

        # Get the post object that is being viewed
        post = Post.objects.get(slug=self.kwargs["slug"])

        context = super().get_context_data(*args, **kwargs)
        context["form"] = CommentCreationForm
        context["comments"] = Comment.objects.filter(post=post)
        return context


class PostComment(CreateView):
    """
    View used to create post comments.

    This is used  `POST` view for ReadPost.
    """

    model = Comment
    template_name = "blog/read-post.html"
    form_class = CommentCreationForm

    def get_success_url(self) -> str:
        return reverse_lazy(
            "blog:post", args=[self.request.user.username, self.kwargs["slug"]]
        )

    def form_valid(self, form):
        post = Post.objects.get(slug=self.kwargs["slug"])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.form = self.get_form()
        return super().post(request, *args, **kwargs)


class ReadPost(View):
    def get(self, request, *args, **kwargs):
        view = PostDetail.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)
