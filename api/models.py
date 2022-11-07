from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    category = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField()
    demo = models.CharField(max_length=255, null=True, blank=True)
    thumbnail = models.ImageField(
        upload_to="thumbnail/images", null=True, blank=True
    )

    def __str__(self):
        return self.title
