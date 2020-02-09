
class scoring:

    # list of players. each player object is a tuple containing sid, name, and score
    players = []
    # temp list for players who have not yet entered a name
    no_name_players = []

    @staticmethod
    def add_player(sid):
        # add a new player who just connected
        new_player = (sid, "NO_NAME", 0)
        scoring.no_name_players.append(new_player)

    @staticmethod
    def assign_name(sid, name):
        for p in scoring.no_name_players:
            if p[0] == sid:
                scoring.players.append((p[0], name, p[2]))
                scoring.no_name_players.remove(p)
                break

    @staticmethod
    def remove_player(sid):
        # remove a player from the list when they disconnect
        for p in scoring.players:
            if p[0] == sid:
                scoring.players.remove(p)
                break
        # update leaderboard. sort by score
        scoring.players = sorted(scoring.players, key = lambda x: x[2])[:-1]

    @staticmethod
    def update_score(sid):
        for n, p in scoring.players:
            if p[0] == sid:
                # add one point for the correct answer
                # replace tuple for player with new one with new score
                scoring.players[n] = (p[0], p[1], p[2] + 1)
                break
        # update leaderboard. sort by score
        scoring.players = sorted(scoring.players, key = lambda x: x[2])[:-1]
    
    @staticmethod
    def get_leaderboard():
        return scoring.players