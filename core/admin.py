from django.contrib import admin
from .models import UserGroups, Message, GroupMembers, Plot, PlotImages


admin.site.register(UserGroups)
admin.site.register(Message)
admin.site.register(GroupMembers)
admin.site.register(Plot)
admin.site.register(PlotImages)


