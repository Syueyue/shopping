from django.db import models
from ta_user.models import User
from ta_goods.models import GoodInfo
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey('ta_user.User',None)
    goods=models.ForeignKey('ta_goods.GoodInfo',None)
    count=models.IntegerField(default=0)
