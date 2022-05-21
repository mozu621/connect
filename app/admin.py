from django.contrib import admin
from django.utils.translation import gettext as _
from . import models


admin.site.register(models.Profile)
admin.site.register(models.Portfolio)
admin.site.register(models.Like)
admin.site.register(models.Comment)
admin.site.register(models.Tag)

