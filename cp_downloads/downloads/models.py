from django.db import models

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name

class Downloads(models.Model):
    application = models.ForeignKey("Application", on_delete=models.CASCADE, null=True)
    location = models.URLField(max_length=512)
    version = models.DecimalField(decimal_places=3, max_digits=3)
    release_date = models.DateTimeField(null=True)
    release_notes = models.TextField(null=True)
    is_available_for_download = models.BooleanField(default=False)
    def __str__(self):
        return self.application


#add columns for downloads to be viewed
