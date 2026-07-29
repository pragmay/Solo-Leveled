

***

### I. Conceptual Overview

**Purpose:** To simulate a high-stakes military resource, personnel, and mission management system in a console environment.
**Architecture:** The application is built around role-based access control (RBAC). Users must authenticate as either a "Captain" (Monarch/High Command) or a "Soldier." Each role leads to a separate command loop with distinct operational capabilities.
**Operational Flow:**

1.  **Initialization:** Load hardcoded initial data (Captains, Soldiers, Arsenal) into global lists.
2.  **Authentication (`auth()`):** User logs in using name and password; the system determines their role (`cap` or `sol`).
3.  **Role Execution:** The user enters their specific menu loop (e.g., 🗡️ Soldier Operations or 👑 Monarch Command Center).
4.  **Action Handling:** Functions execute specific actions, manipulating both the global in-memory state *and* triggering corresponding database operations (MySQL Connector/Python) for persistence.

### II. System Components and Modules

The code is logically separated based on function: Constants, Initialization Data, Core Logic, Soldier Operations, và Captain Operations.

#### A. Global Configuration & Indexing
This section defines the schema (implicitly) using integer constants before data is stored in lists. This design pattern makes list-based access extremely fast but highly dependent on the index order never changing.

*   `NAME`, `CALIBER`, `QTY`: Indices for Weapon entries.
*   `SOL_HP`, `SOL_RANK`, `SOL_LEVEL`, `SOL_STATUS`: Key indices for Soldier data structures.
*   `M_ID`, `M_ASSIGNED`, `M_STATUS`, `M_PRIORITY`: Key indices for Mission tasks.

#### B. Data Initialization (State Persistence)
This section populates the system's initial state using hardcoded lists and dictionaries:

1.  **Personnel:** Pre-populated lists of Captains (`captains`) and Soldiers (`all_soldiers`), complete with roles, passwords, HP/Mana stats, and ranks.
2.  **Inventory (Armory):** The `armory` dictionary is the primary inventory database, categorized into types like `"Assault_Rifles"`, `"Ammunition"`, and `"Accessories"`. This holds all available resources (`QTY`).
3.  **Operations:** Initial entries for ongoing military assignments (`mission_tasks`) and tracking logistics (`weapon_orders`).

#### C. Role-Based Command Centers

##### ⚔️ Soldier Operations (`soldier_menu`):
This menu is focused on individual soldier progress and immediate needs.

*   **Order Weapons:** The soldier views available weaponry by category, selects an item/quantity, and submits a requisition to the system log (`weapon_orders`), pending Captain approval.
*   **Update Health Status:** Allows the soldier (or external users via this function) to manually update their combat stats (HP, Mana, Status). This triggers a database write.
*   **View Missions/Update Completed Tasks:** Provides soldiers visibility into assigned objectives and allows them to mark tasks as completed, which updates mission records and awards simulated XP.
*   **View My Stats:** Displays detailed performance metrics, including calculated success rates based on `mission_tasks`.

##### 👑 Captain Operations (`captain_menu`):
This menu is focused on strategic management, logistics, and personnel oversight.

*   **Approve Weapon Orders:** The core logistical function. Captains review the pending orders list and approve or cancel requisitions submitted by soldiers.
*   **Order Inventory Supplies:** Allows supply chain managers to introduce new items (Ammunition/Accessories) into the system inventory.
*   **Add New Missions/Weapons/Recruits:** Functions for expanding the operational scope of the system, manually adding tasks, armaments, or personnel.
*   **Check All Soldiers' Health Status:** Provides a high-level overview of overall unit readiness across all soldiers.

### III. Data Model Structure Summary

The application uses three primary data types to represent its core entities:

| Entity | Primary Container(s) | Core Data Fields (Index Reference) | Description |
| :--- | :--- | :--- | :--- |
| **Soldier** | `all_soldiers` | Name, Pass, HP, Mana, Rank, Level, Status | Personnel unit. Dynamic stats tracked in memory and DB. |
| **Captain** | `captains` | Name, Pass | Authentication users with administrative access. |
| **Inventory Item** | `armory` (Category Lists) | Name, Caliber/Qty/Status | Weapons, Ammo, Accessories. Tracks current stock level (`QTY`). |
| **Operation Record** | `mission_tasks`, `weapon_orders` | ID, Description, Target, Status | Logs the historical and future operational demands of the military unit. |

### IV. Key Function Summaries

| Function Name | Role | Purpose (High Level) | System Impacted |
| :--- | :--- | :--- | :--- |
| `auth()` | General | Initiates login, validates credentials against Captains or Soldiers data. Central traffic director. | Global State |
| `soldier_menu()` | Soldier | Provides the interactive loop and routing for soldier-specific commands. | Soldier Data, Mission Tasks |
| `order_weapons()` | Soldier | Allows a soldier to submit a request for an item from the current arsenal stock. | `weapon_orders` (Pending) |
| `approve_weapon_orders()` | Captain | Reviews all pending requisitions and changes their status in the system. | `weapon_orders` Status, Inventory Stock (implied update upon approval) |
| `update_health_status()` | Soldier/Captain | Modifies a soldier's core combat attributes (HP, Mana, Status). Requires DB persistence (`db_update_soldier`). | Soldier Data |
| `view_system_stats()` | Captain | Provides administrative oversight by calculating unit performance metrics (e.g., success rate, total resources). | All data structures |

***
