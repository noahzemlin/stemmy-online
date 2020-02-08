
class scoring:

    # list of players. each player object is a tuple containing sid, name, and score
    players = []

    @staticmethod
    def add_player(sid, name):
        # add a new player who just connected
        new_player = (sid, name, 0)
        scoring.players.append(new_player)

    @staticmethod
    def remove_player(sid):
        # remove a player from the list when they disconnect
        for p in scoring.players:
            if p[0] == sid:
                scoring.players.remove(p)
                break
        # update leaderboard. sort by score
        scoring.players = sorted(scoring.players, key = lambda x: x[2]) 

    @staticmethod
    def update_score(sid):
        for p in scoring.players:
            if p[0] == sid:
                #give one point for the correct answer
                p[2] += 1 
                break
        # update leaderboard. sort by score
        scoring.players = sorted(scoring.players, key = lambda x: x[2]) 
    
    @staticmethod
    def get_leaderboard():
        return scoring.players