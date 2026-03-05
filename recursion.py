import math

def build_recursion_tree(n):
    levels = []
    level = 0
    current_n = n

    while current_n >= 1:
        num_subproblems = 3 ** level
        subproblem_size = max(int(n / (3 ** level)), 1)
        cost_at_level = num_subproblems * subproblem_size

        levels.append((level, num_subproblems, subproblem_size, cost_at_level))

        level += 1
        current_n = current_n // 3

    return levels


def compute_total(levels):
    total = 0
    for level in levels:
        total += level[3]
    return total


def analyze(n):
    levels = build_recursion_tree(n)
    total = compute_total(levels)

    print("="*70)
    print(f"Recursion Tree for T(n) = 3T(n/3) + n, n = {n}")
    print("="*70)
    print(f"{'Level':<10}{'#Subproblems':<15}{'Size':<10}{'Cost'}")
    print("-"*50)

    for lvl, sub, size, cost in levels:
        print(f"{lvl:<10}{sub:<15}{size:<10}{cost}")

    print("-"*50)
    print("Total Estimated Cost:", total)

    print("\nMaster Theorem Analysis:")
    print("T(n) = aT(n/b) + f(n)")
    print("a = 3, b = 3, f(n) = n")
    print("n^(log_b(a)) = n^(log3(3)) = n")
    print("Therefore T(n) = Θ(n log n)")


n = int(input("Enter value of n: "))
analyze(n)