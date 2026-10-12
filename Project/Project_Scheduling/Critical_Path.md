# Critical Path

## Result

**Critical Path:** T1 -> T3 -> T5 -> T8 -> T9 -> T11 -> T12 -> T13 -> T15 -> T16

**Expected Project Duration:** 46 days (9 weeks and 1 day, Mon 12 Oct 2026 to Mon 14 Dec 2026)

**Critical Path activities:** T1 Requirements Refinement & Model Alignment (3); T3 Database Schema & Seed Data (5); T5 Authentication & Role-Based Access (6); T8 Violation Management Module (2.0) (6); T9 Appeals Module (3.0) (8); T11 Notification Module (5.0) (5); T12 Integration & Regression Testing (4); T13 System & Acceptance Testing (5); T15 Deployment Preparation (2); T16 Final Demo & Report Packaging (2).

Check: 3 + 5 + 6 + 6 + 8 + 5 + 4 + 5 + 2 + 2 = 46 days.

## Forward pass (ES and EF)

Rule: ES = largest EF among the predecessors (0 if none). EF = ES + E.

| Task | Predecessors | E | ES | EF | Working |
| --- | --- | --- | --- | --- | --- |
| T1 | - | 3 | 0 | 3 | ES = 0; EF = 0 + 3 = 3 |
| T2 | T1 | 3 | 3 | 6 | ES = max(EF(T1)=3) = 3; EF = 3 + 3 = 6 |
| T3 | T1 | 5 | 3 | 8 | ES = max(EF(T1)=3) = 3; EF = 3 + 5 = 8 |
| T4 | T1 | 4 | 3 | 7 | ES = max(EF(T1)=3) = 3; EF = 3 + 4 = 7 |
| T5 | T2, T3 | 6 | 8 | 14 | ES = max(EF(T2)=6, EF(T3)=8) = 8; EF = 8 + 6 = 14 |
| T6 | T4, T5 | 6 | 14 | 20 | ES = max(EF(T4)=7, EF(T5)=14) = 14; EF = 14 + 6 = 20 |
| T7 | T6 | 5 | 20 | 25 | ES = max(EF(T6)=20) = 20; EF = 20 + 5 = 25 |
| T8 | T4, T5 | 6 | 14 | 20 | ES = max(EF(T4)=7, EF(T5)=14) = 14; EF = 14 + 6 = 20 |
| T9 | T8 | 8 | 20 | 28 | ES = max(EF(T8)=20) = 20; EF = 20 + 8 = 28 |
| T10 | T6, T8 | 5 | 20 | 25 | ES = max(EF(T6)=20, EF(T8)=20) = 20; EF = 20 + 5 = 25 |
| T11 | T7, T9 | 5 | 28 | 33 | ES = max(EF(T7)=25, EF(T9)=28) = 28; EF = 28 + 5 = 33 |
| T12 | T10, T11 | 4 | 33 | 37 | ES = max(EF(T10)=25, EF(T11)=33) = 33; EF = 33 + 4 = 37 |
| T13 | T12 | 5 | 37 | 42 | ES = max(EF(T12)=37) = 37; EF = 37 + 5 = 42 |
| T14 | T12 | 3 | 37 | 40 | ES = max(EF(T12)=37) = 37; EF = 37 + 3 = 40 |
| T15 | T13 | 2 | 42 | 44 | ES = max(EF(T13)=42) = 42; EF = 42 + 2 = 44 |
| T16 | T14, T15 | 2 | 44 | 46 | ES = max(EF(T14)=40, EF(T15)=44) = 44; EF = 44 + 2 = 46 |

Project duration = largest EF = 46 (T16).

## Backward pass (LF and LS) and slack

Rule: LF = smallest LS among the successors (project duration 46 if none). LS = LF - E. Slack = LS - ES (equal to LF - EF).

| Task | Successors | E | LF | LS | Slack | Working |
| --- | --- | --- | --- | --- | --- | --- |
| T16 | - | 2 | 46 | 44 | 0 | LF = 46; LS = 46 - 2 = 44; Slack = 44 - 44 = 0 |
| T15 | T16 | 2 | 44 | 42 | 0 | LF = min(LS(T16)=44) = 44; LS = 44 - 2 = 42; Slack = 42 - 42 = 0 |
| T14 | T16 | 3 | 44 | 41 | 4 | LF = min(LS(T16)=44) = 44; LS = 44 - 3 = 41; Slack = 41 - 37 = 4 |
| T13 | T15 | 5 | 42 | 37 | 0 | LF = min(LS(T15)=42) = 42; LS = 42 - 5 = 37; Slack = 37 - 37 = 0 |
| T12 | T13, T14 | 4 | 37 | 33 | 0 | LF = min(LS(T13)=37, LS(T14)=41) = 37; LS = 37 - 4 = 33; Slack = 33 - 33 = 0 |
| T11 | T12 | 5 | 33 | 28 | 0 | LF = min(LS(T12)=33) = 33; LS = 33 - 5 = 28; Slack = 28 - 28 = 0 |
| T10 | T12 | 5 | 33 | 28 | 8 | LF = min(LS(T12)=33) = 33; LS = 33 - 5 = 28; Slack = 28 - 20 = 8 |
| T9 | T11 | 8 | 28 | 20 | 0 | LF = min(LS(T11)=28) = 28; LS = 28 - 8 = 20; Slack = 20 - 20 = 0 |
| T8 | T9, T10 | 6 | 20 | 14 | 0 | LF = min(LS(T9)=20, LS(T10)=28) = 20; LS = 20 - 6 = 14; Slack = 14 - 14 = 0 |
| T7 | T11 | 5 | 28 | 23 | 3 | LF = min(LS(T11)=28) = 28; LS = 28 - 5 = 23; Slack = 23 - 20 = 3 |
| T6 | T7, T10 | 6 | 23 | 17 | 3 | LF = min(LS(T7)=23, LS(T10)=28) = 23; LS = 23 - 6 = 17; Slack = 17 - 14 = 3 |
| T5 | T6, T8 | 6 | 14 | 8 | 0 | LF = min(LS(T6)=17, LS(T8)=14) = 14; LS = 14 - 6 = 8; Slack = 8 - 8 = 0 |
| T4 | T6, T8 | 4 | 14 | 10 | 7 | LF = min(LS(T6)=17, LS(T8)=14) = 14; LS = 14 - 4 = 10; Slack = 10 - 3 = 7 |
| T3 | T5 | 5 | 8 | 3 | 0 | LF = min(LS(T5)=8) = 8; LS = 8 - 5 = 3; Slack = 3 - 3 = 0 |
| T2 | T5 | 3 | 8 | 5 | 2 | LF = min(LS(T5)=8) = 8; LS = 8 - 3 = 5; Slack = 5 - 3 = 2 |
| T1 | T2, T3, T4 | 3 | 3 | 0 | 0 | LF = min(LS(T2)=5, LS(T3)=3, LS(T4)=10) = 3; LS = 3 - 3 = 0; Slack = 0 - 0 = 0 |

## Summary table

| Task | E | ES | EF | LS | LF | Slack | Critical |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | 3 | 0 | 3 | 0 | 3 | 0 | Yes |
| T2 | 3 | 3 | 6 | 5 | 8 | 2 | No |
| T3 | 5 | 3 | 8 | 3 | 8 | 0 | Yes |
| T4 | 4 | 3 | 7 | 10 | 14 | 7 | No |
| T5 | 6 | 8 | 14 | 8 | 14 | 0 | Yes |
| T6 | 6 | 14 | 20 | 17 | 23 | 3 | No |
| T7 | 5 | 20 | 25 | 23 | 28 | 3 | No |
| T8 | 6 | 14 | 20 | 14 | 20 | 0 | Yes |
| T9 | 8 | 20 | 28 | 20 | 28 | 0 | Yes |
| T10 | 5 | 20 | 25 | 28 | 33 | 8 | No |
| T11 | 5 | 28 | 33 | 28 | 33 | 0 | Yes |
| T12 | 4 | 33 | 37 | 33 | 37 | 0 | Yes |
| T13 | 5 | 37 | 42 | 37 | 42 | 0 | Yes |
| T14 | 3 | 37 | 40 | 41 | 44 | 4 | No |
| T15 | 2 | 42 | 44 | 42 | 44 | 0 | Yes |
| T16 | 2 | 44 | 46 | 44 | 46 | 0 | Yes |

## Explanation

The critical path is the longest chain of dependent tasks from T1 to T16. Every task on it has slack 0 (LS = ES and LF = EF), so a delay of one day in any of them delays the whole project by one day. The path runs through the database and access-control foundation (T3, T5), then the violation and appeals modules (T8, T9), because the Appeals module needs violation records to exist (an appeal must match a violation). Notifications (T11) wait for the permit and appeals modules because they react to their status changes. Testing and deployment preparation (T12, T13, T15) and the final packaging (T16) follow in sequence.

Why the other tasks are not critical: T2 has 2 days of slack; T4 has 7 days of slack; T6 has 3 days of slack; T7 has 3 days of slack; T10 has 8 days of slack; T14 has 4 days of slack. For example T2 (3 days) can slip 2 days because T5 also waits for T3 (5 days), the longer of the two predecessors; T10 can slip 8 days because T12 cannot start until T11 finishes on day 33 and T10 finishes on day 25.

Only one path has zero slack, so there is a single critical path.

## Verification

1. `verify_cpm.py` (in this folder) recomputes the schedule with a different method: it enumerates every path from T1 to T16, takes the longest, and compares it and every ES, EF, LS, LF and slack value against a forward and backward pass. It also cross-checks with the `networkx` longest-path function. Run `python verify_cpm.py`; expected last lines:

```
Longest path: T1 -> T3 -> T5 -> T8 -> T9 -> T11 -> T12 -> T13 -> T15 -> T16
Duration: 46 days
All checks passed
```

2. **Project-management tool check (team to do and screenshot):** import `WBS_for_Project_Tool.csv` into GanttProject, MS Project or a similar tool (columns: ID, Task Name, Duration, Predecessors), set finish-to-start links, and confirm the tool highlights the same critical path and a project duration of 46 working days. Add the screenshot to the report.
