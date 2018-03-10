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


class PmOperaterType(models.Model):  # 操作员操作类型维度表 例如：存款，上分，登记战绩等
    type_id = models.IntegerField(null=False)
    type_name = models.IntegerField(null=False)
    inactive_time = models.DateTimeField(default='2037-01-01')


class Operator(models.Model):  # 操作员基本信息表
    operator_id = models.IntegerField(null=False)
    operator_name = models.CharField(max_length=20)
    login_id = models.CharField(max_length=20)
    password = models.CharField(max_length=80)
    club_id = models.IntegerField(null=True)
    group_id = models.IntegerField(null=True)
    developer_id = models.IntegerField(null=True)
    active_time = models.DateTimeField(default=timezone.now)
    inactive_time = models.DateTimeField(default='2037-01-01')
    permission_group = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)


class OperatorGroup(models.Model):  # 客服组表
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=20)
    club_id = models.IntegerField(null=False)
    active_time = models.DateTimeField(default=timezone.now)
    inactive_time = models.DateTimeField(default='2037-01-01')


class ClubAccount(models.Model):  # 俱乐部客服组账户表
    account_id = models.IntegerField(null=False)
    club_id = models.IntegerField(null=False)
    type_id = models.IntegerField(null=False)
    group_id = models.IntegerField(null=False)
    account_desc = models.CharField(max_length=20)
    active_time = models.DateTimeField(default=timezone.now)
    inactive_time = models.DateTimeField(default='2037-01-01')


class PmAccount(models.Model):  # 账户类型维度表(银行卡，微信，支付宝等)
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)
    inactive_time = models.DateTimeField(default='2037-01-01')

