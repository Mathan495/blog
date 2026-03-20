from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post,Aboutus
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForms

# static demo data
# posts = [
#         {'id': 1, 'title': 'Post1', 'content': 'Content of post1'},
#         {'id': 2, 'title': 'Post2', 'content': 'Content of post2'},
#         {'id': 3, 'title': 'Post3', 'content': 'Content of post3'},
#         {'id': 4, 'title': 'Post4', 'content': 'Content of post4'}
#     ]

# Create your views here.
def index(request):
    blog_title = "Latest Posts"

    # getting data from post model
    all_posts = Post.objects.all()

    # paginate 
    paginator = Paginator(all_posts, 5) 
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)

    return render(request, 'index.html', {'blog_title': blog_title, 'page_obj': page_obj})  

def details(request, slug):
    # ststic data
    # post = next((item for item in posts if item['id'] == post_id), None) 

    # getting data from models by post id and handling error for post not in db 
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post Does not Exist")

    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post is {post}') 
    return render(request, 'detail.html', {'post' : post,'related_posts':related_posts})   

def old_url(request):
    return redirect(reverse('blog:new_url_page'))

def new_url(request):
    return HttpResponse("this is the new url page") 

def contact_view(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f'POST data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}') 
            success_msg = "your Email has been sent"
            # send email or save in database
            return render(request, 'contact.html',{'form':form, 'success_msg':success_msg}) 
        else:
            logger.debug('Form validation failure')
        return render(request, 'contact.html', {'form': form, 'name':name, 'email':email, 'message':message})
    return render(request, 'contact.html') 

def about_view(request):
    about_content = Aboutus.objects.first().content
    return render(request, 'about.html',{'about_content':about_content})