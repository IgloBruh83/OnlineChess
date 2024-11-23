import socket


def Request(code, route) -> list:
    try:
        route.send(code.encode('utf-8'))
    except:
        print("Send/Request failed - ["+code+"]")
        raise ConnectionRefusedError
    finally:
        answer = route.recv(1024).decode('utf-8')
        return answer.split(".")


def StartClient(server_ip, port) -> object:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clientSocket.connect( (server_ip, port) )
        # Request a confirmation from server
        if Request("-Check", route=clientSocket) == "--Connected":
            print("Successfully connected to server")
        return clientSocket
    except:
        print("Client init failed or connection refused - [-Check]")
        raise ConnectionRefusedError
    finally:
        return clientSocket


def StopClient(route):
    try:
        if Request("-Disconnect", route=route) == "--Disconnected":
            print("Socket closed successfully - [-Disconnect]")
            route.close()
    except:
        raise ConnectionRefusedError


def RecvMainloop(route):
    while True:
        command = route.recv(1024).decode('utf-8').split(".")
        if command[0] == "--Disconnected":
            StopClient(route)
            break