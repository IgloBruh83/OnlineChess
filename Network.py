import socket


def Connect(cfg):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(( cfg['ip'], cfg['port'] ))
    print(f"Підключено до сервера {cfg['ip']}:{cfg['port']}")

    return clientSocket