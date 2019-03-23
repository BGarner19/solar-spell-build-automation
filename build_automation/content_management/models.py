import os

from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


# Defines the models for the database tables
class AbstractTag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=2000, null=True)

    class Meta:
        abstract = True


# Title of the content
class Title(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('title-detail', args=[str(self.id)])

    class Meta:
        ordering = ['title']


# File name of the content. Used to match with uploaded content.
class FileName(models.Model):
    fileName = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('filename-detail', args=[str(self.id)])

    class Meta:
        ordering = ['fileName']


# Creator of the content. May include authors, companies, organizations, etc.
class Creator(models.Model):
    creator = models.CharField(max_length=300, unique=True)

    def get_absolute_url(self):
        return reverse('creator-detail', args=[str(self.id)])

    def __str__(self):
        return "Creator[{}]".format(self.name)

    class Meta:
        ordering = ['creator']


# Description of the content
class Description(models.Model):
    description = models.CharField(max_length=5000, unique=True)

    def get_absolute_url(self):
        return reverse('description-detail', args=[str(self.id)])

    class Meta:
        ordering = ['description']


# Format of the piece of content. May be in formats such as mp4, pdf, mp3, or "NoFormat"
class Format(models.Model):

    format = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('format-detail', args=[str(self.id)])

    class Meta:
        ordering = ['format']


# Coverage of the content; specifically spatial coverage. Essentially the area/location that the content discusses.
class Coverage(models.Model):

    coverage = models.CharField(max_length=300, unique=True)

    def get_absolute_url(self):
        return reverse('coverage-detail', args=[str(self.id)])

    def __str__(self):
        return "Coverage[{}]".format(self.name)

    class Meta:
        ordering = ['coverage']


# The main subject of the content. Ex: Health, Math, Science, etc.
class MainSubject(models.Model):
    mainSubject = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('main-subject-detail', args=[str(self.id)])

    class Meta:
        ordering = ['mainSubject']


# Version of the library that the content belongs to.
class LibraryVersion(models.Model):
    version = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('version-detail', args=[str(self.id)])

    class Meta:
        ordering = ['version']


# Audience of the content. Ex. Students, Teachers, etc.
class Audience(models.Model):
    audience = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('audience-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['audience']


# Reading level of the content. Levels 0, 1, 2, 3.
class ReadingLevel(models.Model):
    readingLevel = models.IntegerField()

    def get_absolute_url(self):
        return reverse('reading-level-detail', args=[str(self.id)])

    class Meta:
        ordering = ['readingLevel']


# Language that the content is in.
class Language(models.Model):

    language = models.CharField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('language-detail', args=[str(self.id)])

    def __str__(self):
        return "Language[{}]".format(self.name)

    class Meta:
        ordering = ['language']


# Copyright statement or license for the content.
class Copyright(models.Model):
    copyright = models.CharField(max_length=1000, unique=False)

    def get_absolute_url(self):
        return reverse('rights-holder-detail', args=[str(self.id)])

    class Meta:
        ordering = ['rights']


# Statement of rights/licenses for the content.
class RightsStatement(models.Model):
    rightsStatement = models.CharField(max_length=1000, unique=False)

    def get_absolute_url(self):
        return reverse('rights-statement-detail', args=[str(self.id)])

    class Meta:
        ordering = ['rightsStatement']


# The person who added the content to the catalog.
class Cataloger(models.Model):

    cataloger = models.CharField(max_length=300, unique=True)

    def get_absolute_url(self):
        return reverse('cataloger-detail', args=[str(self.id)])

    def __str__(self):
        return "Cataloger[{}]".format(self.name)

    class Meta:
        ordering = ['cataloger']


# Miscellaneous notes added by the content curators.
class Notes(models.Model):
    notes = models.CharField(max_length=10000, unique=False)

    def get_absolute_url(self):
        return reverse('notes-detail', args=[str(self.id)])

    class Meta:
        ordering = ['notes']


# This definition is similar to the existing Content table. It will be similar to that table and should eventually
# take its place once all front-end code is finished tying into it.
class Content(models.Model):

    def set_original_name(self, file_name):
        return os.path.join("contents", file_name)

    # This is the file that was uploaded to the server by the librarian
    content_file = models.FileField("File", upload_to=set_original_name)

    updated_time = models.DateField(
        "Content updated on",
        help_text='Date when the piece of content was last updated by the librarian.'
    )

    last_uploaded_time = models.DateTimeField(
        "Last Updated On",
        editable=False,
        help_text='Date and Time when the file was uploaded.'
    )

    checksum = models.SlugField(
        "SHA256 CheckSum",
        max_length=65,
        editable=False,
        help_text='The SHA256 CheckSum of the uploaded file.'
    )

    content_file_uploaded = False

    # Finalized metadata fields

    title = models.TextField()
    original_file_name = models.TextField()
    description = models.TextField()
    format = models.OneToOneField(Format, on_delete=models.SET_NULL, null=True)
    library_version = models.OneToOneField(LibraryVersion, on_delete=models.SET_NULL, null=True)
    audience = models.OneToOneField(Audience, on_delete=models.SET_NULL, null=True)
    reading_level = models.OneToOneField(ReadingLevel, on_delete=models.SET_NULL, null=True)
    main_subject = models.ManyToManyField(MainSubject)
    copyright = models.TextField()
    rights_statement = models.TextField()
    notes = models.ManyToManyField(Notes)
    creators = models.ManyToManyField(Creator)
    coverage = models.ManyToManyField(Coverage)
    language = models.ManyToManyField(Language)
    cataloger = models.ForeignKey(Cataloger, on_delete=models.SET_NULL, null=True)

    def _init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_file = self.content_file

    def __str__(self):
        return "ContentNew[{}]".format(self.name)

    def get_absolute_url(self):
        return reverse('content-new-detail', args=[self.pk])

    class Meta:
        ordering = ['pk']


# The DirectoryLayout class defines the top level library versions
class DirectoryLayout(models.Model):

    def set_original_name(self, file_name):
        self.original_file_name = file_name
        return os.path.join("banners", "libversions", file_name)

    banner_file_uploaded = False

    name = models.CharField(max_length=100, unique=True) # Name of the library version
    description = models.CharField(max_length=5000, null=True) # Description of what the library version is for
    banner_file = models.FileField(upload_to=set_original_name) # Banner file location for the entire version
    original_file_name = models.CharField(max_length=500, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.existing_banner_file = self.banner_file

    def __str__(self):
        return "DirectoryLayout[{}]".format(self.name)

    class Meta:
        ordering = ['pk']


# The Directory class defines the inner folders of the library version and supports nesting through the use of parent_id
class Directory(models.Model):
    def set_original_name(self, file_name):
        self.original_file_name = file_name
        return os.path.join("banners", "folders", file_name)

    name = models.CharField(max_length=100) # Name of the inner folder
    dir_layout = models.ForeignKey(DirectoryLayout, related_name='directories', on_delete=models.CASCADE)  # Top level library version that this folder belongs in
    parent = models.ForeignKey('self', related_name='subdirectories', on_delete=models.CASCADE, null=True) # Parent folder of this folder
    banner_file = models.FileField(upload_to=set_original_name, null=True)
    original_file_name = models.CharField(max_length=200, null=True)
    individual_files = models.ManyToManyField(Content, related_name='individual_files') # Content in this folder
    banner_file_uploaded = False

    # Tags to add to this folder
    formats = models.ManyToManyField(Format)
    library_versions = models.ManyToManyField(LibraryVersion)
    audiences = models.ManyToManyField(Audience)
    reading_levels = models.ManyToManyField(ReadingLevel)
    main_subjects = models.ManyToManyField(MainSubject)
    creators = models.ManyToManyField(Creator)
    coverages = models.ManyToManyField(Coverage)
    languages = models.ManyToManyField(Language)
    catalogers = models.ManyToManyField(Cataloger)

    # The following lines define whether ALL of the provided tags should be present in this folder of content. UI side,
    # the user defines whether they want "ANY" or "ALL" of the input metadata to be filtered into this folder. These
    # are the only filterable metadata options.
    formats_need_all = models.BooleanField(default=False)
    library_versions_need_all = models.BooleanField(default=False)
    audiences_needs_all = models.BooleanField(default=False)
    reading_levels_need_all = models.BooleanField(default=False)
    main_subjects_need_all = models.BooleanField(default=False)
    creators_need_all = models.BooleanField(default=False)
    coverages_need_all = models.BooleanField(default=False)
    languages_need_all = models.BooleanField(default=False)
    catalogers_need_all = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.existing_banner_file = self.banner_file

    def __str__(self):
        return "Directory[{}]".format(self.name)

    class Meta:
        ordering = ['pk']


class Build(models.Model):
    """
    Representation of the build of library version. Only one record will be present, since we need to have only the
    latest build.
    """

    class TaskState:
        RUNNING = 1
        FINISHED = 2

    class BuildCompletionState:
        SUCCESS = 1
        FAILURE = 2

    TASK_STATES = (
        (TaskState.RUNNING, 'Running'),
        (TaskState.FINISHED, 'Finished'),
    )

    BUILD_COMPLETION_STATES = (
        (BuildCompletionState.SUCCESS, 'Success'),
        (BuildCompletionState.FAILURE, 'Failure'),
    )

    task_state = models.IntegerField(choices=TASK_STATES)
    build_file = models.CharField(max_length=400, null=True)
    dir_layout = models.ForeignKey(DirectoryLayout, on_delete=models.SET_NULL, null=True)
    completion_state = models.IntegerField(choices=BUILD_COMPLETION_STATES, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)

    class Meta:
        ordering = ['pk']
