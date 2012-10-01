from django.db import models


from polymorphic import PolymorphicModel


class Entry(PolymorphicModel):
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

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
