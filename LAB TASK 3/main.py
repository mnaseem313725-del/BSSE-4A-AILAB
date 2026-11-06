graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path
    if len(path) - 1 == limit:
        for child in graph[node]:
            if child not in path:
                return "CUTOFF", None
        return "FAILURE", None
    cutoff = False
    for child in graph[node]:
        if child not in path:
            status, result = dls(child, goal, limit, path + [child])
            if status == "FOUND":
                return status, result
            if status == "CUTOFF":
                cutoff = True
    if cutoff:
        return "CUTOFF", None
    return "FAILURE", None
def iddfs(start, goal, max_depth):
    attempts = []
    for limit in range(1, max_depth + 1):
        status, path = dls(start, goal, limit, [start])
        attempts.append((limit, status, path))
        if status == "FOUND":
            return status, path, attempts
    return status, None, attempts
print("DLS RESULT")
for limit in range(1, 5):
    status, path = dls("A", "G", limit, ["A"])
    print(limit, status, path)
print("\nIDDFS RESULT")
for depth in range(1, 5):
    status, path, attempts = iddfs("A", "G", depth)
    print("Maximum :", depth)
    print("Attempt:", attempts)
    print("Result", status, path)
