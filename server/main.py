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
    scoring.add_player(sid)

@sio.event
def assign_name(sid, name):
    print('received_name ', sid)
    # assign name to player
    scoring.assign_name(sid, name)
    # put up leaderboard so everyone can see if they are in before starting
    sio.emit('leaderboard', scoring.get_leaderboard())

@sio.event
def start(sid):
    print('starting')
    # don't allow start game until certain number of players
    min_players = 1
    if len(scoring.players) >= min_players: 
        # create initial set of dice and send to everyone
        dice_list = game_logic.generate_dice(num_dice=3)
        sio.emit('new_dice', dice_list)
        # put up leaderboard with everyone (with all 0 score)
        sio.emit('leaderboard', scoring.get_leaderboard())

@sio.event
def receive_answer(sid, ans):
    try:
        answer = int(ans)
    except:
        # ignore a non-numeric answer
        return

    print('received_answer ', sid)
    # check if result is correct
    if game_logic.check_result(answer):
        # result is correct, so add to the user's score
        scoring.update_score(sid)
        # send new dice set out since current one was guessed
        dice_list = game_logic.generate_dice(num_dice=3)
        sio.emit('new_dice', dice_list)
        # update leaderboard
        sio.emit('leaderboard', scoring.get_leaderboard())
    else:
        sio.emit("incorrect", room=sid)

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
    scoring.remove_player(sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)