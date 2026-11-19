# Architectural Style Selection

## 1. Selected Style: Layered Architecture (three layers)

ParkAppeal uses a layered architecture with three layers: a Presentation Layer, a Business Logic Layer and a Foundation Layer. The database and the email service are external systems used by the lower layers. Each layer offers its services to the layer above through interfaces.

| Layer | Components | Role in ParkAppeal |
|---|---|---|
| Presentation Layer | CO1 User Interface | Pages and forms for the four roles on phones, tablets and computers. Validates input and shows results. |
| Business Logic Layer | CO2 Permit Management, CO3 Violation Management, CO4 Appeal Management, CO5 Search and Reporting | The rules of the system, one component per DFD process (1.0 to 4.0): eligibility and quota, violation recording, the 14-day appeal window, decisions, search and reports. |
| Foundation Layer | CO6 Accounts and Common Services | Services used by all business components: user accounts and roles (D1), authentication, notifications (Process 5.0) and the common Attachment base class for evidence files. |
| External systems | ParkAppeal Database, Email Service | Persistent storage of D1 to D4, and delivery of notification emails. |

## 2. Main Characteristics

- Components are grouped into ordered layers, and each layer has one kind of responsibility.
- A layer calls only the layers below it, through their provided interfaces. CO1 calls the Business Logic Layer, and calls the Foundation Layer directly only to log in (IAuthentication). Components of the same layer may call each other through interfaces (relaxed layering), for example CO4 reads violations from CO3.
- Lower layers never call higher layers. The user interface does not reach the database directly.
- Each component hides its classes behind its interfaces, so other components depend only on the operations listed in the interface.

## 3. Why It Is Appropriate for ParkAppeal

- ParkAppeal is a form and record based information system: users fill in forms, the system checks rules, stores records and sends notifications. This is the typical use of a layered architecture.
- The earlier models already separate these concerns. Lab 5 marks the user interface classes with <<UI>>, the Level-0 DFD (Lab 4) has five processes and four data stores, and the Lab 6 and Lab 7 diagrams show forms calling services and services calling entities. The layers follow the same split.
- The team members' slices of the requirements map to components: appeals (CO4), violations (CO3), permits (CO2), and search, notifications and the user interface (CO5, CO6, CO1). The slices can be built and tested in parallel.
- The system is small enough for one deployable application with one database. A distributed style such as microservices would add network calls and separate databases without a requirement that needs them.

## 4. Support for the Design Goals

| Goal | How the layered style supports it |
|---|---|
| DG-01 Security | Every request passes from CO1 through a business interface, where the role check is made before any change (canRecord for NFR-12, the Administrator check for NFR-16, the Appeals Officer check for NFR-02). The user interface has no direct access to the data. Login goes through IAuthentication (CO6), and CO1 ends the session after 15 minutes of inactivity (NFR-06). |
| DG-02 Reliability | Only the business components and CO6 write records, and each writes only its own data store (D1 to D4) in the persistent database, so records survive a restart (NFR-03, NFR-19). Each kind of record is written by one component, which keeps the audit trail (NFR-15) and the single-permit quota check (NFR-18) in one place. |
| DG-03 Maintainability | Each component is replaceable behind its interfaces. The user interface can change for phones and tablets (FR-06, FR-07, NFR-08) without changing the rules, and a slice can change its classes as long as its interface stays the same. |
| DG-04 Performance | Each frequent request is one interface call to one business component, which reads its own data store directly: lookUpVehicle (NFR-11), submitAppeal (NFR-01), getAppealsByHolder (NFR-05), decideApplication (NFR-17). The business layer holds no session state, so it can run as more than one instance if load grows. |

## 5. Advantages and Limitations

### Advantages

- Clear separation of concerns: user interface, rules and data are in different layers.
- Easy to test: each business component can be tested through its interface without the user interface.
- Easy to change the user interface or the storage without changing the rules.
- Matches the team's split of work and the earlier models, so the design is easy to follow.
- One place in each component to enforce security rules and log actions.

### Limitations

- Every request passes through more than one layer, which adds a small overhead to each call.
- Some requests only pass data through a layer without adding logic (for example listPending), which adds code without value.
- A change to a record, such as a new field, can reach all three layers.
- The whole application is deployed as one unit and uses one database, so it scales as a whole rather than per component, and the database is a single point of failure.
- Some CO6 operations name business classes in their signatures (for example PermitHolder.applyForPermit returns PermitApplication, and notifyViolationIssued takes a Violation). CO6 never calls a higher layer, since the role actions go through CO1 and the business interfaces, but these type references point upward. Passing identifiers instead would remove them.
