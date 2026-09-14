# Software Process Model

## Selected Model

For the ParkAppeal project, the **Incremental Model** is the most appropriate software development lifecycle model.

ParkAppeal can be divided into several functional modules and developed through a series of working increments. Each increment will go through requirements analysis, design, implementation, and testing before being integrated into the complete system.

## Justification

The Incremental Model is appropriate for ParkAppeal because:

- The system has a clear core workflow, but some requirements may change after feedback from peers and administrators.
- Essential features can be delivered first, while reporting and other supporting features can be added later.
- Each increment provides a working version that the team can demonstrate and test.
- Developing smaller parts makes the project easier for a small student team to manage.
- Problems with important features, such as role-based access, document uploads, and appeal routing, can be identified before the complete system is developed.
- The course has a limited schedule, so completing the system in stages reduces the risk of reaching the deadline without a functional product.

## Overheads Drawbacks and Management Strategies

| Overhead or Drawback | Effect on ParkAppeal | Management Strategy |
| --- | --- | --- |
| Detailed initial planning | The team must define the system architecture, database relationships, module boundaries, and increment order before development begins. | The team will prepare a prioritized feature list, database design, and interface definitions before implementing the first increment. |
| Integration complexity | Later modules depend on earlier modules. For example, violations must connect correctly to users, vehicles, and permits. | The team will use a shared database schema, stable interfaces, version control, and continuous integration testing after every increment. |
| Repeated testing | Existing functions must be tested again whenever a new increment is added. This increases development time. | The team will create reusable test cases and perform regression testing after each integration. |
| Architectural problems may appear later | A weak design in the first increment could make later features, such as appeal routing and reporting, difficult to add. | The team will design the overall architecture and core data model before coding, even though features will be implemented incrementally. |
| Requirement changes may cause scope expansion | Feedback after each increment may introduce additional features that the team cannot finish within the course duration. | The team will prioritize required features and place nonessential requests in a future-work list. Changes will only enter the current increment if time permits. |
| Early versions are incomplete | The first increment will not represent the full ParkAppeal system and may have limited value by itself. | Each increment will remain functional and demonstrable, and stakeholders will receive a clear explanation of which features belong to later increments. |
