from django.db import models

class UserStates(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    game = models.CharField(max_length=100, blank=True)
    crawltime = models.CharField(max_length=50)
    userurl = models.CharField(max_length=150)

    class Meta:
        db_table = 'UserStates'

class BcNews(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()
    newsurl = models.CharField(max_length=150)

    class Meta:
        db_table = 'BcNews'
