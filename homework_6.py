
chess_players = {"Carlsen, Magnus": 1865, "Firouzja, Alireza": 2804, "Ding, Liren": 2799,
                 "Caruana, Fabiano": 1792, "Nepomniachtchi, Ian": 2773}

new_list = {val: i for i, val in chess_players.items() if val > 2000}

print(new_list)
