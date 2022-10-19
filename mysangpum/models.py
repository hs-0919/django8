from django.db import models

# Create your models here. 기존 원격db와 같이 사용할 때 하는법, 이미 있는것을 가져올때
class Sangdata(models.Model):
    code = models.IntegerField(primary_key=True)
    sang = models.CharField(max_length=20, blank=True, null=True)
    su = models.IntegerField(blank=True, null=True)
    dan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sangdata'
        




