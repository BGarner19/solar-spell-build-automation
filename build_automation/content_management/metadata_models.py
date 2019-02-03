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

    def __str__(self):
        return "Content Metadata Object: \n" + "File Name: " + self.file_name + "\nSource: " + self.source + \
               "\nTitle: " + self.title + "\nCreators: " + str(self.creators) + "\nDate Created: " + self.date_created + \
                "\nCoverage: " + self.coverage + "\nLibrary Version: " + self.library_version + "\nMain Folder: " + \
                self.main_folder + "\nSub Folder: " + self.sub_folder + "\nSubject: " + str(self.subject) + "\nKeywords: " + \
                str(self.keywords) + "\nWork Areas: " + str(self.workareas) + "\nLanguage: " + str(self.language) + "\nCopyright: " + \
                self.copyright + "\nRights Statement: " + self.rights_statement + "\nContributors: " + str(self.contributors)


def parse_metadata_csv(csv_file):

    with open(csv_file) as csvfile:
        csv_data = csv.reader(csvfile)
        metadata = []

        # TODO: Add error checking and parsing of fields that may have multiple entries to create arrays.

        for row in csv_data:
            file_name = row[0]
            source = row[1]
            title = row[2]
            creators = grab_multiple_items_to_array(row[3])
            date_created = row[4]
            coverage = row[5]
            library_version = row[6]
            main_folder = row[7]
            sub_folder = row[8]
            subject = grab_multiple_items_to_array(row[9])
            keywords = grab_multiple_items_to_array(row[10])
            workareas = grab_multiple_items_to_array(row[11])
            language = grab_multiple_items_to_array(row[12])
            copyright_statement = row[13]
            rights_statement = row[14]
            contributors = grab_multiple_items_to_array(row[15])

            content_metadata = ContentMetadata(file_name, source, title, creators, date_created, coverage, library_version,
                                               main_folder, sub_folder, subject, keywords, workareas, language,
                                               copyright_statement, rights_statement, contributors)

            metadata.append(content_metadata)

            for content in metadata:
                print(content)

        return metadata


def grab_multiple_items_to_array(line):

    items = line.split("|")

    return items







