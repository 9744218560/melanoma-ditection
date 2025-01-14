from django.contrib import admin

from skinapp.models import LoginTable, UserTable
from skinapp.models import Complaints, Feedback, Detectiondata

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(UserTable)
admin.site.register(Complaints)
admin.site.register(Feedback)
admin.site.register(Detectiondata)
