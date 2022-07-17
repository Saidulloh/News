from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=140)
    image = models.ImageField(blank=True, null=True)
    url = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"


class Tag(models.Model):
    title = models.CharField(
        max_length = 100,
    )

    def __str__(self): 
        return self.title

    class Meta:
        verbose_name_plural = "Теги"


class News(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        null = True,
        blank = True
        )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="news/", blank=True, null=True)
    description = RichTextUploadingField()
    url = models.SlugField(null=True, unique=True)
    tags = models.ManyToManyField(
        Tag,
        null = True,
        blank = True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Новости"
        ordering = ['-id']


class SocialSidebar(models.Model):
    social_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    link_address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    icon = models.ImageField( 
        upload_to = 'news/',
        blank=True,
        null=True,
    )
    background = models.CharField(max_length=8)

    class Meta:
        verbose_name_plural = "Социальные сети"


class Contacts_us(models.Model):
    our_office = models.CharField(
        max_length = 255,
        blank = True,
        null = True
        )
    email_us = models.EmailField(
        max_length = 255,
        unique = True,
        blank = False
        )
    call_us = models.IntegerField(
        blank = True,
        null = True,
        )

    class Meta:
        verbose_name_plural = "Контакты" 


class Comment(models.Model):
    post = models.ForeignKey(
        News,
        on_delete=models.CASCADE
        )
    user_name = models.CharField(
        max_length=80
        )
    comm = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return f'{self.comm}'
    
    class Meta:
        verbose_name_plural = "Комментарии" 