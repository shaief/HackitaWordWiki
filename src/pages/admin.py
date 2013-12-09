from django.contrib import admin

from pages.models import Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('word','definition','pub_date')
	list_filter = ['pub_date']
	search_fields = ['word']


admin.site.register(Page, PageAdmin)