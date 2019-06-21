from django.db import models

# Create your models here.


type_choice=(
    ('Film','Film'),
    ('Game','Game'),
)

class Video(models.Model):

    Video = models.FileField(null=True, verbose_name="")
    Name = models.CharField(max_length=200)
    Type = models.CharField(max_length=100, choices=type_choice)
    Client = models.CharField(max_length=200)
    Project_Manager = models.CharField(max_length=200)
    Creation_Date = models.DateTimeField(auto_now_add=True, blank=True)
    ModifiedD = models.DateTimeField(auto_now=True)
    #updated_at = models.DateTimeField(True, True, editable=False)

    def __str__(self):
        return self.Name + ": " + str(self.Video)

    def delete(self, *args, **kwargs):
        self.Video.delete()
        super().delete(*args, **kwargs)

