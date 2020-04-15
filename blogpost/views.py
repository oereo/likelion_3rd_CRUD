from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .models import Comment
#from .forms import CommentForm

# Create your views here.

def home(request):
    blogs = Blog.objects #쿼리셋 개념 알아야됨!! 꼭꼭
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details' : details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #쿼리셋 메소드
    return redirect('/blog/'+str(blog.id)) # redirect와 render의 차이점 알려주기!!

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'edit.html', {'blog' : blog})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    #blog = Blog.objects.filter(id = blog_id)
    blog.delete()
    return redirect('home')

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #쿼리셋 메소드
    return redirect('home')


    #Comment

def make_comment(request, blog_id):
    if request.method == 'POST':
        #comments = Comment.objects.filter(Entry=current_entry).order_by('created')
        comment = Comment()
        comment.text = request.POST['text']
        comment.created_date = timezone.datetime.now()
        comment.blog = Blog.objects.get(pk = blog_id)
        comment.save()
        return redirect('/blog/'+str(comment.blog.id))
        #return render(request, 'detail.html', {'comment.blog' : comment.blog})
    else :
        return redirect('home')


def delete_comment(request, blog_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('detail', blog_id)

# def makecomment(request, blog_id):
#     blog = get_object_or_404(Blog, pk=blog_id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.blog = blog
#             comment.save()
#             return redirect('detail', pk=blog_id)
#     else:
#         form = CommentForm()
#     return render(request, 'detail.html', {'form': form, 'blog' : blog})