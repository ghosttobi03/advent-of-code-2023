'''
The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last digit 
(in that order) to form a single two-digit number.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''
import re

def part1():
    '''
    Solution to AOC2023, Day 1 (part 1)
    '''

    with open("input", 'r') as f: 
        lines = f.readlines()
    parsed_nums = [0] * len(lines)
        
    regex = re.compile(r'[0-9]')

    
    for i in range(len(lines)):
        matches = regex.findall(lines[i])
        if len(matches) == 0:
            pass
        else: 
            parsed_nums[i] = int(matches[0])*10 + int(matches[-1])

    return sum(parsed_nums)


def part2():
    '''
    Solution to AOC2023, Day 1 (part 2)
    '''

    with open("input", 'r') as f: 
        lines = f.readlines()
    parsed_nums = [0] * len(lines)
        
    for i in range(len(lines)):
        extracted = extract_digits(lines[i])
        parsed_nums[i] = extracted[0]*10 + extracted[1]       

    return sum(parsed_nums)

def extract_digits(line: str):
    '''
    Extract the first and last digits from a line,
    then concat them to make a two-digit number
    '''

    regex = re.compile(r'\d|one|two|three|four|five|six|seven|eight|nine')

    # Forward:
    first = -1
    for i in range(len(line)):
        match = regex.findall(line[:i])
        if len(match) > 0:
            first = str_to_digit(match[0])
            break
    if first < 0:
        raise Exception('Could not parse first number!')
            
    # Backward:
    last = -1
    for i in range(1, len(line)+1):
        match = regex.findall(line[-i:])
        if len(match) > 0:
            last = str_to_digit(match[0])
            break
    if last < 0:
        raise Exception('Could not parse last number!')
  
    return [first, last]

def str_to_digit(num):
    '''
    Turns a string number into an integer
    '''
    if num.isdigit():
        return int(num)
        
    WORDS_TO_NUMBERS = ['zero','one','two','three','four','five','six','seven','eight','nine']
    return WORDS_TO_NUMBERS.index(num)


if __name__ == '__main__':
    print('Part 1:', part1())    
    print('Part 2:', part2()) 