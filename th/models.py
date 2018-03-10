from django.db import models
import django.utils.timezone as timezone
# Create your models here.


class User(models.Model):  # 用户信息表
    user_id = models.IntegerField(null=False)
    user_name = models.CharField(max_length=20)
    game_user_id = models.IntegerField(null=False)
    active_time = models.DateTimeField(default=timezone.now)
    inactive_time = models.DateTimeField(default='2037-01-01')


class GameUser(models.Model):  # 游戏平台用户信息
    game_user_id = models.IntegerField(null=False)
    user_name = models.CharField(max_length=20)
    active_time = models.DateTimeField(default=timezone.now)
    inactive_time = models.DateTimeField(default='2037-01-01')


class Club(models.Model):  # 俱乐部基础信息
    club_id = models.IntegerField(null=False)
    game_club_id = models.IntegerField(null=False)
    club_level = models.IntegerField(null=False)
    club_name = models.CharField(max_length=20)
    club_short_name = models.CharField(max_length=4)
    water_rate = models.IntegerField(null=False)
    insurance_rate = models.IntegerField(null=False)
    active_time = models.DateTimeField(default=timezone.now)
    inactive_time = models.DateTimeField(default='2037-01-01')


class UserId(models.Model):  # 生成系统ID
    user_id = models.AutoField(primary_key=True)
    game_user_id = models.IntegerField(null=False)
    active_time = models.DateTimeField(default=timezone.now)
    inactive_time = models.DateTimeField(default='2037-01-01')


class AccountId(models.Model):  # 生成系统account_id
    account_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=False)
    active_time = models.DateTimeField(default=timezone.now)
    inactive_time = models.DateTimeField(default='2037-01-01')


class ClubId(models.Model):  # 生成系统club_id
    club_id = models.AutoField(primary_key=True)
    game_club_id = models.IntegerField(null=False)
    club_name = models.CharField(max_length=20)
    active_time = models.DateTimeField(default=timezone.now)
    inactive_time = models.DateTimeField(default='2037-01-01')


class ClubUser(models.Model):  # 系统俱乐部与玩家关系表
    club_id = models.IntegerField(null=False)
    user_id = models.IntegerField(null=False)
    account_id = models.IntegerField(null=False)
    remark = models.CharField(max_length=20)
    note = models.CharField(max_length=100)
    active_time = models.DateTimeField(default=timezone.now)
    inactive_time = models.DateTimeField(default='2037-01-01')