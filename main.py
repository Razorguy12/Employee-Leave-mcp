from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("EmployeeLeaveManager")

# Constants
MAX_LEAVE = 20

# Simulated database
leave_db = {
    "emp1": [
        {"days": 1, "reason": "Personal", "date": "2025-06-03"},
        {"days": 1, "reason": "Personal", "date": "2025-06-04"}
    ],
    "emp2": []
}

leave_balance = {
    "emp1": MAX_LEAVE - 2,  # 18 left
    "emp2": MAX_LEAVE       # 20 left
}

# TOOL 1: Apply for leave
@mcp.tool()
def apply_leave(employee_id: str, days: int, reason: str, date: str) -> str:
    """Apply for leave for an employee with date fomat as yyyy-mm-dd"""
    if employee_id not in leave_balance:
        leave_balance[employee_id] = MAX_LEAVE
        leave_db[employee_id] = []

    if leave_balance[employee_id] < days:
        return f"Insufficient leave balance. You have {leave_balance[employee_id]} days left."

    leave_balance[employee_id] -= days

    leave_db[employee_id].append({
        "days": days,
        "reason": reason,
        "date": date
    })

    return f"Leave applied for {days} day(s) on {date} for '{reason}'. Remaining balance: {leave_balance[employee_id]} day(s)."

# TOOL 2: Get leave balance
@mcp.tool()
def get_leave_balance(employee_id: str) -> str:
    """Return remaining leave balance for an employee"""
    balance = leave_balance.get(employee_id, MAX_LEAVE)
    return f"{employee_id} has {balance} day(s) of leave remaining."

# TOOL 3: Get leave dates
@mcp.tool()
def get_leave_dates(employee_id: str) -> list:
    """Return all leave dates taken by the employee"""
    records = leave_db.get(employee_id, [])
    return [entry["date"] for entry in records]

# Run server
if __name__ == "__main__":
    mcp.run(host="0.0.0.0", port=8000)