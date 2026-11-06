'''
The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't 
really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
(Periods (.) do not count as a symbol.)

What is the sum of all of the part numbers in the engine schematic?
'''

def createArray():
    with open('input') as f:
        graph = [list(line.strip('\n')) for line in f.readlines()]
    return graph

def solution1(graph: list[list[str]]):
    total = 0

    # Finds leftmost digits based off indices

    for row_idx in range(len(graph)):
        col_idx = 0

        while col_idx < len(graph[row_idx]):

            if graph[row_idx][col_idx].isdigit():
                left_x = col_idx
                
                right_x = get_rightmost_index(left_x, graph[row_idx])

                if find_symbols(row_idx, left_x, right_x):
                    discovered_number = int(''.join(graph[row_idx][left_x:right_x+1]))

                    total += discovered_number

                col_idx = right_x + 1
            else: 
                col_idx += 1
    return total

def get_rightmost_index(col_idx, row):
    while col_idx <= len(row) - 1 and row[col_idx].isdigit():
        col_idx += 1
    return col_idx - 1

def get_leftmost_index(col_idx, row):
    while col_idx >= 0 and row[col_idx].isdigit():
        col_idx -= 1
    return col_idx + 1

def find_symbols(row_idx, left_x, right_x):
    '''
    row_idx is the number of the row we are working on
    left_x is the index value of the leftmost value
    right_x is the index value of the rightmost value
    graph[row_idx][left_x] is the number at the leftmost index
    graph[row_idx][right_x + 1] is the number at the rightmost index
    '''

    symbols = ["!","@","#","$","%","^","&","*","(",")","-","+","=","?","/","<",">"]

    for i in range(row_idx - 1, row_idx + 2):
        for j in range(left_x - 1, right_x + 2):
            
            if i < 0 or i > len(graph) - 1:
                continue
            if j < 0 or j > len(graph[row_idx]) - 1:
                continue
            
            if graph[i][j] in symbols:
                return True


def solution2(graph):
    '''
    The missing part wasn't the only issue - one of the gears in the engine is wrong. 
    A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

    This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.
    '''

    total = 0

    for row_idx in range(len(graph)):
        col_idx = 0

        for col_idx in range(len(graph[row_idx])):

            if graph[row_idx][col_idx] == "*":
                gear_ratio = check_gear_ratio(graph, row_idx, col_idx)

                if gear_ratio is not None:
                    total += gear_ratio
    return total

def check_gear_ratio(graph, row_idx, col_idx):

    gear_numbers = []

    for i in range(row_idx - 1, row_idx + 2):
        j = col_idx - 1
        while j < col_idx + 2:

            if i < 0 or i >= len(graph):
                continue
            if j < 0 or j >= len(graph[i]):
                continue

            if graph[i][j].isdigit():
                left_x = get_leftmost_index(j,graph[i])
                right_x = get_rightmost_index(j,graph[i])
                
                gear_numbers.append(int(''.join(graph[i][left_x:right_x+1])))

                j = right_x
            j = j + 1
    if len(gear_numbers) == 2:
        print(gear_numbers)
        product = gear_numbers[0] * gear_numbers[1]
        return product






'''
When python begins to interpret the file being run, it is pulled into a buffer and renamed to "__main__".
If a file is not the main file being run (i.e. if it is being imported and used as a utility), the main code
should NOT run. This is why we use the condition below.

Often, developers in the real world use this condition to run a quick demo or test suite for moments where they
need to refresh themselves on functionality of a single component of a much larger system.
'''
if __name__ == '__main__':
    graph = createArray()

    print("solution 1:")
    print('ANSWER:',solution1(graph))
    print('solution 2:')
    print('ANSWER:',solution2(graph))