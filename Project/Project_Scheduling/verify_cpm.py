"""Independent CPM check for the ParkAppeal schedule (standard library, optional networkx).
Method: enumerate every path T1 -> T16, take the longest, then recompute ES/EF/LS/LF/slack
with a memoised recursion and compare with the manual forward/backward pass tables."""
from functools import lru_cache

TASKS = {  # id: (expected time in working days, predecessors)
    "T1": (3, []),
    "T2": (3, ['T1']),
    "T3": (5, ['T1']),
    "T4": (4, ['T1']),
    "T5": (6, ['T2', 'T3']),
    "T6": (6, ['T4', 'T5']),
    "T7": (5, ['T6']),
    "T8": (6, ['T4', 'T5']),
    "T9": (8, ['T8']),
    "T10": (5, ['T6', 'T8']),
    "T11": (5, ['T7', 'T9']),
    "T12": (4, ['T10', 'T11']),
    "T13": (5, ['T12']),
    "T14": (3, ['T12']),
    "T15": (2, ['T13']),
    "T16": (2, ['T14', 'T15'])
}
MANUAL = {  # id: (ES, EF, LS, LF, slack) from Critical_Path.md
    "T1": (0, 3, 0, 3, 0),
    "T2": (3, 6, 5, 8, 2),
    "T3": (3, 8, 3, 8, 0),
    "T4": (3, 7, 10, 14, 7),
    "T5": (8, 14, 8, 14, 0),
    "T6": (14, 20, 17, 23, 3),
    "T7": (20, 25, 23, 28, 3),
    "T8": (14, 20, 14, 20, 0),
    "T9": (20, 28, 20, 28, 0),
    "T10": (20, 25, 28, 33, 8),
    "T11": (28, 33, 28, 33, 0),
    "T12": (33, 37, 33, 37, 0),
    "T13": (37, 42, 37, 42, 0),
    "T14": (37, 40, 41, 44, 4),
    "T15": (42, 44, 42, 44, 0),
    "T16": (44, 46, 44, 46, 0)
}
succ = {t: [s for s, (_, p) in TASKS.items() if t in p] for t in TASKS}
starts = [t for t, (_, p) in TASKS.items() if not p]
ends = [t for t in TASKS if not succ[t]]

# 1. Enumerate all paths (depth-first) and find the longest
paths = []
def walk(t, acc):
    acc = acc + [t]
    if not succ[t]:
        paths.append(acc)
        return
    for s in succ[t]:
        walk(s, acc)
for s in starts:
    walk(s, [])
length = lambda p: sum(TASKS[t][0] for t in p)
best = max(paths, key=length)
total = length(best)
print("Paths enumerated:", len(paths))
print("Longest path:", " -> ".join(best))
print("Duration:", total, "days")

# 2. Recompute every value by memoised recursion
@lru_cache(None)
def EF(t):
    return ES(t) + TASKS[t][0]
@lru_cache(None)
def ES(t):
    return max((EF(p) for p in TASKS[t][1]), default=0)
@lru_cache(None)
def LS(t):
    return LF(t) - TASKS[t][0]
@lru_cache(None)
def LF(t):
    return min((LS(s) for s in succ[t]), default=total)

ok = True
for t in TASKS:
    got = (ES(t), EF(t), LS(t), LF(t), LS(t) - ES(t))
    if got != MANUAL[t]:
        ok = False
        print("MISMATCH", t, "script", got, "manual", MANUAL[t])
crit = [t for t in TASKS if LS(t) - ES(t) == 0]
if set(crit) != set(best):
    ok = False
    print("Critical set differs from longest path:", crit, best)

# 3. Optional cross-check with networkx
try:
    import networkx as nx
    G = nx.DiGraph()
    for t, (e, preds) in TASKS.items():
        for p in preds:
            G.add_edge(p, t)
    for t, (e, _) in TASKS.items():
        G.nodes[t]["e"] = e
    # node-weighted longest path via edge weights = duration of the source node
    for u, v in G.edges:
        G[u][v]["w"] = TASKS[u][0]
    lp = nx.dag_longest_path(G, weight="w")
    nx_total = sum(TASKS[t][0] for t in lp)
    print("networkx longest path:", " -> ".join(lp), "=", nx_total, "days")
    if lp != best or nx_total != total:
        ok = False
        print("networkx result differs")
except ImportError:
    print("networkx not installed, skipped cross-check")

print("All checks passed" if ok else "CHECKS FAILED")
