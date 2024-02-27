from django.contrib import admin
from .models import Nodes
from .models import Edges
# Register your models here.
admin.site.register(Nodes)
admin.site.register(Edges)