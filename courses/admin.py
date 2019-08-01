from django.contrib import admin

from .models import Course, Lesson

# OPTION 1 - generic

# admin.site.register(Course)
# admin.site.register(Lesson)

# OPTION 2 - displaying course


# class CourseAdmin(admin.ModelAdmin):
#     # add_form to override fields (optional)
#     fields = (
#         'slug',
#         'title',
#         'description',
#         'allowed_memberships',
#     )

# OPTION 3


class InLineLesson(admin.TabularInline):  # Tabular or Stacked
    model = Lesson
    extra = 1  # to change the stacked lesson form from 3 to 1
    max_num = 3  # to limit the number of extras


class CourseAdmin(admin.ModelAdmin):
    inlines = [InLineLesson]  # from InLineLesson class to combine course and lessons on the same form
    list_display = ('title', 'slug', 'description', 'combine_title_and_slug')# you can change what is shown on the list in the django-admin
    list_display_links = ('combine_title_and_slug', )  # create links in the Django Admin
    list_editable = ('slug', )  # edit straight in the list
    list_filter = ('title', 'slug')
    search_fields = ('title', 'slug')
    fieldsets = (
        (None, {
            'fields': (
                'slug',
                'title',
                'description',
                'allowed_memberships',
            )
        }),
    )
    # method on the ModelAdmin class to be referenced in the list_display

    def combine_title_and_slug(self, obj):
        return "{}-{}".format(obj.title, obj.slug)


admin.site.register(Course, CourseAdmin)