from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from th.models import *
from th.mainFunctions import *


def test(request):
    list_user_id=poker_get_club_player_all('777777')
    result=poker_get_user_name_list(list_user_id)
    return HttpResponse(result)


def registerclub(request):
    club_name = '已查封'
    club_level = 1
    club_shortname = '查封'
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
