from django.contrib import admin
from .models import MainWikiModel, RelatedWikiModel
# Register your models here.

admin.site.register(MainWikiModel)
admin.site.register(RelatedWikiModel)