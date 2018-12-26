from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_time'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_time']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'votes']


admin.site.register(Question, QuestionAdmin)    # 顺序不可颠倒
admin.site.register(Choice, ChoiceAdmin)
# admin.site.register((Question, Choice))
# admin.site.register(Question, Choice)是不合法的
