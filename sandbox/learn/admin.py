from django.contrib import admin

# Register your models here.
from .models import Question, Answer
admin.site.register(Answer)

class ChoiceInLine(admin.TabularInline):
    model = Answer
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['query_text', 'q_date', 'asked_recent']
    list_filter = ['q_date']
    search_fields = ['query_text']
    fieldsets = [
        (None, {'fields': ['query_text']}),
        ('Date Information', {'fields': ['q_date'], 'classes' : ['collapse']}),
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)