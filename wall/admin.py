from django.contrib import admin

from models import Article
from models import Image
from models import Entry
from models import Embed
from models import Link


admin.site.register(Article)
admin.site.register(Image)
admin.site.register(Entry)
admin.site.register(Embed)
admin.site.register(Link)
