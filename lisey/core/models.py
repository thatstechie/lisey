from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from froala_editor.fields import FroalaField

class Post(models.Model):
    title=models.CharField(max_length=120, verbose_name="Başlığı")
    content= FroalaField(verbose_name="Məzmun")
    image=models.ImageField(upload_to="post")
    is_active=models.BooleanField(default=False, verbose_name="Bu post paylaşılsın ?")
    is_new=models.BooleanField(default=False, verbose_name="Bu xəbərdir ?")
    is_contest=models.BooleanField(default=False, verbose_name="Bu müsabiqədir ?")
    is_event=models.BooleanField(default=False, verbose_name="Bu tədbirdir ?")
    created_at= models.DateField(auto_now=False, auto_now_add=False, verbose_name="Paylaşılma tarixi")
    slug=models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return  f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug= slugify(self.title)
        super().save(*args, **kwargs)