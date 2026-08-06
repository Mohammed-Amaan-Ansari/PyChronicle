# PyChronicle

 > **Time-Travel Debugging for Python Applications**

PyChronicle is an AST-powered execution tracer that records the state of every variable during program execution. Instead of repeatedly rerunning your application and adding print statements, PyChronicle lets you move backward and forward through execution history to inspect exactly how your program reached its current state.

##  Features

- Trace Python program execution line-by-line
- Record variable state changes (delta tracking)
- Parse source code using Python AST
- Lightweight execution tracing with `sys.settrace`
- Fast in-memory SQLite storage
- Interactive Terminal UI built with Textual
-  Time-travel through program execution
- Inspect historical variable values
- Zero modification required to target programs


##  Architecture

Python Script
      │
      ▼
 AST Parser
      │
      ▼
Execution Tracer
(sys.settrace)
      │
      ▼
State Recorder
      │
      ▼
SQLite Database
      │
      ▼
Textual Timeline UI

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.11+ |
| Parsing | ast |
| Execution Tracing | sys.settrace |
| Database | SQLite |
| Serialization | pickle |
| Terminal UI | Textual |
| Packaging | Poetry / pip |


## Installation Process of Pychronicla
```bash
pip install -e .
```

## Run a Script

```bash
pychronicle run examples/final_demo.py
```

## Launch the UI

```bash
pychronicle ui
```