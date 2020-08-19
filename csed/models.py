from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Subject(models.Model):
    sub_name = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('publish_date')
    def __str__(self):
        return self.sub_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days= 1)
class Video(models.Model):
    subject = models.ForeignKey(Subject,on_delete = models.CASCADE)
    video_link = models.CharField(max_length=200)
    video_date = models.DateTimeField(default = timezone.now())
    def __str__(self):
        return self.video_link
    def was_recorded_recently(self):
        return self.video_date>= timezone.now() - date.timedelta(days = 1)

