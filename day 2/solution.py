'''To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, 
grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number 
(like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag 
(like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 
4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, 
and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. 
However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, 
game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games 
that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, 
and 14 blue cubes. What is the sum of the IDs of those games?'''

possible_games = 0
all_games = []

def validateGames(game, red_base, green_base, blue_base):
    for round in game:
        if round['red'] > red_base or round['green'] > green_base or round['blue'] > blue_base:
            return False
    return True

def parse_data():
    with open("input") as f:
        game_data = f.read().split("\n")
        all_games = []

        for i in range(len(game_data)):
            rounds = (
                game_data[i]
                .split(": ")[1]
                .split("; ")
            )
            game = []

            for round in rounds:
                round = round.split(", ")
                dice = {
                        'red': 0,
                        'green': 0,
                        'blue': 0
                    }

                for line in round:
                    val_key = line.split(' ')
                    dice[val_key[1]] = int(val_key[0])

                game.append(dice)
            all_games.append(game)

        return all_games

'''PART 1'''
red_base = 12
green_base = 13
blue_base = 14  

all_games = parse_data()

for i in range(len(all_games)):
    if validateGames(all_games[i], red_base, green_base, blue_base):
        possible_games += (i+1)
print(possible_games)

'''PART 2'''
output = 0

for game in all_games:
    red = max([round['red'] for round in game])
    green = max([round['green'] for round in game])
    blue = max([round['blue'] for round in game])

    power = red * green * blue
    output += power
    
print(output)


'''
To Do 1: Find the minimum set of cubes for each game - iterate through each round (dict) of each game (list)
To Do 2: Find the power of each set
To Do 3: Sum the power of all sets
    Use Alt to alter multiple lines of code at once
    Use Alt and arrow to move lines around
    List iteration

'''