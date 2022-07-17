from news.models import *
import datetime
from django import template


def show_social(request):
    social = SocialSidebar.objects.all()
    tags_all = Tag.objects.all()
    categories_all = Category.objects.all()
    context = {
        'tags_all':tags_all,
        'categories_all':categories_all,
        'social' : social,
    }
    return context
