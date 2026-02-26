# 🏢 Employee Leave Manager MCP Server

This project implements an **Employee Leave Management System** using the **Model Context Protocol (MCP)** framework.

The system provides MCP tools that allow a Large Language Model (LLM) to manage employee leave records.

The MCP server was developed using **FastMCP**, integrated with the **Claude LLM**, and managed using the modern **uv Python environment**.

Employees can:

• Apply for leave  
• Check leave balance  
• View leave history  

This project demonstrates how **LLMs can interact with backend tools using MCP.**

------------------------------------------------------------

## 🚀 Features

• MCP-based tool server  
• FastMCP implementation  
• Claude LLM integration  
• Leave application tool  
• Leave balance tracking  
• Leave history retrieval  
• Automatic leave balance updates  
• In-memory database  
• uv-based Python environment

------------------------------------------------------------

## 🧠 Model Context Protocol (MCP)

Model Context Protocol (MCP) allows Large Language Models to interact with external tools in a structured way.

Instead of generating plain text responses, the LLM can directly call backend functions.

System workflow:

Claude LLM → MCP Client → MCP Server → Leave Tools → Response → Claude

The MCP server exposes structured tools that Claude can use automatically.

------------------------------------------------------------

## 📁 Project Structure

employee-leave-mcp/

README.md  
main.py  
pyproject.toml  
uv.lock

------------------------------------------------------------

## 🧰 MCP Tools

### 1. Apply Leave

Tool Name:

apply_leave

Description:

Apply for leave for an employee.

Parameters:

employee_id → Employee ID  
days → Number of leave days  
reason → Leave reason  
date → Leave date (yyyy-mm-dd)

Example:

apply_leave("emp1",1,"Personal","2025-06-10")

Example Response:

Leave applied for 1 day(s) on 2025-06-10 for 'Personal'. Remaining balance: 17 day(s).

------------------------------------------------------------

### 2. Get Leave Balance

Tool Name:

get_leave_balance

Description:

Returns remaining leave balance.

Parameters:

employee_id

Example:

get_leave_balance("emp1")

Example Response:

emp1 has 18 day(s) of leave remaining.

------------------------------------------------------------

### 3. Get Leave Dates

Tool Name:

get_leave_dates

Description:

Returns all leave dates taken by an employee.

Parameters:

employee_id

Example:

get_leave_dates("emp1")

Example Response:

["2025-06-03","2025-06-04"]

------------------------------------------------------------

## 🗄 Simulated Database

The system uses an in-memory database.

Maximum leave allowed per employee:

20 days

Example balances:

emp1 → 18 days remaining  
emp2 → 20 days remaining

The database resets when the server restarts.

------------------------------------------------------------

## ⚙️ Environment Setup (uv)

This project uses **uv** for dependency management and execution.

### Install uv

pip install uv

### Initialize Project

uv init

### Install Dependencies

uv add mcp

This automatically creates:

pyproject.toml  
uv.lock

------------------------------------------------------------

## ▶️ Installing the MCP Server

Instead of running a normal server, this project installs MCP tools that can be used by Claude.

Install the MCP server:

uv run mcp install main.py

After installation, the tools become available to Claude automatically.

------------------------------------------------------------

## 🤖 Claude LLM Integration

This MCP server was designed to work with the **Claude LLM**.

Claude converts natural language into MCP tool calls.

Example prompts:

Apply leave for emp1 on 2025-06-10 for personal reason

Check leave balance for emp1

Show leave dates for emp1

Claude automatically selects and executes the appropriate MCP tool.

------------------------------------------------------------

## 🔧 Technologies Used

Python  
FastMCP  
Model Context Protocol (MCP)  
Claude LLM  
uv Environment Manager

------------------------------------------------------------

## 🎯 Applications

Employee leave management

HR automation

LLM tool integration

Workflow automation

AI assistants with backend tools

------------------------------------------------------------

## 🔮 Future Improvements

Persistent database support

Authentication system

Web interface

Cloud deployment

Leave approval workflow

------------------------------------------------------------

## 👨‍💻 Author

Mohammed Azhar Sait
