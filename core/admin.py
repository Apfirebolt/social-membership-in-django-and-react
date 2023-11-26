from django.contrib import admin
from .models import UserGroups, Message, GroupMembers


admin.site.register(UserGroups)
admin.site.register(Message)
admin.site.register(GroupMembers)

