from django.contrib import admin

# Register your models here.
from art_gallery.models import *

admin.site.register(Artists)
admin.site.register(Artwork)
admin.site.register(Customer)
admin.site.register(Groups)