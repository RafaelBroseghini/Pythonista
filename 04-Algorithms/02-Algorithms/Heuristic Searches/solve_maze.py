from best_fs import *
import requests

def get(url: str) -> dict:  
    res = requests.get(url)
    return res.json()

data = get('http://api.noopschallenge.com/mazebot/random')
space = data['map']

answer = data['mazePath']

source, target = data['startingPosition'], data['endingPosition']

path = best_first_search(space, source, target)
if len(path) > 0:
    # for line in space:
    #     print(" ".join(str(x) for x in line))
    # print() 
    res = get_path(len(space[0]), len(space), source, target, path, space)
    r = requests.post('https://api.noopschallenge.com' + answer, json={'directions': res})
    print(r.text)

# print(best_first_search(maze['map'], maze['startingPosition'], maze['endingPosition']))

