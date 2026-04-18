from django.contrib import admin
# ✅ Updated imports
from .models import Course, Lesson, Instructor, Learner, Enrollment, Question, Choice, Submission


# Inline for Lesson (already correct)
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# ✅ NEW: Choice inline inside Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


# ✅ NEW: Question inline inside Course
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


# Course admin (UPDATED to include QuestionInline)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]  # 👈 added QuestionInline
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Lesson admin (unchanged)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# ✅ NEW: Question admin with choices inside it
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# ✅ Register everything
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
