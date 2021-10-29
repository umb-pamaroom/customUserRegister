from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Memoモデルを作成する
class Memo(models.Model):

    # user_memo = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE,default=0 )

    # 日付
    dateData = models.DateField(default=timezone.now, blank=True)

    # 新しい発見
    discovery = models.TextField(blank=True)

    # 新しい発見
    tired = models.TextField(blank=True)

    # 新しい発見
    dislike = models.TextField(blank=True)

    # 新しい発見
    happy = models.TextField(blank=True)

    # 新しい発見
    best = models.TextField(blank=True)

    # 新しい発見
    tomorrow = models.TextField(blank=True)

    # 新しい発見
    other = models.TextField(blank=True)

    # 新しい発見
    summarize = models.TextField(blank=True)

    breakfast = models.ImageField(upload_to='images/breakfast/%Y/%m/%d/%s/', blank=True, null=True)

    # 朝食名
    breakfastName = models.CharField(max_length=30, blank=True)

    breakfastEvaluation = models.IntegerField(blank=True, default='0')

    lunch = models.ImageField(upload_to='images/lunch/%Y/%m/%d/%s/', blank=True, null=True)

    lunchName = models.CharField(max_length=30, blank=True)

    lunchEvaluation = models.IntegerField(blank=True, default='0')

    dinner = models.ImageField(upload_to='images/dinner/%Y/%m/%d/%s/', blank=True, null=True)

    dinnerName = models.CharField(max_length=30, blank=True)

    dinnerEvaluation = models.IntegerField(blank=True, default='0')

    snack = models.ImageField(upload_to='images/snack/%Y/%m/%d/%s/', blank=True, null=True)

    snackName = models.CharField(max_length=30, blank=True)

    snackEvaluation = models.IntegerField(blank=True, default='0')

    mealComment = models.TextField(blank=True)

    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    
