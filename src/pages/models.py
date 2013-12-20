from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Page(models.Model):
    word = models.CharField(max_length=200)
    definition = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.word
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def as_html(self):
        for d in definition:
            defintion += mark_safe("<a href='{}'>{}</a>".format(escape(d),escape(d)))
        return mark_safe(definition)
    
    def page_list(self):
        return ", ".join([page.name for page in self.pages.all()])
    page_list.short_description = "Pages"
    
    def get_absolute_url(self):
        return reverse('pages:detail', args=(self.id,))

        
