Here is the complete Class 12 Computer Science Investigatory Project Report based on your project (**Solo Leveling Military Management System v2.0 / Shadow Military Protocol**) and styled after the reference PDF layout.

As requested, the first three pages (Title Page, Bonafide Certificate, and Acknowledgement) have been **omitted**, and no sample command-line outputs have been generated so you can run the code and insert your own screenshots.

## 📌 Jupyter Notebook Structure & Markdown Setup Guide

To create a clean, professional HTML export from Jupyter Notebook:

### 1. Where to Place Markdown Boxes

In Jupyter Notebook, click on a cell, press `Esc`, then press `M` to change the cell type to **Markdown**. Insert a Markdown cell **before each major section and before every key function block**.

#### Recommended Cell Architecture:

- **Cell 1 (Markdown):** Index & Project Introduction
    
- **Cell 2 (Markdown):** System Requirements & Database Architecture
    
- **Cell 3 (Markdown):** Section Header: `## 1. System Setup & Database Layer`
    
- **Cell 4 (Code):** Imports, Database Configuration, Index Constants
    
- **Cell 5 (Markdown):** Function Header Box: `### 🔹 Module: Authentication Protocol`
    
- **Cell 6 (Code):** `auth()` function definition
    
- **Cell 7 (Markdown):** Function Header Box: `### 🔹 Module: Soldier Command Center`
    
- **Cell 8 (Code):** `soldier_menu()`, `order_weapons()`, `update_health_status()`, etc.
    
- **Cell 9 (Markdown):** Function Header Box: `### 🔹 Module: Captain Command Center`
    
- **Cell 10 (Code):** `captain_menu()`, `approve_weapon_orders()`, `view_system_stats()`, etc.
    
- **Cell 11 (Markdown):** Section Header: `## 2. Program Execution & Output Screenshots`
    
- **Cell 12 (Code):** Program entry point execution (`setup_database()`, `auth()`, main menu loop)
    
- **Cell 13 (Markdown):** Project Conclusion & Bibliography
    

### 2. How to Format Function Documentation & Outputs

#### A. Making Functions Stand Out (Styling Markdown Cells)

Use HTML Alert Boxes in Markdown cells right above each function:

HTML

```
<div style="background-color: #f0f4f8; border-left: 5px solid #2b6cb0; padding: 12px; margin: 10px 0; border-radius: 4px;">
    <h3 style="margin: 0; color: #2b6cb0;">⚙️ Function: <code>auth()</code></h3>
    <p style="margin: 5px 0 0 0; color: #4a5568;"><b>Purpose:</b> Multi-role identity verification system supporting Captain (Monarch) and Soldier access tiers with credential lookup.</p>
</div>
```

#### B. Making Code Cells Reader-Friendly

- **Docstrings:** Place a triple-quoted docstring under every `def function_name():`.
    
- **Section Dividers:** Keep long code blocks visually structured using commented rule lines (`# ═════════...`).
    

#### C. Formatting the Output Cell in Jupyter

When you run your program in Jupyter, output text can look plain. To make it visually clear:

1. **Clear Output before Exporting:** Go to `Cell -> All Output -> Clear` before your final execution run so old errors or test runs aren't exported.
    
2. **Standard Output Formatting:** Ensure rich Unicode banners (like the ones in your script: `🗡️`, `👑`, `⚔️`) display properly by ensuring Jupyter's output encoding is UTF-8.
    
3. **Exporting:** Navigate to `File -> Save and Export Notebook As... -> HTML` (or run `jupyter nbconvert --to html notebook.ipynb` in terminal).
    

# 📖 PROJECT REPORT DOCUMENTATION

_(Copy and paste the text below directly into your Jupyter Notebook Markdown cells or Word/LaTeX editor)_

## INDEX

| **Sl. No.** | **Topic**                            |
| ----------- | ------------------------------------ |
| 1           | Introduction to Python and SQL       |
| 2           | About the Project                    |
| 3           | Hardware and Software Specifications |
| 4           | Database Schema & SQL Architecture   |
| 5           | Source Code                          |
| 6           | Execution & Output Documentation     |
| 7           | Conclusion                           |
| 8           | Bibliography                         |

## INTRODUCTION TO PYTHON AND SQL

### Python

Python is a widely used high-level, interpreted programming language created by Guido van Rossum in 1991. It emphasizes code readability and logical simplicity, enabling developers to build complex applications using clean, concise syntax.

**Key Applications:**

- Web and Software Development
    
- Database Integration and API Management
    
- Data Analytics and Statistical Computations
    
- Automated CLI Systems and Scripting
    

**Features of Python:**

- **Easy to Learn & Read:** Object-oriented architecture with straightforward syntax rules.
    
- **Interpreted Language:** Code executes line-by-line, simplifying debugging.
    
- **Cross-Platform Compatibility:** Runs seamlessly across Windows, Linux, and macOS platforms.
    
- **Extensive Ecosystem:** Rich built-in standard libraries (`statistics`, `math`, `datetime`) and third-party database drivers (`mysql-connector-python`).
    

### SQL (Structured Query Language)

SQL is the standard query language utilized for creating, manipulating, and querying Relational Database Management Systems (RDBMS).

**Key Applications:**

- Managing structured datasets across primary and foreign key constraints.
    
- Executing CRUD (Create, Read, Update, Delete) operations.
    
- Ensuring data integrity, persistence, and transactional reliability (ACID compliance).
    

**Integration in this Project:** In this project, Python serves as the front-end application logic controller, while MySQL serves as the robust back-end relational database. Communication between the two layers is handled via the `mysql.connector` interface.

## ABOUT THE PROJECT

### Title: Solo Leveling Military Management System v2.0 (Shadow Military Protocol)

The **Shadow Military Protocol** is an enterprise-grade administrative and tactical management system modeled after advanced command-and-control software architectures. It bridges tactical field metrics with centralized relational database storage to manage elite units, armory inventory, mission assignments, and combat readiness metrics.

### Key Objectives & Functionalities

1. **Role-Based Authentication Security:**
    
    - **Monarch / Captain Tier:** Full administrative access for personnel oversight, inventory procurement, requisition approvals, and system analytics.
        
    - **Shadow Soldier Tier:** Restricted access to personal combat stats, task updates, health monitoring, and weapon requisitions.
        
2. **Arsenal & Logistics Management:**
    
    - Multi-categorical inventory tracking covering Assault Rifles, Battle Rifles, LMGs, Snipers, Pistols, Shotguns, SMGs, Explosives, Ammunition, and Accessories.
        
    - Requisition order workflow with approval/rejection overrides by Captains.
        
3. **Combat Readiness & Health Analytics:**
    
    - Real-time monitoring of HP, Mana, combat ranks (S-Rank through E-Rank), and field statuses (Active, Injured, Recovering, Critical).
        
    - Automated calculation of military readiness averages using standard deviation and mean calculations via Python’s `statistics` module.
        
4. **Dynamic Mission Deployment:**
    
    - Assignment of S-Rank through C-Rank combat quests with priority filtering and status progress tracking.
        
5. **MySQL Database Persistence:**
    
    - Automatic schema initialization, automated table creation, and state synchronization between Python memory lists and MySQL tables (`shadow_army_db`).
        

## HARDWARE AND SOFTWARE SPECIFICATIONS

### Hardware Requirements

- **Processor:** x86/x64 Dual-Core CPU @ 2.0 GHz or higher (Intel Core / AMD Ryzen)
    
- **RAM:** 4 GB minimum (8 GB recommended)
    
- **Disk Space:** 500 MB available storage for database tables and application runtime logs
    
- **Input Devices:** Standard Keyboard and Mouse/Trackball
    

### Software Requirements

- **Operating System:** Windows 10/11, macOS, or Linux (Debian/Ubuntu)
    
- **Environment:** Jupyter Notebook / JupyterLab or VS Code
    
- **Python Runtime:** Python v3.9+ (64-bit)
    
- **Database Engine:** MySQL Server v8.0 or v9.0 Community Server
    
- **Required Libraries:**
    
    - `mysql-connector-python` (Database Driver)
        
    - `statistics` & `math` (Mathematical & Statistical Calculations)
        
    - `getpass` (Secure Password Input)
        
    - `datetime` (Timestamping Operations)
        

## DATABASE SCHEMA & SQL ARCHITECTURE

The backend utilizes the database **`shadow_army_db`**. Below is the structural schema derived from the database dump:

### Table Structures

#### 1. `captains`

Stores administrative user credentials.

- `id` INT AUTO_INCREMENT PRIMARY KEY
    
- `name` VARCHAR(100) UNIQUE NOT NULL
    
- `password` VARCHAR(100) NOT NULL
    

#### 2. `soldiers`

Stores combat personnel details and health state metrics.

- `id` INT AUTO_INCREMENT PRIMARY KEY
    
- `name` VARCHAR(100) UNIQUE NOT NULL
    
- `password` VARCHAR(100) NOT NULL
    
- `hp` INT NOT NULL
    
- `mana` INT NOT NULL
    
- `rank` VARCHAR(20) NOT NULL
    
- `level` INT NOT NULL
    
- `status` VARCHAR(20) NOT NULL
    

#### 3. `weapons`

Catalog of armory hardware.

- `id` INT AUTO_INCREMENT PRIMARY KEY
    
- `category` VARCHAR(50) NOT NULL
    
- `name` VARCHAR(100) NOT NULL
    
- `caliber` VARCHAR(60) NOT NULL
    
- `qty` INT NOT NULL
    

#### 4. `mission_tasks`

Operational deployments and quests.

- `id` INT AUTO_INCREMENT PRIMARY KEY
    
- `mission_id` VARCHAR(20) NOT NULL
    
- `description` VARCHAR(200) NOT NULL
    
- `assigned_to` VARCHAR(100) NOT NULL
    
- `status` VARCHAR(30) NOT NULL
    
- `priority` VARCHAR(20) NOT NULL
    

#### 5. `weapon_orders`

Logistical requisition tracking.

- `id` INT AUTO_INCREMENT PRIMARY KEY
    
- `soldier` VARCHAR(100) NOT NULL
    
- `weapon` VARCHAR(100) NOT NULL
    
- `qty` INT NOT NULL
    
- `status` VARCHAR(30) NOT NULL
    

## SOURCE CODE

_(Insert your clean Python program source code in this section)_

Python

```
import math, random, statistics as stat
from math import pi
from getpass import getpass
from datetime import datetime
import mysql.connector

# ── DATABASE CREDENTIALS ──────────────────────────────────────────────────────
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "12345"  # Modify as per system configuration
DB_NAME = "shadow_army_db"

print("="*80)
print("🗡️  INITIALIZING SHADOW MILITARY PROTOCOL  🗡️")
print("="*80)

# ═══════════════════════════════════════════════════════════════════════════════
#  INDEX CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

NAME        = 0
CALIBER     = 1
QTY         = 2

EXP_NAME    = 0
EXP_QTY     = 1

ITEM_NAME   = 0
ITEM_QTY    = 1
ITEM_STATUS = 2

CAP_NAME    = 0
CAP_PASS    = 1

SOL_NAME    = 0
SOL_PASS    = 1
SOL_HP      = 2
SOL_MANA    = 3
SOL_RANK    = 4
SOL_LEVEL   = 5
SOL_STATUS  = 6

M_ID        = 0
M_DESC      = 1
M_ASSIGNED  = 2
M_STATUS    = 3
M_PRIORITY  = 4

O_SOLDIER   = 0
O_WEAPON    = 1
O_QTY       = 2
O_STATUS    = 3

# [Source code continues with function definitions: auth(), soldier_menu(), captain_menu(), etc.]
```

_(Note: In your exported report, run each corresponding function in Jupyter Notebook and capture/display the CLI execution block under each heading below)_.

### Output 1: System Initialization & Database Handshake

_(Run `setup_database()` and capture successful database creation and connection confirmation)_.

### Output 2: Identity Verification System (`auth()`)

_(Capture login sequences for both Captain tier and Soldier tier)_.

### Output 3: Monarch Command Center (`captain_menu()`)

_(Capture the main administrative options dashboard)_.

### Output 4: Armory Inventory & Requisition Approval (`approve_weapon_orders()`)

_(Capture viewing pending orders and approving/rejecting a soldier's weapon request)_.

### Output 5: Shadow Army Health & Readiness Dashboard (`check_health_status()`)

_(Capture the health status grouping across Critical, Injured, Recovering, and Active Duty units)_.

### Output 6: System Analytics & Combat Readiness (`view_system_stats()`)

_(Capture personnel stats, mission completion percentages, average HP/Level metrics, and rank distribution visualization)_.

### Output 7: Shadow Soldier Command Center (`soldier_menu()`)

_(Capture soldier-side options, weapon ordering, health updates, and assigned mission checks)_.

## CONCLUSION

The **Shadow Military Protocol (Solo Leveling Military Management System v2.0)** successfully achieves a robust integration between object-oriented Python scripting and a relational MySQL backend database. By decoupling administrative functions from low-level data storage, the system ensures data persistence, transactional security, and modularity.

### Scope for Future Enhancement:

1. **Graphical User Interface (GUI):** Transition from a Command-Line Interface (CLI) to a desktop GUI using PyQt6 or Tkinter.
    
2. **Role-Based Access Control (RBAC) Expansion:** Implement hashed password storage using `bcrypt` or `hashlib` instead of plain-text passwords.
    
3. **Automated Combat Simulation Engine:** Integrate dynamic statistical algorithms to model mission success probability based on unit levels, HP, and available armory supplies.
    
4. **REST API Interface:** Develop a FastAPI/Flask backend to expose military management endpoints for web/mobile client applications.
    

## BIBLIOGRAPHY

- **Computer Science with Python (Class XII)** – Sumita Arora
    
- **Computer Science with Python (Class XII)** – Preeti Arora
    
- **MySQL 8.0 Reference Manual** – Oracle Documentation (`[dev.mysql.com/doc](https://dev.mysql.com/doc)`)
    
- **Python 3.x Documentation** – Official Python Reference (`docs.python.org`)
    
- **W3Schools Online Web Tutorials** (`[www.w3schools.com/python](https://www.w3schools.com/python)`, `[www.w3schools.com/sql](https://www.w3schools.com/sql)`)
    
- **GeeksforGeeks Computer Science Resources** (`www.geeksforgeeks.org`)