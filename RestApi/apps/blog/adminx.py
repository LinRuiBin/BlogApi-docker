import xadmin
from .models import Label, Artilcle, HomeData

class LabelAdmin(object):
    list_display = ["name"]

class ArtilcleAdmin(object):
    list_display = ["title", "add_time", "is_origin", "label", "art_type","is_home"]
    search_fields = ['title']
    list_editable = ["is_origin", "is_home"]
    list_filter = ["title",  "label", "art_type"]

class HomeDataAdmin(object):
    list_display = ["name"]


xadmin.site.register(Artilcle, ArtilcleAdmin)
xadmin.site.register(Label, LabelAdmin)
xadmin.site.register(HomeData, HomeDataAdmin)