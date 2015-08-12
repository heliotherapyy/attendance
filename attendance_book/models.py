from django.db import models

# Create your models here.

class Attendance(models.Model):
    name = models.CharField(max_length=50)
    attended_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name
