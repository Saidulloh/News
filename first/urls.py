from django.contrib import admin
from django.urls import path, include
from news.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', HomeListView.as_view(), name="homepage"),
    path('category/', CategoryListView.as_view(), name="show_category"),
    path('category_id/<int:cat_id>', CategoryIdListView.as_view(), name="show_category_id"),
    path('post/<int:post_id>', PostDetailView.as_view(), name = 'post'),
    path('tags_id/<int:tag_id>', TagsIdListView.as_view(), name = 'show_tags_id'),
    path('contact_us/', ContactsFormView.as_view(), name = 'contact_us'),
    path('add_new/', NewsCreateView.as_view(), name = 'create_new'),
    path('update_new/<int:id>', update_news, name = 'update_news'),
    path('delete_new/<int:id>', delete_news, name = 'delete_news')
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 