from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat  # 0 represents the left bank, 1 represents the right bank
        self.parent = parent

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0:
            return False
        if 3 - self.missionaries < 0 or 3 - self.cannibals < 0:
            return False
        if (self.cannibals > self.missionaries > 0) or (3 - self.cannibals > 3 - self.missionaries > 0):
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 1

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __str__(self):
        return f"({self.missionaries}, {self.cannibals}, {self.boat})"


def get_successors(current_state):
    successors = []
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for move in moves:
        missionaries, cannibals = move
        if current_state.boat == 0:
            new_state = State(current_state.missionaries - missionaries,
                              current_state.cannibals - cannibals,
                              1,
                              current_state)
        else:
            new_state = State(current_state.missionaries + missionaries,
                              current_state.cannibals + cannibals,
                              0,
                              current_state)
        if new_state.is_valid():
            successors.append(new_state)
    return successors


def breadth_first_search():
    initial_state = State(3, 3, 0)
    goal_state = State(0, 0, 1)

    visited = set()
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            return current_state

        visited.add(current_state)

        successors = get_successors(current_state)
        for successor in successors:
            if successor not in visited and successor not in queue:
                queue.append(successor)

    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        path = []
        while solution:
            path.insert(0, solution)
            solution = solution.parent
        for state in path:
            print(state)

if __name__ == "__main__":
    solution = breadth_first_search()
    print_solution(solution)
