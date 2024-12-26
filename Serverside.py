import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 13579))
server_socket.listen(10)
print(f"Server started. Waiting for players")

queue = []
currentGames = []

def AwaitForPlayers():
    global queue; global currentGames
    while True:
        conn, addr = server_socket.accept()
        callback = conn.recv(1024).decode()
        if callback != "" and callback is not None:
            queue.append( [conn, addr, callback] )
        if len(queue) >= 2:
            currentGames.append(Game(queue[0], queue[1]))

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1
        self.field = [ ['rook_w', 'pawn_w', None, None, None, None, 'pawn_b', 'rook_b'],
                       ['knight_w', 'pawn_w', None, None, None, None, 'pawn_b', 'knight_b'],
                       ['bishop_w', 'pawn_w', None, None, None, None, 'pawn_b', 'bishop_b'],
                       ['queen_w', 'pawn_w', None, None, None, None, 'pawn_b', 'queen_b'],
                       ['king_w', 'pawn_w', None, None, None, None, 'pawn_b', 'king_b'],
                       ['bishop_w', 'pawn_w', None, None, None, None, 'pawn_b', 'bishop_b'],
                       ['knight_w', 'pawn_w', None, None, None, None, 'pawn_b', 'knight_b'],
                       ['rook_w', 'pawn_w', None, None, None, None, 'pawn_b', 'rook_b'] ]


        player1[0].send("START")
        player2[0].send("START")
        while True:
            move = self.player1[0].recv(1024).decode() if self.turn == 1 else self.player2[0].recv(1024).decode()
            temp = move.split(".")
            self.field = ApplyMove(self.field, temp[0], temp[1], temp[2], temp[3])

            player1[0].send(f"{temp[0]}.{temp[1]}.{temp[2]}.{temp[3]}")
            player2[0].send(f"{temp[0]}.{temp[1]}.{temp[2]}.{temp[3]}")

            if self.turn == 1:
                self.turn = 2
            else:
                self.turn = 1

    def ApplyMove(self, _field, x1, y1, x2, y2):
        _newField = _field
        pieceToMove = _newField[x1][y1]
        _newField[x1][y1] = None
        _newField[x2][y2] = pieceToMove
        return _newField

