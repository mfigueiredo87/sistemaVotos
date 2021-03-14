from django.contrib import admin

from .models import Question, Choice

#change the site title admin
admin.site.site_header = "Gestor Votos Admin"
admin.site.site_title = "Gestor de Votos Admin Area"
admin.site.index_title = "Bem vindo ao Gestor Votos - Admin"


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]
    
# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)
