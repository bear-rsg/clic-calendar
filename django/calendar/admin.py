from django.contrib import admin
from . import models

admin.site.site_header = 'CLiC Calendar: Admin Dashboard'


def approve_answer(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to approved
    """
    queryset.update(admin_approved=True)


approve_answer.short_description = "Approve selected answers (will appear on main site)"


def disapprove_answer(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not approved
    """
    queryset.update(admin_approved=False)


disapprove_answer.short_description = "Disapprove selected answers (will not appear on main site)"


class AnswerAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of Answers in the Django admin
    """
    list_display = ('answer_text',
                    'question',
                    'admin_approved',
                    'meta_created_datetime',
                    'meta_lastupdated_datetime')
    list_filter = ('question', 'admin_approved')
    list_per_page = 30
    ordering = ('-id',)
    actions = (approve_answer, disapprove_answer)


def publish_question(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to published
    """
    queryset.update(admin_published=True)


publish_question.short_description = "Publish selected questions (will appear on main site)"


def unpublish_question(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not published
    """
    queryset.update(admin_published=False)


unpublish_question.short_description = "Unpublish selected questions (will not appear on main site)"


class QuestionAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of Questions in the Django admin
    """
    list_display = ('question_text',
                    'question_image',
                    'year',
                    'month',
                    'admin_published',
                    'meta_created_datetime',
                    'meta_lastupdated_datetime')
    list_filter = ('year', 'month', 'admin_published')
    list_per_page = 30
    ordering = ('-id',)
    actions = (publish_question, unpublish_question)


class YearAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of Year in the Django admin
    """
    list_display = ('name',)
    list_per_page = 30
    ordering = ('name',)


class MonthAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of Year in the Django admin
    """
    list_display = ('name', 'name_short', 'number')
    list_per_page = 30
    ordering = ('number',)


# Register
admin.site.register(models.Answer, AnswerAdminView)
admin.site.register(models.Question, QuestionAdminView)
admin.site.register(models.Year, YearAdminView)
admin.site.register(models.Month, MonthAdminView)
