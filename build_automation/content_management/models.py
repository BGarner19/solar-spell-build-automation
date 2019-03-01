import os

from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


# Defines the models for the database tables
class AbstractTag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=2000, null=True)

    class Meta:
        abstract = True


class Title(AbstractTag):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('title-detail', args=[str(self.id)])

    class Meta:
        ordering = ['title']


class FileName(AbstractTag):
    fileName = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('filename-detail', args=[str(self.id)])

    class Meta:
        ordering = ['fileName']


class Description(AbstractTag):
    description = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('description-detail', args=[str(self.id)])

    class Meta:
        ordering = ['description']


class Format(AbstractTag):
    description = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('format-detail', args=[str(self.id)])

    class Meta:
        ordering = ['description']


class LibraryVersion(AbstractTag):
    version = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('version-detail', args=[str(self.id)])

    class Meta:
        ordering = ['version']


class Audience(AbstractTag):
    audience = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('audience-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['audience']


class ReadingLevel(AbstractTag):
    readingLevel = models.IntegerField()

    def get_absolute_url(self):
        return reverse('reading-level-detail', args=[str(self.id)])

    class Meta:
        ordering = ['readingLevel']


class MainSubject(AbstractTag):
    mainSubject = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('main-subject-detail', args=[str(self.id)])

    class Meta:
        ordering = ['mainSubject']


class RightsHolder(AbstractTag):
    rights = models.CharField(max_length=1000, unique=False)

    def get_absolute_url(self):
        return reverse('rights-holder-detail', args=[str(self.id)])

    class Meta:
        ordering = ['rights']


class RightsStatement(AbstractTag):
    rightsStatement = models.CharField(max_length=1000, unique=False)

    def get_absolute_url(self):
        return reverse('rights-statement-detail', args=[str(self.id)])

    class Meta:
        ordering = ['rightsStatement']


class Notes(AbstractTag):
    notes = models.CharField(max_length=2000, unique=False)

    def get_absolute_url(self):
        return reverse('notes-detail', args=[str(self.id)])

    class Meta:
        ordering = ['notes']


class Creator(AbstractTag):
    name = models.CharField(max_length=300, unique=True)

    def get_absolute_url(self):
        return reverse('creator-detail', args=[str(self.id)])

    def __str__(self):
        return "Creator[{}]".format(self.name)

    class Meta:
        ordering = ['name']


class Coverage(AbstractTag):

    def get_absolute_url(self):
        return reverse('coverage-detail', args=[str(self.id)])

    def __str__(self):
        return "Coverage[{}]".format(self.name)

    class Meta:
        ordering = ['name']


class Subject(AbstractTag): # OBSOLETE

    def get_absolute_url(self):
        return reverse('subject-detail', args=[str(self.id)])

    def __str__(self):
        return "Subject[{}]".format(self.name)

    class Meta:
        ordering = ['name']


class Keyword(AbstractTag):  # OBSOLETE

    def get_absolute_url(self):
        return reverse('keyword-detail', args=[str(self.id)])

    def __str__(self):
        return "Keyword[{}]".format(self.name)

    class Meta:
        ordering = ['name']


class Workarea(AbstractTag):  # OBSOLETE

    def get_absolute_url(self):
        return reverse('workarea-detail', args=[str(self.id)])

    def __str__(self):
        return "Workarea[{}]".format(self.name)

    class Meta:
        ordering = ['name']


class Language(AbstractTag):

    def get_absolute_url(self):
        return reverse('language-detail', args=[str(self.id)])

    def __str__(self):
        return "Language[{}]".format(self.name)

    class Meta:
        ordering = ['name']


class Cataloger(AbstractTag):

    def get_absolute_url(self):
        return reverse('cataloger-detail', args=[str(self.id)])

    def __str__(self):
        return "Cataloger[{}]".format(self.name)

    class Meta:
        ordering = ['name']


"""
This definition is similar to the existing Content table. It will be similar to that table and should eventually
take its place once all front-end code is finished tying into it. 
"""
class ContentNew(models.Model):

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

    title = models.OneToOneField(Title, on_delete=models.SET_NULL, null=True)
    original_file_name = models.CharField(FileName, max_length=100)
    description = models.OneToOneField(Description, on_delete=models.SET_NULL, null=True)
    format = models.OneToOneField(Format, on_delete=models.SET_NULL, null=True)
    library_version = models.OneToOneField(LibraryVersion, on_delete=models.SET_NULL, null=True)
    audience = models.ManyToManyField(Audience, on_delete=models.SET_NULL, null=True)
    reading_level = models.OneToOneField(ReadingLevel, on_delete=models.SET_NULL, null=True)
    main_subject = models.OneToOneField(MainSubject, on_delete=models.SET_NULL, null=True)
    rights_holder = models.OneToOneField(RightsHolder, on_delete=models.SET_NULL, null=True)
    rights_statement = models.OneToOneField(RightsStatement, on_delete=models.SET_NULL, null=True)
    notes = models.ManyToManyField(Notes, on_delete=models.SET_NULL, null=True)
    creators = models.ManyToManyField(Creator)
    coverage = models.ForeignKey(Coverage, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
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


class Content(models.Model):

    def set_original_name(self, file_name):
        self.original_file_name = file_name
        return os.path.join("contents", file_name)

    """
    A content is the representation of a file.
    """
    name = models.CharField(max_length=300)

    description = models.TextField()

    # The Actual File
    content_file = models.FileField("File", upload_to=set_original_name)

    updated_time = models.DateField(
        "Content updated on",
        help_text='Date when the content was last updated'
    )

    last_uploaded_time = models.DateTimeField(
        "Last updated on",
        editable=False,
        help_text='Date & Time when the file was uploaded'
    )

    # SHA-256 Checksum of the latest updated file.
    checksum = models.SlugField(
        "SHA256 Sum",
        max_length=65,
        editable=False,
        help_text='SHA256 Sum of the file uploaded recently.'
    )

    content_file_uploaded = False

    creators = models.ManyToManyField(Creator)
    coverage = models.ForeignKey(Coverage, on_delete=models.SET_NULL, null=True)
    subjects = models.ManyToManyField(Subject)
    keywords = models.ManyToManyField(Keyword)
    workareas = models.ManyToManyField(Workarea)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    cataloger = models.ForeignKey(Cataloger, on_delete=models.SET_NULL, null=True)
    original_file_name = models.CharField(max_length=300, null=True)
    source = models.CharField(max_length=2000, null=True)
    copyright = models.CharField(max_length=500, null=True)
    rights_statement = models.TextField(null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_file = self.content_file

    def __str__(self):
        return "Content[{}]".format(self.name)

    def get_absolute_url(self):
        return reverse('content-detail', args=[self.pk])

    class Meta:
        ordering = ['pk']


class DirectoryLayout(models.Model):

    def set_original_name(self, file_name):
        self.original_file_name = file_name
        return os.path.join("banners", "libversions", file_name)

    """
    The Directory Layout for each build.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=2000, null=True)
    banner_file = models.FileField(upload_to=set_original_name)
    original_file_name = models.CharField(max_length=200, null=True)

    banner_file_uploaded = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.existing_banner_file = self.banner_file

    def __str__(self):
        return "DirectoryLayout[{}]".format(self.name)

    class Meta:
        ordering = ['pk']


class Directory(models.Model):

    def set_original_name(self, file_name):
        self.original_file_name = file_name
        return os.path.join("banners", "folders", file_name)

    """
    Representation of the directory for each build.
    """
    name = models.CharField(max_length=100)
    dir_layout = models.ForeignKey(DirectoryLayout, related_name='directories', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='subdirectories', on_delete=models.CASCADE, null=True)
    banner_file = models.FileField(upload_to=set_original_name, null=True)
    original_file_name = models.CharField(max_length=200, null=True)
    individual_files = models.ManyToManyField(Content, related_name='individual_files')

    # Tags
    creators = models.ManyToManyField(Creator)
    coverages = models.ManyToManyField(Coverage)
    subjects = models.ManyToManyField(Subject)
    keywords = models.ManyToManyField(Keyword)
    workareas = models.ManyToManyField(Workarea)
    languages = models.ManyToManyField(Language)
    catalogers = models.ManyToManyField(Cataloger)

    # Whether All of the specificed tags should be present in the content, or atleast one is needed.
    # Represent ALL or ANY of the UI state.
    creators_need_all = models.BooleanField(default=False)
    coverages_need_all = models.BooleanField(default=False)
    subjects_need_all = models.BooleanField(default=False)
    keywords_need_all = models.BooleanField(default=False)
    workareas_need_all = models.BooleanField(default=False)
    languages_need_all = models.BooleanField(default=False)
    catalogers_need_all = models.BooleanField(default=False)

    banner_file_uploaded = False

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
