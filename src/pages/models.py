from django.db import models

# Create your models here.
class Page(models.Model):
    word = models.CharField(max_length=200)
    definition = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.word
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

