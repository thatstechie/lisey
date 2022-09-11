from django.shortcuts import render
from core.models import Post
from django.core.paginator import Paginator, EmptyPage

def home(request):
   posts=Post.objects.all()[::-1]
   paginator=Paginator(posts,3)
   page=1
   try:
      posts=paginator.page(page)
   except EmptyPage:
      posts=paginator.page(paginator.num_pages)

   return render(request, 'lisey/index.html', {'lisey': posts})


def about(request):
   return render(request, "lisey/message.html")

def mission(request):
   return render(request, "lisey/mission.html")

def edusys(request):
   return render(request, "lisey/edusys.html")

def associations(request):
   return render(request, "lisey/associations.html")

def clubs(request):
   return render(request, "lisey/clubs.html")

def achievements(request):
   return render(request, "lisey/achievements.html")

def alumni2022(request):
   return render(request, "lisey/alumni2022.html")



def news(request, page=1):
   posts=Post.objects.filter(is_active=True, is_contest=True)[::-1]
   paginator=Paginator(posts,3)
   try:
      posts=paginator.page(page)
   except EmptyPage:
      posts=paginator.page(paginator.num_pages)

   return render(request, 'lisey/news.html', {'posts': posts})


def contests(request, page=1):
   posts=Post.objects.filter(is_active=True, is_contest=True)[::-1]
   paginator=Paginator(posts,12)
   try:
      posts=paginator.page(page)
   except EmptyPage:
      posts=paginator.page(paginator.num_pages)

   return render(request, 'lisey/contests.html', {'posts': posts})

def events(request, page=1):
   posts=Post.objects.filter(is_active=True, is_contest=True)[::-1]
   paginator=Paginator(posts,12)
   try:
      posts=paginator.page(page)
   except EmptyPage:
      posts=paginator.page(paginator.num_pages)

   return render(request, 'lisey/events.html', {'posts': posts})



def news_details(request, slug):
    lisey=Post.objects.get(slug=slug)
    return render(request, "lisey/news_details.html", {
        "lisey": lisey
    })

