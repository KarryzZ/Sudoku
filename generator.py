import requests
import json

def load_board(level):
    r1 = requests.get('https://sugoku.herokuapp.com/board?difficulty='+ level)
    data = json.loads(r1.text)
    bod = list(data['board'])
    print(bod)
    return bod
