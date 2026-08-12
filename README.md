# PyChronicle

**AST-Powered Time-Travel Debugger for Python**

PyChronicle is an experimental Python debugging framework that records program execution history using **AST instrumentation**, **runtime tracing**, **delta-compressed state storage**, and an **interactive Textual terminal UI**.

---

## 🚀 Features

* AST-based instrumentation
* Runtime execution tracing using `sys.settrace()`
* SQLite-backed trace persistence
* Delta-compressed variable storage
* Full state reconstruction
* Interactive Textual debugger UI
* Timeline navigation
* Watch variables panel
* JSON and CSV export
* Trace analytics and statistics
* Advanced trace search and filtering
* Session management
* Interactive replay with breakpoint support

---

## 📦 Installation

```bash
Copy the Git Link : git clone https://github.com/your-username/PyChronicle.git
cd PyChronicle
pip install -e .
```

---

## ▶️ Quick Start

### Run a Script Under Tracing

```bash
pychronicle run examples/final_demo.py
```

### Launch the Interactive UI

```bash
pychronicle ui
```

### View Statistics

```bash
pychronicle stats
```

### Search Trace Records

```bash
pychronicle search --function calculate_total
pychronicle search --event return
pychronicle search --line 8
```

### Export Trace

```bash
pychronicle export trace_report.json
pychronicle export-csv trace_report.csv
```

### Replay Execution

```bash
x
```

---

## 🏗️ Architecture

```text
Target Python Script
        │
        ▼
AST Instrumentation
        │
        ▼
Runtime Tracer (sys.settrace)
        │
        ▼
Delta Compressor
        │
        ▼
SQLite Storage
        │
        ├── Analytics Engine
        ├── Search Engine
        ├── Replay Engine
        └── Textual UI
```

---

## 🧠 Technologies Used

* **Python 3.10+**
* **Textual**
* **Typer**
* **SQLite3**
* **AST module**
* **sys.settrace**

---

## 📚 Educational Value

PyChronicle demonstrates advanced Python concepts including:

* Abstract Syntax Trees
* Metaprogramming
* Runtime introspection
* Execution tracing
* Delta compression
* State reconstruction
* Terminal UI development
* CLI application packaging

---
 