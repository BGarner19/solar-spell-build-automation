import os
import csv

from django.db import models


# class DB_Content(models.Model):
#
#     # TODO: Figure out how the django DB models work
#
#     file_name = models.CharField(max_length=300)
#     source = models.TextField()
#     title = models.TextField()
#     creators = models.ManyToManyField(Creator)
#     date_created = models.TextField()
#     coverage = models.ForeignKey(Coverage)
#     library_version = models.TextField()
#     main_folder = models.TextField()
#     sub_folder = models.TextField()
#     subject = models.ManyToManyField(Subject)
#     keywords = models.ManyToManyField(Keyword)
#     workareas = models.ManyToManyField(Workarea)
#     language = models.ForeignKey(Language)
#     copyright = models.TextField()
#     rights_statement = models.TextField()
#     contributors = models.ManyToManyField(Contributor)


class ContentMetadata(object):

    def __init__(self, title, file_name, creators, date_created, description, format_type, library_version, audience,
                 reading_level, coverage, language, main_subject, rights_holder, rights_statement, catalogers, notes):
        self.file_name = file_name
        self.title = title
        self.creators = creators
        self.date_created = date_created
        self.description = description
        self.format_type = format_type
        self.library_version = library_version
        self.audience = audience
        self.reading_level = reading_level
        self.coverage = coverage
        self.language = language
        self.main_subject = main_subject
        self.rights_holder = rights_holder
        self.rights_statement = rights_statement
        self.catalogers = catalogers
        self.notes = notes

    def __str__(self):

        return "Content Metadata Object: \n" + "File Name: " + self.file_name + "\nTitle: " + self.title + \
               "\nCreators: " + str(self.creators) + "\nDate Created: " + self.date_created + "\nDescription: " + \
               "\nFormat Type: " + self.format_type + "\nLibrary Version: " + self.library_version + "\nAudience: " + \
                self.audience + "\nReading Level: " + self.reading_level + "\nCoverage: " + self.coverage + \
               "\nLanguage: " + str(self.language) + "\nMain Subject: " + self.main_subject + "\nRights Holder: " + \
               self.rights_holder + "\nRights Statement: " + self.rights_statement + "\nCatalogers: " + \
               str(self.catalogers) + "\nNotes: " + self.notes


def parse_metadata_csv(csv_file):

    with open(csv_file) as csvfile:
        csv_data = csv.reader(csvfile)
        metadataArray = []

        for row in csv_data:
            file_name = row[0]
            title = row[1]
            creators = grab_multiple_items_to_array(row[2])
            date_created = row[3]
            description = row[4]
            format_type = row[5]
            library_version = row[6]
            audience = row[7]
            reading_level = row[8]
            coverage = row[9]
            language = grab_multiple_items_to_array(row[10])
            main_subject = row[11]
            rights_holder = row[12]
            rights_statement = row[13]
            catalogers = grab_multiple_items_to_array(row[14])
            notes = grab_multiple_items_to_array(row[15])

            content_metadata = ContentMetadata(file_name, title, creators, date_created, description, format_type,
                                               library_version, audience, reading_level, coverage, language,
                                               main_subject, rights_holder, rights_statement, catalogers, notes)

            metadataArray.append(content_metadata)

            for content in metadataArray:
                print(content)

        return metadataArray


def grab_multiple_items_to_array(line):

    items = line.split("|")

    items = [s.strip() for s in items]

    return items







