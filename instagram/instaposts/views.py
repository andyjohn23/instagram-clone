from django.shortcuts import render, redirect
from .models import InstaPosts, Like
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView

def likes(request):
    qs = InstaPosts.objects.all()
    user = request.user

    context = {
        'qs':qs,
        'user': user,
    }

    return render(request, 'instaposts/post.html', context)

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = InstaPosts.objects.get(id=post_id)

        if user in post_obj.likes.all():
            post_obj.likes.remove(user)

        else:
            post_obj.likes.add(user)
    
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'like':
                like.value == 'unlike'
            else:
                like.value == 'like'

        like.save()
    return redirect('instaposts:post-list')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = InstaPosts
    fields = ['image', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)