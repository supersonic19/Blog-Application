from django.shortcuts import render,get_object_or_404
from main import models

# Create your views here.

def index(request):
    # Minus is written so that it is sorted in descending order
    latest_articles = models.Article.objects.all().order_by('-createdAt')[:10]  # Limits the no of articles to 10

    context = {
        'latest_articles' : latest_articles
    }

    return render(request,'main/index.html',context)

def article(request,pk):
    #article = models.Article.objects.get(pk = pk)

    article = get_object_or_404(models.Article,pk = pk)   #404 is the page not found error

    context = {
        'article' : article
    }
    return render(request, 'main/article.html',context )

def author(request,pk):
    
    author = get_object_or_404(models.Author,pk = pk)

    context = {
        'author' : author
    }
    return render(request , 'main/author.html' , context)

def create_article(request):
    authors = models.Author.objects.all()

    context = {
        "authors" : authors
    }    

    if request.method == "POST":

        article_data = {
            "title" : request.POST['title'],
            "content" : request.POST['content']
        }
        article = models.Article.objects.create(**article_data)
        author = models.Author.objects.filter(pk = request.POST['author'])
        article.Authors.set(author)

        context['success'] = True
        
    return render(request , 'main/create_article.html' , context)