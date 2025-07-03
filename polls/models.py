from django.db import models



class questions(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=50,default="")
    option2 = models.CharField(max_length=50,default="")
    option3 = models.CharField(max_length=50,default="")
    option1_count = models.IntegerField(default=0)
    option2_count = models.IntegerField(default=0)
    option3_count = models.IntegerField(default=0)
