from django.contrib import admin
#from movielib.models import Video
# Register your models here.

from .models import Video

class movieAdmin(admin.ModelAdmin):
    list_display =('Video','Name','Type','Client','Project_Manager','Creation_Date','ModifiedD');


admin.site.register(Video, movieAdmin)