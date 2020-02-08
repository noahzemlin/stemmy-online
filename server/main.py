import eventlet
import socketio
from controllers.game_logic import game_logic

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    # create initial set of dice and send to everyone
    dice_list = game_logic.generate_dice(num_dice=3)
    sio.emit(dice_list)

@sio.event
def receive_answer(sid, answer):
    print('received ', sid)
    # check if result is correct
    if game_logic.check_result(answer):
        # result is correct, so note the user and add to their score TODO
        
        # send new dice set out since current one was guessed
        dice_list = game_logic.generate_dice(num_dice=3)
        sio.emit(dice_list)
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

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)