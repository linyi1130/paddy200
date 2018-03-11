from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from th.models import *
from th.mainFunctions import *
import json
import django.core.serializers.json


def test(request):
    user_id=147
    result=poker_get_user_club_id(user_id)
    return HttpResponse(result)


def login(request):
    return render(request, 'login.html')


def sidebar_init(request):  # 边栏初始化

    return render(request,'sidebar_templete.html')


def usercash(request):  # 用户存取款加载页
    web_name = '积分充值'
    club_id=1000
    group_id=1
    tb_user = func_dropdown_userinfo(club_id)
    tb_type_list = ClubAccount.objects.filter(inactive_time='2037-01-01').filter(group_id=group_id).filter(
        club_id=club_id).values('account_id', 'account_desc')
    return render(request,'usercash.html', {'web_name': web_name,'tb_user': tb_user,'tb_type_list': tb_type_list})


def registerclub(request):
    club_name = '很厉害的俱乐部'
    club_level = 1
    club_shortname = '厉害'
    water_rate = 100
    insurance_rate = 100
    game_club_id=func_get_clubid(club_name)
    if game_club_id:
        result = func_register_club(club_name, game_club_id, club_level, club_shortname, water_rate, insurance_rate)
    return HttpResponse(result)


def clubuserinit(request):
    game_club_id='868'
    result = func_clubuser_init(game_club_id)
    result = str(result)
    return HttpResponse(result)


def operator(request):  # 操作员管理界面

    return render(request,'manage/operator_manage.html')


def operator_setup(request):  # 新增操作员

    return render(request, 'manage/group_setup.html')


def operator_group_setup(request):

    return render(request, 'manage/group_setup.html')


def add_operator_group(request):  # 新增客服组
    group_name=request.POST['group_name']
    club_id = 1000
    group_id = func_add_group(group_name, club_id)
    if group_id:
        cnt = 1
        while cnt <= 3:
            account_id = func_create_club_account_id(club_id)
            account_type = PmAccount.objects.filter(inactive_time='2037-01-01').get(type_id=cnt).type_name
            if func_create_club_account(account_id, club_id, cnt, group_id, account_type):
                cnt = cnt + 1
    else:
        return HttpResponse('False')
    return HttpResponse('True')


def operator_group_subs_list(request):  # 客服组列表
    club_id=1000
    try:
        group_list=OperatorGroup.objects.filter(inactive_time='2037-01-01').filter(club_id=club_id).values('group_name')
    except Exception as e:
        return False
    return render(request,'manage/group_subs_list.html',{'group_list': group_list})


def operater_setup(request):  # 操作员新增加载页

    return render(request, 'manage/operator_setup.html')


def add_operator(request):  # 新增操作员
    operator_name = request.POST['operator_name']
    login_id = request.POST['login_id']
    club_id=1000
    permission_group=106
    result = func_add_operator(operator_name, login_id, club_id, permission_group, None)
    return HttpResponse(result)


def operator_subs_list(request):  # 操作员列表
    club_id=1000
    try:
        operator_list=Operator.objects.filter(inactive_time='2037-01-01').filter(club_id=club_id)\
            .values('operator_name', 'login_id')
    except Exception as e:
        return False
    return render(request, 'manage/operator_subs_list.html', {'operator_list': operator_list})


def operator_relation(request):  # 操作员关系加载页
    club_id=1000
    tb_group_list = OperatorGroup.objects.filter(inactive_time='2037-01-01').filter(club_id=club_id)
    tb_operator_list = Operator.objects.filter(inactive_time='2037-01-01').filter(club_id=club_id).filter(group_id=None)
    return render(request, 'manage/operator_relation.html', {'tb_group_list': tb_group_list,
                                                             'tb_operator_list': tb_operator_list})


def operator_relation_setup(request):  # 操作员关系绑定
    operator_id_list = request.POST['operator_id']
    group_id = request.POST['group_id']
    operator_id = operator_id_list.split(",")
    for t in operator_id:
        if t != '':
            if not func_operation_relation(t, group_id):
                return HttpResponse('False')
    return HttpResponse('True')


def user(request):  # 新增用户加载页
    web_name = '玩家注册'
    club_name = '很厉害的俱乐部'
    return render(request, 'user.html', {'web_name': web_name, 'club_name': club_name})


def register_user(request):
    club_id = 1000
    user_name = request.POST['user_name']
    remark = request.POST['remark']
    note = request.POST['note']
    feedback = request.POST['feedback']
    feedback = int(float(feedback) * 10000)
    feedback_type = request.POST['feedback_type']
    if func_register_club_user(user_name, club_id, remark, note):
        if feedback != 0:
            user_id=func_get_user_id_by_user_name(user_name)
            func_user_feedback_reg(user_id, club_id, feedback, feedback_type)
    else:
        return HttpResponse('False')
    return HttpResponse('True')


def user_subs_list(request):
    club_id=1000
    tb_result=func_get_userlist_by_clubid(club_id)
    return render(request, 'user_list.html',{'tb_user': tb_result})


def user_account_info(request):
    club_id = 1000
    club_name = '很厉害的俱乐部'
    user_id = request.POST['user_id']
    account_id = request.POST['account_id']
    user_name = request.POST['user_name']

    master_account = func_user_master_accountinfo(club_id,account_id)
    balance_info = func_user_account_info(club_id, user_id, account_id)
    user_note= func_user_note(club_id,user_id)
    tb_result = {'user_name':user_name, 'master_account': master_account, 'club_name': club_name}
    return render(request, 'user_account_info.html', {'tb_result': tb_result, 'blance_info': balance_info, 'user_note': user_note})


def group_subs_list(request):  # 客服组账户余额列表
    club_id = 1000
    group_id = 1
    group_name = '1号'
    tb_result = func_club_subs_accountlist(club_id, group_id)
    return render(request,'group_subs_list.html', {'tb_result': tb_result, 'group_name': group_name})


def user_balance_cash(request):
    club_id=1000
    group_id = 1
    operator_id = 3000
    user_id = request.POST['user_id']
    account_id = func_get_account_by_userid(user_id, club_id)
    pay_account_id = request.POST['pay_account_id']
    chance_num = request.POST['change_num']
    type_id = request.POST['type_id']
    note = request.POST['note']
    chance_num = int(float(chance_num)*10000)
    type_id = int(type_id)
    serial_no = func_create_serial_no(club_id, operator_id)
    if func_user_cash(account_id, user_id, club_id, type_id, operator_id, chance_num, note, serial_no):
        if func_club_cash(pay_account_id, club_id, type_id, operator_id, chance_num, group_id, note, serial_no):
            return HttpResponse('True')
        else:
            return HttpResponse('False')


def check_cash_balance(request):
    club_id=1000
    group_id = 1
    operator_id = 3000
    user_id = request.POST['user_id']
    account_id = func_get_account_by_userid(user_id, club_id)
    pay_account_id = request.POST['pay_account_id']
    chance_num = request.POST['change_num']
    chance_num = int(float(chance_num)*10000)
    flag1 = func_user_balance_check(club_id, account_id, chance_num)
    flag2 = func_club_balance_check(pay_account_id, chance_num)
    if flag1 & flag2:
        return HttpResponse('True')
    else:
        return HttpResponse('False')


def user_subs_balance_list(request):
    club_id = 1000
    user_id = request.POST['user_id']
    account_id = func_get_account_by_userid(user_id, club_id)
    tb_result = func_user_balance_subs_list(club_id, account_id)
    return render(request, 'user_subs_balance_list.html', {'tb_balance_list': tb_result})


def user_result_min_list(request):
    club_id=1000
    club_name='很厉害的俱乐部'
    user_id = request.POST['user_id']
    user_name = request.POST['user_name']
    account_id = func_get_account_by_userid(user_id, club_id)
    tb_balance_list = func_user_balance_subs_list(club_id, account_id)
    return render(request, 'user_result_min_list.html',{'tb_balance_list': tb_balance_list,'club_name': club_name,'user_name':user_name})