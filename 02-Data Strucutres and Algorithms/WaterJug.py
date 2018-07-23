from copy import copy

class Jug:
    def __init__(self, max):
        self.max = max
        self.jug_volume = 0

    def empty_my_jug(self):
        self.jug_volume = 0

    def fill_my_jug(self):
        self.jug_volume = self.max

    def transfer_from_jug_to_jug(self, other_jug):
        total_jug_volume = self.jug_volume + other_jug.jug_volume
        if total_jug_volume <= other_jug.max:
            self.jug_volume = 0
            other_jug.jug_volume = total_jug_volume
        else:
            to_transfer = other_jug.max - other_jug.jug_volume
            self.jug_volume -= to_transfer
            other_jug.jug_volume += to_transfer
            
            
            
class State:
    def __init__(self, jug_a, jug_b):
        self.a = jug_a
        self.b = jug_b

    def __eq__(self, other):
        return self.a.jug_volume == other.a.jug_volume and self.b.jug_volume == other.b.jug_volume

    def __str__(self):
        return '({}, {})'.format(self.a.jug_volume, self.b.jug_volume)

    def clone(self, moves, visited_states):
        states = []
        for key in moves.keys():
            a_copy, b_copy = copy(self.a), copy(self.b)
            moves[key](a_copy, b_copy)
            state = State(a_copy, b_copy)
            if state not in visited_states:
                states.append(state)
        return states

    # State goal: 2 gallons in the first jug and 0 in the second.
    
    def goal(self):
        return self.a.jug_volume == 2 and self.b.jug_volume == 0
    
    
def main():
    
    jug_1 = Jug(4)
    jug_2 = Jug(3)
    
    
    # Moves as a dictionary with lambda as optimizer. 
    moves = {
        'Empty 1': lambda a, b: a.empty_my_jug(),
        'Empty 2': lambda a, b: b.empty_my_jug(),
        'Fill 1': lambda a, b: a.fill_my_jug(),
        'Fill 2': lambda a, b: b.fill_my_jug(),
        'Transfer from 1 to 2': lambda a, b: a.transfer_from_jug_to_jug(b),
        'Transfer from 1 to 2': lambda a, b: b.transfer_from_jug_to_jug(a)
    }

    start = State(jug_1, jug_2)
    visited = [start]
    path = search(start, moves, visited)


    print()
    print('Water Jug Problem: ')
    print(start, end = ' ')
    for step in path:
        print(step, end = ' ')

# Recursive function to find path.
 
def search(start_state, moves, visited_states):
    path = []
    if not start_state.goal():
        new_states = start_state.clone(moves, visited_states)
        visited_states.extend(new_states)
        for state in new_states:
            if state.goal():
                path.append(state)
                break
            else:
                searched_path = search(state, moves, visited_states)
                if searched_path:
                    path.append(state)
                    path.extend(searched_path)
                    break
    return path



main()
