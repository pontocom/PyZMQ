import zmq

context = zmq.Context()

print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    message = input("Enter your message: ")
    socket.send_string(message)

    message_received = socket.recv_string()

    print("RECEIVED: " + message_received)

    if message_received == "TERMINATE":
        break

print("Finished server and client")
