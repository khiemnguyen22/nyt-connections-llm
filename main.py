# pylint: disable=redefined-outer-name
import datetime
import json
import random 

def date_to_puzzle(date):
    first_puzzle_id = 204
    first_date = datetime.datetime.strptime('01/01/2024','%m/%d/%Y')

    number_of_days = (date - first_date)
    return first_puzzle_id + number_of_days.days

def load_puzzle(puzzle_data, puzzle_id):
    for puzzle in puzzle_data:
        # print(puzzle['puzzle_id'])
        if puzzle['puzzle_id'] == str(puzzle_id):
            return puzzle['content']
    return None

def load_words(puzzle_content):
    answers, words = {}, []
    for group in puzzle_content:
        answers[group['description']] = group['words']
        words += group['words']
    return answers, words

def llm_suggestion(words):
    pass

if __name__ == '__main__':
    date_str = input('Choose date (MM/DD/2024): ')
    date = datetime.datetime.strptime(date_str, '%m/%d/%Y')

    puzzle_id = date_to_puzzle(date)
    print('Puzzle Number: ', puzzle_id)

    with open('nyt_connect_crawler/puzzles.json') as f:
        puzzle_data = json.load(f)
    
    content = load_puzzle(puzzle_data, puzzle_id)
    answers, words = load_words(content)

    random.shuffle(words)
    
    print(f'\n-----Puzzle {puzzle_id} - {date_str}-----')
    for i in range(4):
        print('| ' + ' | '.join(words[i*2: i*2 + 4]) + ' |')

    i = 0
    while i < 4:
        reveal = input('\n reveal 1 group (y/n)?: ')
        if reveal == 'y':
            print(f'\n----- Group {i + 1} -----')
            group = list(answers.keys())[i]
            print(f'{group}: '+ ', '.join(answers[group]))
            i += 1
        else:
            continue
        
