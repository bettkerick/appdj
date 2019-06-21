
from .models import Video
from django import forms
from django.contrib.auth.forms import UserChangeForm

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["Video", "Name","Type","Client","Project_Manager"]


class videoeditForm(UserChangeForm):
    class Meta:
        model= Video
        fields= ["Video", "Name","Type","Client","Project_Manager"]
