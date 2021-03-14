from django.db import models
from smtplib import SMTP

NOTIFY_EMAIL = 'something@lists.bham.ac.uk'
NOTIFY_EMAIL_FROM = 'bear-software@contacts.bham.ac.uk'
LAST_EMAIL = None
EMAIL_MIN_TIME = timedelta(hours=1)

def email_notify():
   if LAST_EMAIL is not None and datetime.now() - LAST_EMAIL < EMAIL_MIN_TIME:
       return
   msg = "There are new things to look at"
   server = SMTP(settings.SOMETHINGOROTHER)
   server.set_debuglevel(1)
   server.sendmail(NOTIFY_EMAIL_FROM, NOTIFY_EMAIL, msg)
   server.quit()
   global LAST_EMAIL
   LAST_EMAIL = datetime.now()


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
       # 1. check if new
           # 2. email_notify()
       super().save(*args, **kwargs)

    class Meta:
        ordering = ['-meta_created_datetime']
