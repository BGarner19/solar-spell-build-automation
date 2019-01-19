import os

from django.db import models


class DB_Content(models.Model):

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


class ContentMetadata(object):

    def __init__(self, file_name, source, title, creators, date_created, coverage, library_version, main_folder, sub_folder, subject, keywords, workareas, language, copyright, rights_statement, contributors):
        self.file_name = file_name
        self.source = source
        self.title = title
        self.creators = creators
        self.date_created = date_created
        self.coverage = coverage
        self.library_version = library_version
        self.main_folder = main_folder
        self.sub_folder = sub_folder
        self.subject = subject
        self.keywords = keywords
        self.workareas = workareas
        self.language = language
        self.copyright = copyright
        self.rights_statement = rights_statement
        self.contributors = contributors








