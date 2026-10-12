# Work Breakdown Structure (WBS)

Project: ParkAppeal. Process model: Incremental (Process_Model.md). Durations are the expected times E from the three-point estimates below, in working days.

| ID | Task Name | Description | Predecessor(s) | Duration (Days) |
| --- | --- | --- | --- | --- |
| T1 | Requirements Refinement & Model Alignment | Resolve Lab 3 / Lab 4 inconsistencies (actors, FR-05, eligibility and quota flows), freeze the FR/UC list and set increment priorities. | - | 3 |
| T2 | Architecture & Dev Environment Setup | Choose the web stack, define one module per Level-0 process, set up repository branches, CI and shared configuration. | T1 | 3 |
| T3 | Database Schema & Seed Data | Design D1 User and Vehicle Registry, D2 Permit Records, D3 Violation Records and D4 Appeal Records; create seeded test users, vehicles and permits (Scope.md: seeded data only). | T1 | 5 |
| T4 | UI/UX Wireframes & Responsive Layouts | Wireframes for Permit Holder, Parking Officer, Administrator and Appeals Officer screens; responsive layouts for phone, tablet and desktop (FR-06, FR-07). | T1 | 4 |
| T5 | Authentication & Role-Based Access | Registration and login, four roles, permission checks on every route, automatic logout after 15 minutes of inactivity (NFR-06). | T2, T3 | 6 |
| T6 | Permit Application Module (1.0) | Application form, document upload from any device, eligibility evaluation, renewal and permit status (FR-08, FR-18; UC-06, UC-08). | T4, T5 | 6 |
| T7 | Admin Decision, Quota & Issuance (1.0) | Approve or reject with reason, quota check, issue one uniquely numbered permit with start and expiry dates, Expired status (FR-16, FR-17, FR-19, FR-20; UC-07, UC-16 to UC-20). | T6 | 5 |
| T8 | Violation Management Module (2.0) | Plate lookup, record violation with type and location, evidence upload, unmatched violations, void with reason (FR-11 to FR-15; UC-11 to UC-15). | T4, T5 | 6 |
| T9 | Appeals Module (3.0) | Submit appeal inside the 14-day window, evidence upload, status tracking, officer review and decision with justification (FR-01 to FR-04; UC-01 to UC-04). | T8 | 8 |
| T10 | Search & Reporting Module (4.0) | Search and filter permits, violations and appeals by status or date; reports on permits issued, violations recorded and appeal outcomes (FR-09; UC-09). | T6, T8 | 5 |
| T11 | Notification Module (5.0) | In-app and email notifications on permit, violation and appeal status changes, including appeal confirmation email (FR-01, FR-10; UC-10). | T7, T9 | 5 |
| T12 | Integration & Regression Testing | Merge all increments, verify data flows between processes and data stores D1 to D4, run the regression suite. | T10, T11 | 4 |
| T13 | System & Acceptance Testing | Test cases derived from UC-01 to UC-20 and scenarios S-01 to S-06; check NFR targets (form load time, role restrictions, session timeout). | T12 | 5 |
| T14 | Documentation & User Guide | User guide for the four roles; update repository documents to match the final system. | T12 | 3 |
| T15 | Deployment Preparation | Demo environment, configuration, seed data load and demo database backup (production deployment is out of scope per Scope.md). | T13 | 2 |
| T16 | Final Demo & Report Packaging | Demo script, final lab report with team names and IDs, repository link and AI-use declaration. | T14, T15 | 2 |

## Time estimates (three-point)

Expected time: **E = (O + 4M + P) / 6**, where O = optimistic, M = most likely, P = pessimistic (working days). Estimates assume a team of 4 working part-time alongside other courses. Wider O to P gaps mark the risks in Risk_Register.md and Feasibility_Study.md: the database (T3), role-based access (T5, risk R1), appeals logic (T9) and notifications (T11).

| ID | O | M | P | E = (O + 4M + P) / 6 |
| --- | --- | --- | --- | --- |
| T1 | 2 | 3 | 4 | (2 + 4x3 + 4) / 6 = 3 |
| T2 | 2 | 3 | 4 | (2 + 4x3 + 4) / 6 = 3 |
| T3 | 3 | 4 | 11 | (3 + 4x4 + 11) / 6 = 5 |
| T4 | 2 | 4 | 6 | (2 + 4x4 + 6) / 6 = 4 |
| T5 | 4 | 5 | 12 | (4 + 4x5 + 12) / 6 = 6 |
| T6 | 4 | 6 | 8 | (4 + 4x6 + 8) / 6 = 6 |
| T7 | 3 | 5 | 7 | (3 + 4x5 + 7) / 6 = 5 |
| T8 | 4 | 6 | 8 | (4 + 4x6 + 8) / 6 = 6 |
| T9 | 5 | 7 | 15 | (5 + 4x7 + 15) / 6 = 8 |
| T10 | 3 | 5 | 7 | (3 + 4x5 + 7) / 6 = 5 |
| T11 | 3 | 4 | 11 | (3 + 4x4 + 11) / 6 = 5 |
| T12 | 3 | 4 | 5 | (3 + 4x4 + 5) / 6 = 4 |
| T13 | 3 | 5 | 7 | (3 + 4x5 + 7) / 6 = 5 |
| T14 | 2 | 3 | 4 | (2 + 4x3 + 4) / 6 = 3 |
| T15 | 1 | 2 | 3 | (1 + 4x2 + 3) / 6 = 2 |
| T16 | 1 | 2 | 3 | (1 + 4x2 + 3) / 6 = 2 |

## Calendar mapping

Assumptions: project day 1 is Monday 12 Oct 2026; working days are Monday to Friday; no holidays are modelled (UAE National Day holidays in early December would add 1 to 2 days). Start date is the first working day of the task, finish date is the last.

| ID | Start day (ES) | Finish day (EF) | Start date | Finish date |
| --- | --- | --- | --- | --- |
| T1 | 0 | 3 | Mon 12 Oct 2026 | Wed 14 Oct 2026 |
| T2 | 3 | 6 | Thu 15 Oct 2026 | Mon 19 Oct 2026 |
| T3 | 3 | 8 | Thu 15 Oct 2026 | Wed 21 Oct 2026 |
| T4 | 3 | 7 | Thu 15 Oct 2026 | Tue 20 Oct 2026 |
| T5 | 8 | 14 | Thu 22 Oct 2026 | Thu 29 Oct 2026 |
| T6 | 14 | 20 | Fri 30 Oct 2026 | Fri 06 Nov 2026 |
| T7 | 20 | 25 | Mon 09 Nov 2026 | Fri 13 Nov 2026 |
| T8 | 14 | 20 | Fri 30 Oct 2026 | Fri 06 Nov 2026 |
| T9 | 20 | 28 | Mon 09 Nov 2026 | Wed 18 Nov 2026 |
| T10 | 20 | 25 | Mon 09 Nov 2026 | Fri 13 Nov 2026 |
| T11 | 28 | 33 | Thu 19 Nov 2026 | Wed 25 Nov 2026 |
| T12 | 33 | 37 | Thu 26 Nov 2026 | Tue 01 Dec 2026 |
| T13 | 37 | 42 | Wed 02 Dec 2026 | Tue 08 Dec 2026 |
| T14 | 37 | 40 | Wed 02 Dec 2026 | Fri 04 Dec 2026 |
| T15 | 42 | 44 | Wed 09 Dec 2026 | Thu 10 Dec 2026 |
| T16 | 44 | 46 | Fri 11 Dec 2026 | Mon 14 Dec 2026 |

Project finish: Mon 14 Dec 2026 (day 46).
