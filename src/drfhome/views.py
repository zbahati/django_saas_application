from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
  qs = PageVisit.objects.all()
  page_qs = PageVisit.objects.filter(path=request.path)
  
  try: 
    percent = (page_qs.count() * 100.0)/ qs.count()
  except:
    percent = 0

  html_template = "home.html"
  my_title = "My Page"
  my_context = {
    "page_title": my_title,
    "page_visit_count": page_qs.count(),
    "percent": percent,
    "total_visit_count": qs.count()
  }
  PageVisit.objects.create(path=request.path)

  return render(request, html_template, my_context)