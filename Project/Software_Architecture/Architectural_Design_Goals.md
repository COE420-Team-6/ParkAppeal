# Architectural Design Goals

The ParkAppeal architecture is designed around four goals taken from the Lab 3 requirements. Exercise 2 (Architectural_Style_Selection.md) explains how the selected style supports each goal.

| Goal ID | Design Goal | Description | Related Requirement | Priority | Justification |
|---|---|---|---|---|---|
| DG-01 | Security | Only authenticated users reach the system, and each business operation checks the role of the caller before it changes a record. | NFR-02, NFR-06, NFR-12, NFR-16 | High | Violations, appeal decisions, permit rules and quotas carry fines and parking rights. A wrong role must not be able to create or decide them, even by calling an operation directly. |
| DG-02 | Reliability | Every submitted application, issued permit, violation, appeal and decision is stored persistently and is never lost or silently changed. | NFR-03, NFR-09, NFR-15, NFR-18, NFR-19 | High | These records are the evidence in a dispute. They must survive a server restart, keep an audit trail and stay correct when two administrators act on the last quota slot. |
| DG-03 | Maintainability | Each functional area (permits, violations, appeals, search) is a separate component behind an interface, so it can be changed or tested without changing the others. | FR-01 to FR-20 (four slices), FR-06, FR-07, NFR-08 | High | Four team members each own a slice of the requirements, and the user interface must change for phones, tablets and computers without changing the business rules. |
| DG-04 | Performance | Frequent requests (plate lookup, appeal form, appeals dashboard, permit issuance) reach the data they need in few calls and return within the stated limits. | NFR-01, NFR-05, NFR-11, NFR-17 | Medium | Officers look up plates during patrol, and permit holders and officers use the forms at peak times. The limits are 2 to 3 seconds. |
