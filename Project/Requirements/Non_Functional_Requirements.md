# Non-Functional Requirements

## Mohamad Al Kadi (B00098738) Contributions

- NFR-01
- NFR-02
- NFR-03
- NFR-04
- NFR-05

## Mehlam Muniwala (B00104714) Contributions

- NFR-06
- NFR-07
- NFR-08
- NFR-09
- NFR-10

## Jad Zeidan (B00088013) Contributions

- NFR-11
- NFR-12
- NFR-13
- NFR-14
- NFR-15

## Seyed Moshtagh Moulaei (B00106497) Contributions

- NFR-16
- NFR-17
- NFR-18
- NFR-19
- NFR-20

## Team Consolidated Requirements

| NFR ID | Category | Non-Functional Requirement | Contributor |
| --- | --- | --- | --- |
| NFR-01 | Performance | The appeal submission form should load within 3 seconds for 95% of users at 200 concurrent users. | Mohamad Al Kadi |
| NFR-02 | Security | The system should restrict appeal review and decision actions to authenticated appeals officers and appeals committee members, and log every decision with a timestamp and user ID. | Mohamad Al Kadi |
| NFR-03 | Reliability | The system should retain a submitted appeal and its attachments even after a server restart, maintaining at least 99.5% uptime per month. | Mohamad Al Kadi |
| NFR-04 | Usability | The system should retain a submitted appeal and its attachments even after a server restart, maintaining at least 99.5% uptime per month. | Mohamad Al Kadi |
| NFR-05 | Scalability | The appeals queue should support at least 1,000 pending appeals and 50 concurrent officer reviews without dashboard load times exceeding 2 seconds. | Mohamad Al Kadi |
| NFR-06 | Security | The system should automatically log out a user after 15 minutes of inactivity. | Mehlam Muniwala |
| NFR-07 | Usability | A new user should be able to complete a parking permit application in less than 5 minutes. | Mehlam Muniwala |
| NFR-08 | Portability | ParkAppeal shall work correctly on Chrome, Safari, and Edge on both desktop and mobile devices. | Mehlam Muniwala |
| NFR-09 | Reliability | The system shall save submitted permit applications and appeals without losing user-entered information. | Mehlam Muniwala |
| NFR-10 | Usability | The system shall display clear success or error messages after users submit forms or perform actions. | Mehlam Muniwala |
| NFR-11 | Performance | A licence plate lookup shall return a result within 2 seconds for a database of up to 10,000 registered vehicles over a standard campus network connection. | Jad Zeidan |
| NFR-12 | Security | The system shall permit the creation of violation records only to accounts holding the parking officer or administrator role, and shall reject and log any attempt made by another role. | Jad Zeidan |
| NFR-13 | Usability | A trained parking officer shall be able to complete a violation record, from plate lookup to submission, in a few input actions and within two minutes. | Jad Zeidan |
| NFR-14 | Robustness | If an evidence image upload fails or is interrupted, the system shall retain the entered violation details and allow the officer to retry the upload without re-entering the record. | Jad Zeidan |
| NFR-15 | Reliability | Every violation record shall be recorded with an audit trail capturing its creation, the identity of the acting user, and the time of each action. | Jad Zeidan |
| NFR-16 | Security | The server shall reject permit rule, quota, and issuance requests from accounts without the administrator role, even if a valid record identifier is supplied directly. | Seyed Moshtagh Moulaei |
| NFR-17 | Performance | With 1,000 permit applications in the test database and 20 concurrent users, at least 95% of approved-permit issuance requests shall complete within two seconds in the team's documented test environment. | Seyed Moshtagh Moulaei |
| NFR-18 | Data Integrity | When two administrators act concurrently on the last available quota slot, at most one permit shall be issued, and an approved application shall have no more than one issued permit. | Seyed Moshtagh Moulaei |
| NFR-19 | Reliability | After a server restart, every successfully issued permit shall retain its number, owner, vehicle, dates, and current validity state in persistent storage. | Seyed Moshtagh Moulaei |
| NFR-20 | Usability | In a moderated test with five administrators trained on the prototype, at least four shall locate an approved application and issue its permit without assistance within two minutes. | Seyed Moshtagh Moulaei |
