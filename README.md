# Website Vulnerabilities Demo

A Django-based web application built to demonstrate common web application vulnerabilities and their corresponding mitigations, alongside a written report covering exploitation, remediation, and database encryption.

## Overview

This project demonstrates hands-on understanding of the OWASP Top 10-adjacent vulnerability classes below — both how they're exploited and how they're properly mitigated in a real application.

## Vulnerabilities Demonstrated

- **Cross-Site Scripting (XSS)**
- **Cross-Site Request Forgery (CSRF)** 
- **SQL Injection (SQLi)**
- **Command Injection**

## Mitigations Implemented

For each vulnerability above, the project also implements and documents the corresponding fix — including input sanitisation, parameterised queries, CSRF token enforcement, and output encoding, following Django's built-in security best practices.

## Tech Stack

- Python / Django

## Written Report

Please see the "testing.txt" documentation for further explanation.

## Running Locally

```bash
git clone https://github.com/RajanBharaj/website-vulnerabilities-demo.git
cd website-vulnerabilities-demo
pip install -r requirements.txt
python manage.py runserver
```

## Context

Originally developed as part of NYU's Application Security coursework and independently extended. The "HW2_Instructions.md" and "testing.txt" documents give context to the work independently completed. 

## Disclaimer

This project is intentionally vulnerable and intended strictly for educational purposes. Do not deploy in a production environment.
