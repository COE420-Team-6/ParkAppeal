# Component Descriptions

ParkAppeal is decomposed into six components in three layers. The component diagram is in `Component_Diagram/Software_Architecture_Component_Diagram.pdf` (native draw.io file `Software_Architecture_Component_Diagram.drawio`).

## 1. Components

| ID | Component Name | Layer | Responsibilities | Supported Functionality | DFD Process or Data Store |
|---|---|---|---|---|---|
| CO1 | User Interface | Presentation | Shows the pages and forms for the four roles on phones, tablets and computers. Logs users in and out (15-minute inactivity logout). Validates forms before submission, shows success and error messages, and passes each user action to the business component that handles it. | User access to every use case (UC-01 to UC-20). FR-06, FR-07, NFR-06, NFR-08, NFR-10. | User interface to Processes 1.0 to 5.0 |
| CO2 | Permit Management | Business Logic | Accepts permit applications with documents, evaluates them against the eligibility criteria of the permit type, and lets the Administrator approve or reject them. Issues and renews permits within the quota (one permit per approved application), tracks validity and expiry, configures eligibility criteria and quotas, and gives the permit status of a vehicle to Violation Management. | UC-06, UC-07, UC-08, UC-16, UC-17, UC-18, UC-19, UC-20. FR-08, FR-16 to FR-20, NFR-16 to NFR-19. | Process 1.0, D2 (and vehicles in D1) |
| CO3 | Violation Management | Business Logic | Looks up vehicles by licence plate and shows their permit status. Records violations with type, location and issue time, only for Parking Officer or Administrator accounts, and attaches up to 5 photographs. Marks unmatched plates for review and links them to vehicles later. Voids violations with a reason while keeping the original record and the audit trail, and gives violation records to Appeal Management. | UC-11, UC-12, UC-13, UC-14, UC-15. FR-11 to FR-15, NFR-11 to NFR-15. | Process 2.0, D3 |
| CO4 | Appeal Management | Business Logic | Accepts appeals within 14 days of the issue date with a reason and up to 3 files, after verifying the violation record. Tracks appeal status for the Permit Holder, lets Appeals Officers review an appeal and record a decision with a justification, and voids the violation when an appeal is approved. | UC-01, UC-02, UC-03, UC-04, UC-05. FR-01 to FR-05, NFR-01 to NFR-05. | Process 3.0, D4 |
| CO5 | Search and Reporting | Business Logic | Searches and filters permits, violations and appeals by status or date for the Administrator, and generates reports for a date range. Reads the permit, violation and appeal records without changing them. | UC-09. FR-09. | Process 4.0, reads D2 to D4 |
| CO6 | Accounts and Common Services | Foundation | Stores user accounts and their roles (D1) and authenticates users. Supplies the account and role that the business components check before an action. Sends the submission confirmation and the status change notifications to permit holders by email. Defines the common Attachment base class that validates the type and size of evidence files. | Login for all use cases, UC-10. FR-10, the confirmation email of FR-01, role checks for NFR-02, NFR-12 and NFR-16, file checks for FR-01 and FR-13. | Process 5.0, D1 |

## 2. Provided and Required Interfaces

Provided interfaces are drawn as lollipops (balls) and required interfaces as sockets. Each provided interface is also drawn with its operations and a realization arrow from its component.

| ID | Component Name | Provided Interfaces | Required Interfaces |
|---|---|---|---|
| CO1 | User Interface | None | IAuthentication, IPermitManagement, IViolationManagement, IAppealManagement, IReporting |
| CO2 | Permit Management | IPermitManagement, IVehicleStatus | INotification |
| CO3 | Violation Management | IViolationManagement, IViolationRecords | IVehicleStatus, INotification |
| CO4 | Appeal Management | IAppealManagement | IViolationRecords, INotification |
| CO5 | Search and Reporting | IReporting | None (Database only) |
| CO6 | Accounts and Common Services | IAuthentication, INotification | Email Service (external) |

## 3. Interface Definitions

Each operation is an operation of a class in the providing component (Lab 5 class diagram), with the same parameters and return type.

### IAuthentication

Provided by CO6 Accounts and Common Services. Required by CO1 User Interface.

| Operation | Class |
|---|---|
| `authenticate(password : String) : boolean` | User |

### IPermitManagement

Provided by CO2 Permit Management. Required by CO1 User Interface.

| Operation | Class |
|---|---|
| `submitApplication(holderId : String, vehicleId : String, typeId : String, documents : List<File>) : PermitApplication` | PermitService |
| `renewPermit(permitId : String) : Permit` | PermitService |
| `listPending() : List<PermitApplication>` | PermitService |
| `reviewEligibility(applicationId : String) : PermitApplication` | PermitService |
| `decideApplication(applicationId : String, approve : boolean) : void` | PermitService |
| `listByStatus(status : PermitStatus) : List<Permit>` | PermitService |
| `configureEligibility(typeId : String, criteria : String) : void` | PermitService |
| `setQuota(typeId : String, quota : int) : void` | PermitService |

### IVehicleStatus

Provided by CO2 Permit Management. Required by CO3 Violation Management.

| Operation | Class |
|---|---|
| `getActivePermit() : Permit` | Vehicle |
| `isValid() : boolean` | Permit |

### IViolationManagement

Provided by CO3 Violation Management. Required by CO1 User Interface.

| Operation | Class |
|---|---|
| `lookUpVehicle(plate : String) : Vehicle` | ViolationService |
| `recordViolation(officerId : String, plate : String, type : ViolationType, location : String) : Violation` | ViolationService |
| `attachEvidence(violationId : String, photo : ViolationEvidence) : void` | ViolationService |
| `listUnmatched() : List<Violation>` | ViolationService |
| `linkToVehicle(violationId : String, vehicleId : String) : void` | ViolationService |
| `voidViolation(violationId : String, actorId : String, reason : String) : VoidRecord` | ViolationService |

### IViolationRecords

Provided by CO3 Violation Management. Required by CO4 Appeal Management.

| Operation | Class |
|---|---|
| `getViolation(violationId : String) : Violation` | ViolationService |
| `getIssuedAt() : Date` | Violation |
| `voidViolation(violationId : String, actorId : String, reason : String) : VoidRecord` | ViolationService |

### IAppealManagement

Provided by CO4 Appeal Management. Required by CO1 User Interface.

| Operation | Class |
|---|---|
| `submitAppeal(holderId : String, violationId : String, reason : String, files : List<AppealEvidence>) : Appeal` | AppealService |
| `getAppealsByHolder(holderId : String) : List<Appeal>` | AppealService |
| `getStatus() : AppealStatus` | Appeal |
| `reviewAppeal(appealId : String) : Appeal` | AppealService |
| `recordDecision(appealId : String, officerId : String, outcome : DecisionOutcome, justification : String) : Decision` | AppealService |

### IReporting

Provided by CO5 Search and Reporting. Required by CO1 User Interface.

| Operation | Class |
|---|---|
| `searchPermits(filter : SearchFilter) : List<Permit>` | ReportService |
| `searchViolations(filter : SearchFilter) : List<Violation>` | ReportService |
| `searchAppeals(filter : SearchFilter) : List<Appeal>` | ReportService |
| `generateReport(reportType : String, startDate : Date, endDate : Date) : String` | ReportService |

### INotification

Provided by CO6 Accounts and Common Services. Required by CO2 Permit Management, CO3 Violation Management, CO4 Appeal Management.

| Operation | Class |
|---|---|
| `sendSubmissionConfirmation(appeal : Appeal) : void` | NotificationService |
| `notifyAppealStatusChange(appeal : Appeal) : void` | NotificationService |
| `notifyViolationIssued(violation : Violation) : void` | NotificationService |
| `notifyPermitStatusChange(application : PermitApplication) : void` | NotificationService |

## 4. Role Operations

The role classes in CO6 (Lab 5) model the actions each actor may perform. At run time each action is carried out by CO1 through a business interface, so CO6 never calls a higher layer.

| Role Operation (Lab 5) | Carried Out Through |
|---|---|
| PermitHolder.applyForPermit | IPermitManagement.submitApplication |
| PermitHolder.submitAppeal | IAppealManagement.submitAppeal |
| PermitHolder.renewPermit | IPermitManagement.renewPermit |
| PermitHolder.viewAppealStatus | IAppealManagement.getAppealsByHolder, getStatus |
| AppealsOfficer.reviewAppeal | IAppealManagement.reviewAppeal |
| AppealsOfficer.recordDecision | IAppealManagement.recordDecision |
| ParkingOfficer.lookUpPlate | IViolationManagement.lookUpVehicle |
| ParkingOfficer.issueViolation | IViolationManagement.recordViolation |
| Administrator.decideApplication | IPermitManagement.decideApplication |
| Administrator.configureEligibility | IPermitManagement.configureEligibility |
| Administrator.setQuota | IPermitManagement.setQuota |
| Administrator.linkToVehicle | IViolationManagement.linkToVehicle |
| Administrator.voidViolation | IViolationManagement.voidViolation |

## 5. External Systems

| External System | Use |
|---|---|
| ParkAppeal Database | Persistent storage of D1 User and Vehicle Registry, D2 Permit Records, D3 Violation Records and D4 Appeal Records. Used by CO2 to CO6. |
| Email Service | Delivers the notification and confirmation emails sent by NotificationService (CO6). |

## 6. Class Model Updates

The following operations were added to the Lab 5 consolidated class diagram (`Project/Object_Modeling/Class_Diagram.puml`) so that every role operation has an interface operation.

| Operation | Class | Interface | Reason |
|---|---|---|---|
| `configureEligibility(typeId : String, criteria : String) : void` | PermitService | IPermitManagement | UC-16 and FR-16. Administrator.configureEligibility had no service operation to carry it out. |
| `setQuota(typeId : String, quota : int) : void` | PermitService | IPermitManagement | UC-17 and FR-17. Administrator.setQuota had no service operation to carry it out. |
| `linkToVehicle(violationId : String, vehicleId : String) : void` | ViolationService | IViolationManagement | UC-14 and FR-14. Administrator.linkToVehicle had no service operation to carry it out. |
| `reviewAppeal(appealId : String) : Appeal` | AppealService | IAppealManagement | UC-04 and FR-04. AppealsOfficer.reviewAppeal had no service operation to carry it out. |

## 7. Architecture Review

| # | Review Question | Result | Evidence |
|---|---|---|---|
| 1 | Are at least four and no more than six components identified? | Yes | Six components: CO1 in the Presentation Layer, CO2 to CO5 in the Business Logic Layer and CO6 in the Foundation Layer. |
| 2 | Are all classes from Lab 5 assigned to components? | Yes | All 31 classes of the consolidated class diagram are assigned, each to exactly one component (4, 7, 5, 6, 2 and 7 classes). The diagram shows each class inside its component. |
| 3 | Does each component have clearly defined responsibilities? | Yes | Each component has its responsibilities, use cases, requirements and DFD process or data store listed in Component_Descriptions.md. No use case is handled by two components. |
| 4 | Are the provided and required interfaces correctly represented? | Yes | 8 provided interfaces are shown as lollipops on their components and 10 required interfaces as sockets connected to them, plus the SMTP interface of the Email Service required by CO6. Each interface is also shown with its operations and a realization arrow from its component. |
| 5 | Are interface operations consistent with the assigned classes? | Yes | Each of the 33 interface operations is an operation of a class in the providing component, with the same parameters and return type. 4 operations were added to the class diagram for role actions that had no service operation (Class Model Updates). |
| 6 | Does the architecture support the requirements and use cases from Lab 3? | Yes | Every use case UC-01 to UC-20 is handled by one component and reached from CO1 through an interface. The components cover FR-01 to FR-20, and the four design goals trace to 14 of the 20 NFRs. |
| 7 | Is the architecture consistent with the Sequence Diagrams from Lab 6 and Activity Diagrams from Lab 7? | Yes | All 8 messages between lifelines of different components in the Lab 6 diagrams are operations of a declared interface: submitAppeal (IAppealManagement), getViolation and getIssuedAt (IViolationRecords), getActivePermit (IVehicleStatus) and the notifications (INotification). The Lab 7 swimlanes map to CO1, CO2, CO3, CO4 and CO6, and the 4 actions that use a class of another component go through IAppealManagement, IViolationRecords or IVehicleStatus. |
