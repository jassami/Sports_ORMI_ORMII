from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count
from . import team_maker

def index(request):
	context = {
		"all_leagues": League.objects.all(),
		'all_teams': Team.objects.all(),
		"all_players": Player.objects.all(),
		'all_baseball_leagues': League.objects.filter(sport= "Baseball"),
		"all_women_leagues": League.objects.filter(name__contains='Womens'),
		"type_of_hockey": League.objects.filter(sport__contains='hockey'),
		"not_football_leagues": League.objects.exclude(sport__contains= 'football'),
		"leagues_called_conferences": League.objects.filter(name__contains="conference"),
		"leagues_Atlantic_region": League.objects.filter(name__contains= "Atlantic"),
		"teams_in_dallas": Team.objects.filter(location__contains= "Dallas"),
		"teams_named_Raptors": Team.objects.filter(team_name__contains= "Raptors"),
		"teams_includes_city": Team.objects.filter(location__contains= "City"),
		"teams_with_t": Team.objects.filter(team_name__contains= "T"),
		"teams_ordered_location": Team.objects.all().order_by('location'),
		"teams_ordered_name_reverse": Team.objects.all().order_by("-team_name"),
		"player_last_name_Cooper": Player.objects.filter(last_name= "Cooper"),
		"Players_first_name_Joshua": Player.objects.filter(first_name= "Joshua"),
		"last_cooper_first_not_joshue": Player.objects.filter(last_name= "Cooper").exclude(first_name= "Joshua"),
		"first_name_Alexander_or_Wyatt": Player.objects.filter(Q(first_name= "Alexander") | Q(first_name= "Wyatt")),
		"teams_Atlantic_Conference": League.objects.get(name__contains="Atlantic Soccer Conference").teams.all(),
		"players_Boston_Penguins": Team.objects.get(team_name = "Penguins").curr_players.all(),
		"teams_Int_Col_Bball_Conf": League.objects.get(id=2).teams.all(),
		"American_Conf_Amateur_lastname_Lopez": League.objects.get(name="American Conference of Amateur Football").teams.all(),
		"all_football_players": League.objects.filter(sport= "Football"),
		"player_with_Sophia": Player.objects.filter(first_name= "Sophia"),
		"question_8": Player.objects.filter(last_name= "Flores").exclude(curr_team= Team.objects.filter(Q(team_name= "Roughriders") & Q(location= "Washington"))[0]),
		"players_with_Flores": Player.objects.filter(last_name= "Flores"),
		"Samuel_Evans": Player.objects.get(first_name= "Samuel", last_name="Evans"),
		"players_Manitoba_TigerCats": Player.objects.filter(all_teams= Team.objects.get(team_name= "Tiger-Cats", location= "Manitoba")),
		"Manitoba_TigerCats": Team.objects.get(team_name= "Tiger-Cats", location= "Manitoba"),
		"players_formerly_Wichita_Vikings": Player.objects.filter(all_teams= Team.objects.get(team_name= "Vikings", location= "Wichita")).exclude(curr_team= Team.objects.get(team_name= "Vikings", location= "Wichita")),
		"JacobGray_before_OregonColts": Team.objects.exclude(team_name= "Colts", location= "Oregon"),
		"Joshua_AtlantFed_Baseball": Player.objects.filter(first_name= "Joshua"),
		"all_teams_12players": Team.objects.all().annotate(player_num= Count("all_players")),
		"player_team_count": Player.objects.all().annotate(team_num= Count("all_teams")).order_by("-team_num"),
	}
	print(Team.objects.filter(Q(team_name= "Roughriders") & Q(location= "Washington"))[0])
	print(Team.objects.get(team_name= "Vikings", location= "Wichita"))
	print(Player.objects.filter(first_name= "Joshua").count())
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")

