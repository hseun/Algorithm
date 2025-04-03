from collections import Counter
import sys
input = sys.stdin.readline

trees = []

while True:
    tree = input().strip()
    if tree == '':
        break
    trees.append(tree)

total_tree = len(trees)
trees_count = Counter(trees)
trees = sorted(set(trees))

for tree in trees:
    print(f"{tree} {trees_count[tree] / total_tree * 100:.4f}")