from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class IndexPage(TemplateView):
    def get(self,request,**kwargs):
        article_data =[]
        all_article = Article.objects.all().order_by('-created_at')[:9]
        for article in all_article:
            article_data.append({
                'title':article.title,
                'cover':article.cover.url,
                'category':article.category.title,
                'created_at':article.created_at.date(),
            })

        promote_data=[]
        all_promote_article = Article.objects.filter(promote=True)
        for promote_article in all_promote_article:
            promote_data.append({
                'category':promote_article.category.title,
                'title':promote_article.title,
                'author':promote_article.author.user.first_name+ " "+promote_article.author.user.last_name,
                'created_at':promote_article.created_at.date(),
                'cover':promote_article.cover.url if promote_article.cover else None,
                'avatar':promote_article.author.avatar.url if promote_article.author.avatar else None,
            })

        context = {
            'article_data':article_data,
            'promote_article_data':promote_data,
        }

        return render(request,'index.html',context)

class ContactPage(TemplateView):
    template_name = 'page-contact.html'

class AboutUs(TemplateView):
    template_name = 'page-about.html'