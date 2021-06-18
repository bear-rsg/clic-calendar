from django.db import models
from django.core.mail import send_mail
from django.conf import settings
import logging
import re

logger = logging.getLogger(__name__)


def make_urls_clickable(text):
    """
    Find all urls in the provided text and add suitable html <a> tag to make them 'clickable' on the website
    """
    # If a valid string with content
    if type(text) == str and text != '':
        # Regex to find all urls in the provided text
        urls = re.findall(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', text)  # NOQA
        # Loop through all urls found
        for url in urls:
            # Filter out URLs that are already links
            if True:
                # Add necessary HTML to convert link into <a>
                text = text.replace(url[0], '<a href="{0}">{0}</a>'.format(url[0]))

    return text


class Year(models.Model):
    """
    Each year that's available for the system
    """

    name = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Month(models.Model):
    """
    Each month from January to December
    """

    name = models.CharField(max_length=15)
    name_short = models.CharField(max_length=3)
    number = models.IntegerField()
    order = models.IntegerField(default=1, help_text='Descending order (higher to lower)')

    def __str__(self):
        return self.name


class Question(models.Model):
    """
    The question that a researcher poses to the users
    """

    question_text = models.TextField()
    question_image = models.ImageField(upload_to='researchdata-questions-images', blank=True, null=True)
    # Foreign key fields
    year = models.ForeignKey(Year, on_delete=models.PROTECT)
    month = models.ForeignKey(Month, on_delete=models.PROTECT)
    # Admin fields
    admin_published = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True, null=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return "{} {} - {}".format(self.month, self.year, str(self.question_text)[0:40])

    def save(self, *args, **kwargs):
        """
        When a new model is saved:
        - make links in question_text clickable <a> tags
        """

        # Convert links to clickable <a> tags in question_text
        self.question_text = make_urls_clickable(self.question_text)

        # Save new object
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('year', 'month')
        ordering = ['-year', '-month__number', '-month__order']


class Answer(models.Model):
    """
    The answer that a user submits in response to a question
    """

    answer_text = models.TextField()
    name = models.CharField(blank=True, max_length=255)
    # Foreign key fields
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.PROTECT)
    # Admin fields
    admin_approved = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True, null=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.answer_text if len(self.answer_text) < 100 else (f'${self.answer_text[:97]}...')

    def save(self, *args, **kwargs):
        """
        When a new model is saved:
        - email the research team
        - make links in answer_text clickable <a> tags
        """

        # Check if this is a new answer
        if self.meta_created_datetime is None:
            # Send email alert to research team
            try:
                send_mail('CLiC Calendar: New Answer',
                          'There has been a new answer submitted to CLiC Calendar.',
                          settings.DEFAULT_FROM_EMAIL,
                          settings.NOTIFICATION_EMAIL,
                          fail_silently=False)
            except Exception:
                logger.exception("Failed to send email")

        # Convert links to clickable <a> tags in answer_text
        self.answer_text = make_urls_clickable(self.answer_text)

        # Save new object
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-meta_created_datetime']
