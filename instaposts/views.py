from django.shortcuts import render, redirect
from .models import InstaPosts, Like
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from itertools import chain

def likes(request):
    qs = InstaPosts.objects.all()
    user = request.user

    context = {
        'qs':qs,
        'user': user,
    }

    return render(request, 'instausers/instauser-details.html', context)

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
        self.object = form.save(commit=False)
        form.instance.author = self.request.user
        form.instance.object_relation_assume = self.request.user.profile
        self.object.save()
        return super().form_valid(form)

def followers_post(request):
    profile = Profile.objects.get(user=request.user)
    users = [user for user in profile.followers.all()]

    posts = []
    qs = None

    for follower in users:
        p = Profile.objects.get(user=follower)
        p_posts = p.instaposts_set.all()
        posts.append(p_posts)

    my_post = profile.profile_instaposts
    posts.append(my_post)

    if len(posts)>0:
        qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
    return render(request, 'instausers/profile.html', {'posts': qs})