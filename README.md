# Sentinel Log Analyzer

A beginner Python project that analyzes login event records and counts failed logins, successful logins, and unknown events.

## Features

- Counts failed login attempts (`LOGIN_FAILED`)
- Counts successful logins (`LOGIN_SUCCESS`)
- Tracks unrecognized events
- Calculates the total number of records
- Displays an alert when failed logins reach three or more

## Technologies

- Python 3
- Dictionaries
- Conditional statements (`if`, `elif`, `else`)
- Loops (`for`)
- Basic counting and data analysis

## Example output

```text
Falhas: 3
Sucessos: 2
Desconhecidos: 0
Total de registros: 5
ALERTA: muitas falhas de login
```

## Current limitations

This initial version processes a list of log records defined directly in the source code. It does not yet read log files.

## Learning goals

This project is part of my journey learning Python and cybersecurity. Future improvements may include reading log files, handling additional event types, and generating more detailed reports.
