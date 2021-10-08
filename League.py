#!/usr/bin/env python3

'''
author: Joel Benitez - joelbenitez90@gmail.com
https://github.com/joelbenitez


This is a work in progress that will contact the Yahoo! Fantasy API and gather info 
to potentially help us get a competitive advantage (hopefully)

Useful links at:
https://developer.yahoo.com/fantasysports/guide/                                #Intro Docs
https://yahoo-fantasy-api.readthedocs.io/_/downloads/en/latest/pdf/             #API Docs
https://github.com/spilchen/yahoo_fantasy_api                                   #Dude that figured this before me
https://github.com/bbenbenek/nfl-fantasy-football                               #Another dude that figured it out


'''


import yahoo_fantasy_api as yfa
from yahoo_oauth import OAuth2
from pprint import pprint
import requests
import json
from requests.structures import CaseInsensitiveDict


def GetCurrentweek(league):
    week = league.current_week()
    return week

def GetFreeAgents(league, position = None):
    freeAgents = league.free_agents(position)
    return freeAgents


if __name__ == '__main__':
    sc = OAuth2(None, None, from_file='oauth2.json')
    league = yfa.league.League(sc,'406.l.774934')

    #print (vars(league))


    # #Getting Free Agent information per position
    # FAs = GetFreeAgents(league, "QB")
    # y = []
    # for fa in FAs:
    #     if fa['percent_owned'] >= 10:
    #         y.append(fa)

    # FAs = GetFreeAgents(league, "RB")
    # y = []
    # for fa in FAs:
    #     if fa['percent_owned'] >= 10:
    #         y.append(fa)

    # FAs = GetFreeAgents(league, "WR")
    # y = []
    # for fa in FAs:
    #     if fa['percent_owned'] >= 10:
    #         y.append(fa)

    # FAs = GetFreeAgents(league, "K")
    # y = []
    # for fa in FAs:
    #     if fa['percent_owned'] >= 10:
    #         y.append(fa)

    # ##Getting matchups for the week
    # matchupsWeek = league.matchups()
    # #pprint(matchupsWeek, indent=2)
    # with open ("matchups.json", "w") as file:
    #     file.write(json.dumps(matchupsWeek, indent=4))

    # ##Getting position information
    # positions = league.positions()
    # with open ("positions.json", "w") as file:
    #     file.write(json.dumps(positions, indent=4))


    # ##Getting player information
    # playerName = "Stefon Diggs"
    # playerInfo = league.player_details(playerName)
    # #pprint(playerInfo, indent=4)

    # playerID = playerInfo[0]["player_id"]
    #Who has him?
    #pprint(league.ownership([playerID]))

    # ##Getting stat information
    # playerIds = [playerID]
    # reqType = 'season'
    # stats = league.player_stats(player_ids=playerIds, req_type=reqType)
    # pprint(stats, indent=4)

    # #Getting league settings
    # leagueSettings = league.settings()
    # pprint(leagueSettings, indent=4)

    # #Getting league standings
    # leagueStandings = league.standings()
    # pprint(leagueStandings, indent=4)

    # #Getting league transactions
    transactions = league.transactions('drop',count=1)
    with open ("lasttransaction.json", "w") as file:
        file.write(json.dumps(transactions, indent=4))
    #pprint(transactions, indent=4)

    # #Getting players in waivers
    dudesInWaiver = league.waivers()
    with open ("waivers.json", "w") as file:
        file.write(json.dumps(dudesInWaiver, indent=4))


    ##Team information, to find your teamID
    #pprint (league.teams())
    teamID = 'YourTeamID'
    team = yfa.team.Team(sc, teamID)
#     pprint(team)

#     # ##Dude to add information
#     playerAdd = "Josh Gordon"
#     playerInfo = league.player_details(playerAdd)
#     playerAddID = playerInfo[0]["player_id"]

#    # ##Dude to drop information
#     playerDrop = "Van Jefferson Jr."
#     playerInfo = league.player_details(playerDrop)
#     playerDropID = playerInfo[0]["player_id"]

#     print (playerAddID, playerDropID)

    #team.add_and_drop_players(playerAddID, playerDropID)
    # playerID = playerInfo[0]["player_id"]


    #My team
    with open("myteam.json", "w") as file:
        file.write(json.dumps(team.roster(week=5), indent= 4))
    #pprint(team.roster(week=5))

    #print(y)

