import threading
from math import ceil
from Client import Client
from SetupWindow import SetupWindow
from Network import Connect

server_cfg = {
    'ip': '78.47.210.90',
    'port': 13579
}

setup = SetupWindow()
setup.root.mainloop()

name = setup.nameField.get()
setup.root.destroy()
w = Client()

field = [ ['rook_w', 'pawn_w', None, None, None, None, 'pawn_b', 'rook_b'],
          ['knight_w', 'pawn_w', None, None, None, None, 'pawn_b', 'knight_b'],
          ['bishop_w', 'pawn_w', None, None, None, None, 'pawn_b', 'bishop_b'],
          ['queen_w', 'pawn_w', None, None, None, None, 'pawn_b', 'queen_b'],
          ['king_w', 'pawn_w', None, None, None, None, 'pawn_b', 'king_b'],
          ['bishop_w', 'pawn_w', None, None, None, None, 'pawn_b', 'bishop_b'],
          ['knight_w', 'pawn_w', None, None, None, None, 'pawn_b', 'knight_b'],
          ['rook_w', 'pawn_w', None, None, None, None, 'pawn_b', 'rook_b'] ]
gameStarted = True
visualPieces = []
selected = None ; selector = None


def DrawPieces():
    global selector
    for i in visualPieces:
        w.c.delete(i)
    w.c.delete(selector)
    for x in range(8):
        for y in range(8):
            if field[x][y] is not None:
                visualPieces.append(w.c.create_image(x * 75, (7-y) * 75, anchor='nw', image=w.sprites[field[x][y]]))
    if selected is not None:
        selector = w.c.create_rectangle(selected[0] * 75 +5, (7-selected[1]) * 75 +5, selected[0] * 75 +70, (7-selected[1]) * 75 + 70, outline="red", width=2)
    w.c.update()
DrawPieces()

def OnClick(event):
    if not gameStarted:
        return
    global selected
    x, y = ceil(event.x / 75)-1, 8-ceil(event.y / 75)
    w.hint.config(text=f"You clicked field {x}:{y}")
    if selected is None:
        if field[x][y] is None:
            return
        selected = [x, y]
    else:
        SendMove(selected[0], selected[1], x, y)
        selected = None
    DrawPieces()

def ApplyMove(_field, x1, y1, x2, y2):
    _newField = _field
    pieceToMove = _newField[x1][y1]
    _newField[x1][y1] = None
    _newField[x2][y2] = pieceToMove
    DrawPieces()
    return _newField

def SendMove(x1, y1, x2, y2):
    global socket
    global field
    socket.send(f"{x1}.{y1}.{x2}.{y2}")
    ApplyMove(field, x1, y1, x2, y2)



socket = Connect(server_cfg)
socket.send(f"{name}".encode())

def Listen():
    global gameStarted
    global socket
    global field
    while True:
        command = socket.recv(1024).decode()
        if not gameStarted:
            if command == 'START':
                gameStarted = True
        else:
            temp = command.split(".")
            ApplyMove(field, int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3]))


input_thread = threading.Thread(target=Listen)
input_thread.start()
w.c.bind_all("<Button-1>", OnClick)
w.root.mainloop()
