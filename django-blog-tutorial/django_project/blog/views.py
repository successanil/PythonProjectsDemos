from django.shortcuts import render

posts = [
    {
        'author':'Anil',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'Sep 11,2019'
    },
    {
        'author':'Anil2',
        'title':'Blog Post 2',
        'content':'First post content',
        'date_posted':'Sep 11,2019'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    context = {
        'title':'about dynamic'
    }

    return render(request, 'blog/about.html',context)


