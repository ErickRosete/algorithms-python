"""Given a list of numbers return all possible permutations with repetitions."""
from itertools import product

def all_permutations_with_repetitions(numbers):
    """Return all possible permutations with repetitions."""
    return product(numbers, repeat=len(numbers))

def rec_permutations_with_repetitions(numbers, index, solution, solutions):
    """Return all possible permutations with repetitions."""
    if index == len(numbers):
        solutions.append(solution)
    else:
        for num in numbers:
            rec_permutations_with_repetitions(numbers, index + 1, solution + [num], solutions)
    return solutions

def all_permutations_with_repetitions2(numbers):
    """Return all possible permutations with repetitions."""
    return rec_permutations_with_repetitions(numbers, 0, [], [])


def rec_permutations(numbers):
    """Return all possible permutations without repetitions."""
    if len(numbers) == 0 or len(numbers) == 1:
        return [numbers]
    
    solutions = []
    for i in range(len(numbers)):
        for perm in rec_permutations(numbers[:i] + numbers[i+1:]):
            solutions.append([numbers[i]] + perm)
    return solutions

def rec_permutations_with_repetitions2(numbers, repeat):
    if repeat <= 0:
        return [[]]

    solution = []
    for num in numbers:
        for sol in rec_permutations_with_repetitions2(numbers, repeat - 1):
            solution.append([num] + sol)
    return solution

def all_permutations_with_repetitions3(numbers):
    return rec_permutations_with_repetitions2(numbers, len(numbers))


def rec_combinations(numbers, group_size):
    if group_size <= 0:
        return [[]]
    
    solution = []
    for i in range(len(numbers) - group_size + 1):
        for sol in rec_combinations(numbers[i+1:], group_size - 1):
            solution.append([numbers[i]] + sol)
    return solution

if __name__ == "__main__":
    # print(list(all_permutations_with_repetitions([1, 2, 3])))
    # print(list(all_permutations_with_repetitions2(list(range(100)))))
    # print(len(rec_permutations([1,2,3,4])))
    # print(len(all_permutations_with_repetitions3([1,2,3])))
    print(rec_combinations([1,2,3,4,5], 3))
