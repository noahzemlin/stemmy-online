
class scoring:

    # list of players. each player object is a tuple containing sid, name, and score
    players = []
    # temp list for players who have not yet entered a name
    new_player_ids = []

    @staticmethod
    def add_player(sid):
        # add a new player who just connected
        #new_player = (sid, "NO_NAME", 0)
        scoring.new_player_ids.append(str(sid))

    @staticmethod
    def assign_name(sid, name):
        for p in scoring.new_player_ids:
            if p == sid:
                scoring.players.append((p, name, 0))
                scoring.new_player_ids.remove(p)
                break

    @staticmethod
    def remove_player(sid):
        # remove a player from the list when they disconnect
        for p in scoring.players:
            if p[0] == sid:
                scoring.players.remove(p)
                break

    @staticmethod
    def update_score(sid, points):
        for n, p in enumerate(scoring.players):
            if p[0] == sid:
                # add one point for the correct answer
                # replace tuple for player with new one with new score
                scoring.players[n] = (p[0], p[1], p[2] + points)
                break
    
    @staticmethod
    def get_leaderboard():
        # update leaderboard. sort by score
        scoring.players = sorted(scoring.players, key = lambda x: x[2], reverse=True)
        return scoring.players