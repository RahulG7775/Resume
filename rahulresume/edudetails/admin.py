from django.contrib import admin
from .models import Edudetails

# Register your models here.
class EdudetailsAdmin(admin.ModelAdmin):
    list_display=('Education','College','Year_of_Passing','University','Marks',)
admin.site.register(Edudetails, EdudetailsAdmin)

