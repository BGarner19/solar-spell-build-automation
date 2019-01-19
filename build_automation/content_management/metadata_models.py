import os
import csv

from django.db import models


class DB_Content(models.Model):

    # TODO: Figure out how the django DB models work

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

    def __init__(self, file_name, source, title, creators, date_created, coverage, library_version, main_folder,
                 sub_folder, subject, keywords, workareas, language, copyright_statement, rights_statement, contributors):
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
        self.copyright = copyright_statement
        self.rights_statement = rights_statement
        self.contributors = contributors


def parse_metadata_csv(csv_file):

    csv_data = csv.reader(csv_file)
    metadata = []

    # TODO: Add error checking and parsing of fields that may have multiple entries to create arrays.

    for row in csv_data:
        file_name = row[0]
        source = row[1]
        title = row[2]
        creators = row[3]
        date_created = row[4]
        coverage = row[5]
        library_version = row[6]
        main_folder = row[7]
        sub_folder = row[8]
        subject = row[9]
        keywords = row[10]
        workareas = row[11]
        language = row[12]
        copyright_statement = row[13]
        rights_statement = row[14]
        contributors = row[15]

        content_metadata = ContentMetadata(file_name, source, title, creators, date_created, coverage, library_version,
                                           main_folder, sub_folder, subject, keywords, workareas, language,
                                           copyright_statement, rights_statement, contributors)

        metadata.append(content_metadata)

    return metadata









