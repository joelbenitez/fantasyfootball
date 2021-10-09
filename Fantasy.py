class Player:
    def __init__(self,record):
        self.id = record.player_id
        self.name = record.name
        self.position = record.eligible_positions
        self.percentowned = record.percent_owned


def GetCurrentweek(league):
    week = league.current_week()
    return week

def GetFreeAgents(league, position = None):
    freeAgents = league.free_agents(position)
    return freeAgents


