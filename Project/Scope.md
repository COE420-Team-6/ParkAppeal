**Project Scope — ParkAppeal**
Parking Permit Issuance and Violation Appeal System

## 1. Project Objective
The objective of ParkAppeal is to build a single web-based system that handles
parking permit issuance and parking violation appeals for a university campus,
using AUS as the reference case.

At present these processes are handled through paper forms, email threads, and
spreadsheets. This creates three problems: applicants cannot see the status of a
permit request or an appeal, staff re-enter the same information manually more
than once, and appeals are difficult to trace from submission to final decision.

ParkAppeal addresses this by putting permit applications, permit records,
violation records, and appeals into one system with role-based access, a defined
appeal review workflow, and status tracking visible to the applicant.

**2. Target Users**
**Applicants**: (students, staff, visitors) Apply for and renew permits, view their violations, file appeals, and track the status of each request.
**Parking officers / campus security**: Record violations against a vehicle and permit, and attach supporting evidence.
**Administrators**: Set permit quotas and eligibility rules, approve or reject permit applications, review appeals, record decisions, and generate reports.
The development team is a stakeholder in the project but is not a user of the delivered system.

**3. In-Scope Features**
**Accounts and access**
- Account registration and login.
- Role-based access control for applicants, officers, and administrators.

**Permits**
- Online permit application with document upload and eligibility checking.
- Permit issuance, renewal, and expiry tracking.
- Administrator review of applications: approve or reject with a reason.

**Violations**
- Recording a violation and linking it to a registered vehicle and permit.
- Attaching evidence to a violation record.

**Appeals**
- Appeal submission within a defined time window after the violation.
- Upload of supporting evidence with the appeal.
- Routing an appeal to a reviewer, recording the decision and its justification, and notifying the applicant.

**Tracking and reporting**
- Status tracking for applicants across permits, violations, and appeals.
- In-app and email notifications on status changes.
- Searching and filtering permits, violations, and appeals by date, status, or user.
- Administrative dashboard.
- Reports on permits issued, violations recorded, and appeal outcomes.

**4. Out-of-Scope Features**
- **Online payment.** Fine payment and permit fee collection are not handled, the system records amounts only.
- **Integration with live university systems.** No connection to Banner, the AUS identity provider, or any live student record system. 
  User and vehicle data will be seeded test data.
- **Hardware integration.** No licence plate recognition cameras, barrier gates, RFID readers, handheld ticketing devices, or live parking space availability.
- **Native mobile applications.** The system is a responsive web application only.
- **SMS and push notifications.** Notifications are limited to in-app and email.
- **Escalation beyond the system.** Formal or legal escalation after the final in-system appeal decision is outside the workflow.
- **Multi-campus or multi-tenant deployment.** The system is designed for a single institution.
- **Production deployment and operations.** Live hosting, real user data, backups, and ongoing maintenance are not part of the course deliverable.

**5. Major Deliverables**
Deliverables might be adjusted as time goes on and more information about the porject is obtained.
Project definition documents in the repository: `Project_Title.md` and `Project_Description.md`.
Project planning artifacts: `Scope.md`, `Process_Model.md`, `Risk_Register.md`, `Stakeholders.md`, and `Feasibility_Study.md`.
Team documentation carried forward from Lab 1: `Team_Members.md`, `Skills.md`, `Contact_Information.md`, and member CVs.
A written report for each lab, including team member names and AUS IDs, responses to each exercise, and a link to the repository.
A maintained GitHub repository following the required structure, with meaningful commit messages and clear evidence of each member's individual contribution.

**6. Assumptions and Constraints**
- The team may not obtain direct access to the campus parking office. Where that is the case, permit rules, violation categories, and appeal deadlines
  will be based on publicly available campus parking regulations (see R5 in the risk register).
- All data used for development and demonstration is test data. No real personal or vehicle data is used.
- The project is carried out as an analysis and design exercise. Implementing, deploying, and operating a working system is not among the expected project
  deliverables, so the features in Section 3 define what the system is specified to do rather than what will be built during the course.
- The project must be completed within the duration of the course, so feature priority follows the order listed in Section 3.
- The scope defined here is the initial scope and may be refined in later phases as requirements are elicited.