from django.contrib import admin
from testapp.models import Rubric, Article
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

# admin.site.register(Rubric, MPTTModelAdmin)
admin.site.register(
    Rubric, 
    DraggableMPTTAdmin, 
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)


admin.site.register(Article)
