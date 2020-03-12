from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . models import Post
from django.contrib.auth.decorators import login_required
from . forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from datetime import datetime



# Create your views here.


@login_required(login_url="/login/")
def postviews(request):
    chat = Post.objects.all().order_by('-created_on')
    paginator = Paginator(chat, 2) #show 10 employee lists per page

    page = request.GET.get('page')
    chat = paginator.get_page(page)
    if request.method == 'POST':
        posted = PostForm(request.POST)
        if posted.is_valid():
            instance = posted.save(commit=False)
            user = request.user
            instance.user = user
            instance.save()
            messages.success(request,'publication successfully sent',extra_tags = 'alert alert-success alert-dismissible show')
            return redirect('postcreate')
        messages.error(request,'failed to send publication',extra_tags = 'alert alert-warning alert-dismissible show')
    else:
        posted = PostForm()
    return render(request, "post_views.html" ,{'chat':chat,'posted':posted})




# def postdetail(request, id):
#     obj = get_object_or_404(Post, id=id)
#     com = obj.comments.all()
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             post = request.POST.get('post')
#             post_instance = Post.objects.get(id = post)
#             new_comment.post = post_instance
#             user = request.user
#             new_comment.user = user
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#     return render(request, "post_detail.html",{'obj':obj,'com':com,'comment_form':comment_form})

def postdetail(request, id):
    obj = get_object_or_404(Post, id=id)
    com = obj.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            #datas = form.cleaned_data
            #content = datas["body"]
            new_comment = comment_form.save(commit=False)
            
            new_comment.post = obj
            user = request.user
            new_comment.user = user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, "post_detail.html",{'obj':obj,'com':com,'comment_form':comment_form})




    