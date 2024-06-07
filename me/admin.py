from django.contrib import admin
from .models import Education, Interest, ME, ProgrammingLanguage, Technologies


# Register your models here.
class EducationStackedInlineAdmin(admin.StackedInline):
    model = Education
    extra = 1


class InterestStackedInlineAdmin(admin.StackedInline):
    model = Interest
    extra = 1


class ProgrammingLanguageStackedInlineAdmin(admin.StackedInline):
    model = ProgrammingLanguage
    extra = 1


class TechnologiesStackedInlineAdmin(admin.StackedInline):
    model = Technologies
    extra = 1


class MEAdmin(admin.ModelAdmin):
    inlines = [
        EducationStackedInlineAdmin,
        InterestStackedInlineAdmin,
        ProgrammingLanguageStackedInlineAdmin,
        TechnologiesStackedInlineAdmin,
    ]


admin.site.register(ME, MEAdmin)
