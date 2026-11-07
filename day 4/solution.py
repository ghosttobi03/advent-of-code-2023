import re

def parse_data():
    games = []
    
    with open("input") as f:
        data = f.read().split("\n")

        for line in data:
            cards = re.split(r':\s+', line)[1]
            cards = re.split(r'\s+\|\s+', cards)

            winning = [int(w) for w in re.split(r'\s+',cards[0])]
            owned = [int(o) for o in re.split(r'\s+',cards[1])]
            
            games.append({'winning': winning, 'owned': owned})
    return games


def solution1(games):
    
    total = 0
    
    for game in games:
        winning = game['winning']
        owned = game['owned']
        num_winning = 0
        # see if winning:
        for card in owned:
            if card in winning:
                num_winning += 1

        # calculate game score:
        if num_winning > 0:
            total += 2**(num_winning - 1)
    
    return total

if __name__ == '__main__':
    games = parse_data()
        
    print('solution 1:',solution1(games))
    
    