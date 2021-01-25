from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    date = models.DateField()
    website_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    project_language = models.CharField(max_length=1, blank=True)
    html = models.BooleanField(default=False)
    html = models.BooleanField(default=False)
    css = models.BooleanField(default=False)
    javascript = models.BooleanField(default=False)
    python = models.BooleanField(default=False)
    django = models.BooleanField(default=False)

    def __str__(self):
        return self.title
