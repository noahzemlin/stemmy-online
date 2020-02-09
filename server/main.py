import eventlet
import socketio
from controllers.game_logic import game_logic
from controllers.scoring import scoring

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ): 
    print('connect ', sid)
    # users will be asked their name before being allowed to connect
    #query = environ["QUERY_STRING"]
    #name = query[query.find("name=")+5:query.find("&")]
    #scoring.add_player(sid)

@sio.event
def join_room(sid, nameAndRoom):
    name = nameAndRoom[0]
    room = nameAndRoom[1]

    # make sure name and room are gucci
    if str.isalnum(name) and str.isalnum(room) and 2 < len(name) < 12 and 2 < len(room) < 12:
        
        # lowercase room to make it easy to type
        room = str.lower(room)

        print('received_name ', sid)
        # assign name to player
        scoring.join_room(sid, name, room)
        # put up leaderboard so everyone can see if they are in before starting
        sio.enter_room(sid, room)
        sio.emit('joined_room', room, room=sid)
        sio.emit('leaderboard', scoring.get_leaderboard(room), room=room)

@sio.event
def start(sid):
    room = scoring.playerRoom[sid]

    print('starting')
    # don't allow start game until certain number of players
    min_players = 1
    if len(scoring.rooms[room]) >= min_players: 
        # create initial set of dice and send to everyone
        dice_list = game_logic.generate_dice(num_dice=3)
        sio.emit('new_dice', dice_list)
        # put up leaderboard with everyone (with all 0 score)
        sio.emit('leaderboard', scoring.get_leaderboard(room), room=room)

@sio.event
def receive_answer(sid, ans):
    try:
        # make sure the input is an integer (already checked in JS)
        answer = int(ans)
    except:
        # ignore a non-numeric answer
        return
    print('received_answer ', sid)

    # check for cheat codes
    if answer == 3141:
        # give a lot of points
        scoring.update_score(sid, points=15)
        print('Cheater! ', sid)
    # check for reset code
    elif answer == 6282:
        # reset
        scoring.reset()
    # check if result is correct
    elif game_logic.check_result(answer):
        # result is correct, so add to the user's score
        scoring.update_score(sid, points=1)
    # result is incorrect
    else:
        sio.emit("incorrect", room=sid)
        # return instead of generating new dice
        return

    room = scoring.playerRoom[sid]
    
    # generate new dice and update leaderboard
    dice_list = game_logic.generate_dice(num_dice=3)
    sio.emit('new_dice', dice_list)
    sio.emit('leaderboard', scoring.get_leaderboard(room))
    return

@sio.event
def health(sid, data):
    print('health ', data)
    # send "health" back to requesters
    sio.emit("health", room=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    # remove person from the list
    # important so refreshing does not keep increasing the number of people
    if sid in scoring.playerRoom:
        room = scoring.playerRoom[sid]
        sio.leave_room(sid, room)
        scoring.remove_player(sid)

        # if the room still exists, update everyone
        if room in scoring.rooms:
            sio.emit('leaderboard', scoring.get_leaderboard(room))

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)