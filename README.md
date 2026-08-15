# Website Vulnerabilities Demo

A Django-based web application built to demonstrate common web application vulnerabilities and their corresponding mitigations, alongside a written report covering exploitation, remediation, and database encryption.

## Overview

This project demonstrates hands-on understanding of the OWASP Top 10-adjacent vulnerability classes below — both how they're exploited and how they're properly mitigated in a real application.

## Vulnerabilities Demonstrated

- **Cross-Site Scripting (XSS)** — [briefly describe the specific injection point/scenario you built, e.g. "reflected XSS via unsanitised search input"]
- **Cross-Site Request Forgery (CSRF)** — [briefly describe the scenario, e.g. "state-changing form submission without CSRF token validation"]
- **SQL Injection (SQLi)** — [briefly describe, e.g. "login form vulnerable to authentication bypass via crafted SQL input"]
- **Command Injection** — [briefly describe, e.g. "unsanitised user input passed to a system shell command"]

## Mitigations Implemented

For each vulnerability above, the project also implements and documents the corresponding fix — including input sanitisation, parameterised queries, CSRF token enforcement, and output encoding, following Django's built-in security best practices.

## Additional: Database Encryption

[Briefly describe what you implemented here — e.g. "Sensitive fields in the database are encrypted at rest using [method/library], demonstrating defence-in-depth beyond input validation alone."]

## Tech Stack

- Python / Django
- [Add database used, e.g. SQLite/PostgreSQL]
- [Add any other libraries/tools used]

## Written Report

A full write-up accompanying this project covers the exploitation methodology, mitigation strategy, and encryption approach for each vulnerability in detail. [Link to the report here, or note it's included in the repo as `/report.pdf` or similar.]

## Running Locally

```bash
git clone https://github.com/RajanBharaj/website-vulnerabilities-demo.git
cd website-vulnerabilities-demo
pip install -r requirements.txt
python manage.py runserver
```

[Adjust the above to match your actual setup steps.]

## Context

Originally developed as part of NYU's Application Security coursework and independently extended. [Add a sentence here on what you personally built or extended beyond the assignment baseline, so it's clear what's your own work.]

## Disclaimer

This project is intentionally vulnerable and intended strictly for educational purposes. Do not deploy in a production environment.
