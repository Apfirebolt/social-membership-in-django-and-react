from django.contrib import admin
from accounts.models import CustomUser, UserStats


admin.site.register(CustomUser)
admin.site.register(UserStats)

