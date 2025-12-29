from player import Player3d, Player2d, Player1d


probabilities = (0.1, 0.5)
size = 10000
epochs = 100000

player_list = [Player1d(*probabilities) for _ in range(size)]

def remove_dead(player_list):

    new_player_list = []

    for player in player_list:
        if player.pos_x == 0 and player.pos_y == 0 and player.pos_z == 0:
            pass
        else:
            new_player_list.append(player)

    return new_player_list


for epoch in range(epochs):
    for player in player_list:

        player.random_walk()

    player_list = remove_dead(player_list) 
    print(1 - (len(player_list)/size))
