
class scoring:

    # list of rooms with lists of players. each player object is a tuple containing sid, name, and score
    # replace all scoring.players with scoring.rooms[<room>]
    rooms = {}

    playerRoom = {}

    @staticmethod
    def join_room(sid, name, room):

        # player is already in a room, but we shouldn't see this happen
        if sid in scoring.playerRoom:
            return

        # if the room doesn't exist, make it
        if not room in scoring.rooms:
            scoring.rooms[room] = [(0,"Stemmy",-50)]

        # join the player into a room
        scoring.rooms[room].append((sid, name, 0))
        scoring.playerRoom[sid] = room

        print(scoring.rooms)
        print(scoring.playerRoom)

    @staticmethod
    def remove_player(sid):
        room = scoring.playerRoom[sid]

        del scoring.playerRoom[sid]

        # remove a player from the list when they disconnect
        for p in scoring.rooms[room]:
            if p[0] == sid:
                scoring.rooms[room].remove(p)
                break

        # if no one left in the room (besides stemmy), delete it
        if len(scoring.rooms[room]) == 1:
            del scoring.rooms[room]

    @staticmethod
    def update_score(sid, points):
        room = scoring.playerRoom[sid]

        for n, p in enumerate(scoring.rooms[room]):
            # give stemmy points
            if p[0] == 0:
                scoring.rooms[room][n] = (0, "Stemmy", p[2] + points)
            # give player points
            if p[0] == sid:
                # add points for the correct answer
                # replace tuple for player with new one with new score
                scoring.rooms[room][n] = (p[0], p[1], p[2] + points)
    
    @staticmethod
    def get_leaderboard(room):
        # update leaderboard. sort by score
        scoring.rooms[room] = sorted(scoring.rooms[room], key = lambda x: x[2], reverse=True)
        return scoring.rooms[room]

    @staticmethod
    def reset():
        # # reset all players to 0 and stemmy to -50
        # for n, p in enumerate(scoring.players):
        #     # look for stemmy
        #     if p[0] == 0:
        #         scoring.players[n] = (0, "Stemmy", -50)
        #     # look for players
        #     if p[0] != 0:
        #         scoring.players[n] = (p[0], p[1], 0)
        scoring.rooms = {}
        scoring.playerRoom = {}