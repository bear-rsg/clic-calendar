from django.db import models
from django.core.mail import send_mail
from django.conf import settings


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

    class Meta:
        unique_together = ('year', 'month')
        ordering = ['-year', '-month__number', '-month__order']


class Answer(models.Model):
    """
    The answer that a user submits in response to a question
    """

    answer_text = models.TextField()
    # Foreign key fields
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.PROTECT)
    # Admin fields
    admin_approved = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True, null=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return str(self.answer_text)[0:40]

    def save(self, *args, **kwargs):
        """
        When a new model is saved email the research team
        """

        # Check if this is a new answer
        if self.meta_created_datetime is None:
            # Send email alert to research team
            try:
                send_mail('CLiC Calendar: New Answer',
                          'There has been a new answer submitted to CLiC Calendar.',
                          settings.DEFAULT_FROM_EMAIL,
                          [settings.NOTIFICATION_EMAIL],
                          fail_silently=False)
            except Exception as e:
                print(e)
            
        # Save new object
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-meta_created_datetime']
