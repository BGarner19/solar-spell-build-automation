import os

from django.db import models

class Content(models.Model):

    file_name = models.CharField(max_length=300)
    source = models.TextField()
    title = models.TextField()
    creators = models.ManyToManyField(Creator)
    date_created = models.TextField()
    coverage = models.ForeignKey(Coverage)
    library_version = models.TextField()
    main_folder = models.TextField()
    sub_folder = models.TextField()
    subject = models.ManyToManyField(Subject)
    keywords = models.ManyToManyField(Keyword)
    workareas = models.ManyToManyField(Workarea)
    language = models.ForeignKey(Language)
    copyright = models.TextField()
    rights_statement = models.TextField()
    contributors = models.ManyToManyField(Contributor)




