from django.db import models
from django.db.models.signals import post_save

from polymorphic.models import PolymorphicModel

from tasks import render


class Entry(PolymorphicModel):

    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    html = models.TextField()

    def __unicode__(self):
        return self.title


class Article(Entry):
    body = models.TextField()
    modfied_at = models.DateTimeField(auto_now=True)


class Image(Entry):
    original_file = models.ImageField(upload_to='images/')


class Link(Entry):
    url = models.URLField()


class Embed(Link):
    embed = models.TextField()


def post_save_render(sender, **kwargs):
    if isinstance(sender, Entry):
        render.delay(sender)


post_save.connect(post_save_render)
