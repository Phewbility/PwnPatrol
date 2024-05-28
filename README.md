# PwnPatrol

PwnPatrol is a comprehensive analysis tool designed to perform various security analyses on executable files. It can display functions, assembly code, pseudo-code in C, trace library calls, and check security hardening.

## Features

- Display functions with their addresses.
- Show assembly code for specified functions.
- Show pseudo-code in C for specified functions.
- Trace library calls using `ltrace`.
- Run security checks using `checksec` and `hardening-check`.
- Perform full analysis with a single command.

## Installation

### Prerequisites

- `radare2`
- `Python 3`
- `pip`

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/PwnPatrol.git
   cd PwnPatrol
