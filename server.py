import time
import zmq

# implements the REQuest/REPly paradigm 

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Waiting for messages...")

while True:
    message = socket.recv_string()

    print("Message received = " + message)

    if message == "TERMINATE":
        socket.send_string("TERMINATE")
        break
    else:
        socket.send_string("SERVER -> " + message)