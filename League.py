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
from Fantasy import *
import pandas as pd
import numpy as np


if __name__ == '__main__':
    #To Authenticate
    # sc = OAuth2(None, None, from_file='oauth2.json')
    # league = yfa.league.League(sc,'406.l.774934')

    # QBFreeAgents = GetFreeAgents(league, "QB")
    # with open("QBFreeAgentSample.json", "w") as file:
    #     file.write(json.dumps(QBFreeAgents, indent= 4))

    # RBFreeAgents = GetFreeAgents(league, "RB")
    # with open("RBFreeAgentSample.json", "w") as file:
    #     file.write(json.dumps(RBFreeAgents, indent= 4))

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
    #pprint(playerInfo, indent=4)

    # #Getting info for taken players
    # takenPlayers = league.taken_players()
    # tpList = []
    # for tp in takenPlayers:
    #     if tp['position_type'] == 'O':
    #         tpList.append(tp['player_id'])

    # # ##Getting stat information
    # reqType = 'season'
    # stats = league.player_stats(player_ids=tpList, req_type=reqType)
    # #Dumping this in a local file in order to not query Yahoo every single time
    # with open ("currentstats.json", "w") as file:
    #     file.write(json.dumps(stats))

    #Loading the local data into pandas
    with open ("currentstats.json", "r") as file:    
        df = pd.DataFrame(json.loads(file.read()))

    #print(df[['name', 'Rush Yds', 'Rush TD']].sort_values(by=['Rush Yds'], ascending=False).head(20))
    #print(df.columns)
    df['percentCatch'] = (df['Rec']/df['Targets'])
    df['YdsPerCatch'] = np.divide(df['Rec Yds'],df['Rec'])
    df = df[df['Targets'] >=20]
    df = df[df['percentCatch'] >=0.6]
    print(df[['name', 'Rec', 'Rec Yds','Targets', 'percentCatch','YdsPerCatch']].sort_values(by=['YdsPerCatch'], ascending=False).head(20))
    
    #print(len(tpList))

    # playerID = playerInfo[0]["player_id"]
    # #Who has him?
    # #pprint(league.ownership([playerID]))



    # #Getting league settings
    # leagueSettings = league.settings()
    # pprint(leagueSettings, indent=4)

    #Getting league standings
    # leagueStandings = league.standings()
    # pprint(leagueStandings, indent=4)

    # # #Getting league transactions
    # transactions = league.transactions('drop',count=1)
    # with open ("lasttransaction.json", "w") as file:
    #     file.write(json.dumps(transactions, indent=4))
    # #pprint(transactions, indent=4)

    # # #Getting players in waivers
    # dudesInWaiver = league.waivers()
    # with open ("waivers.json", "w") as file:
    #     file.write(json.dumps(dudesInWaiver, indent=4))


    ##Team information, to find your teamID
    #pprint (league.teams())
    #
#     teamID = league.team_key()
#     team = yfa.team.Team(sc, teamID)
#     #pprint(team)

# #     # ##Dude to add information
# #     playerAdd = "Josh Gordon"
# #     playerInfo = league.player_details(playerAdd)
# #     playerAddID = playerInfo[0]["player_id"]

# #    # ##Dude to drop information
# #     playerDrop = "Van Jefferson Jr."
# #     playerInfo = league.player_details(playerDrop)
# #     playerDropID = playerInfo[0]["player_id"]

# #     print (playerAddID, playerDropID)

#     #team.add_and_drop_players(playerAddID, playerDropID)
#     # playerID = playerInfo[0]["player_id"]


#     #My team
#     with open("myteam.json", "w") as file:
#         file.write(json.dumps(team.roster(week=5), indent= 4))

