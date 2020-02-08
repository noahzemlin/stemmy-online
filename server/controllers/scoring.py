
class scoring:

    # list of players. each player object is a dictionary containing sid and score
    players = []

    @staticmethod
    def add_player(sid):
        new_player = (sid, 0)
        scoring.players.append(new_player)

    @staticmethod
    def update_score(sid):
        for p in scoring.players:
            if p[0] == sid:
                #give one point for the correct answer
                p[1] += 1 
        # update leaderboard. sort by score
        scoring.players = sorted(scoring.players, key = lambda x: x[1]) 
    
    @staticmethod
    def get_leaderboard():
        return scoring.players