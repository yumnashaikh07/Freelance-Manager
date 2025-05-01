import json
import os
# Load Clients from JSON
def load_client_list():
    """Load clients from JSON file or return an empty dictionary if file is missing/corrupted."""
    if os.path.exists("client.json"):
        with open("client.json", "r") as f:
            try:
                clientjson = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Error: Could not load client.json. Returning an empty list.")
                return {}
        return clientjson
    else:
        print("client.json not found.")
        return {}
# Save Clients to JSON 
def save_client_list(clients):
    """Save client details into a JSON file."""
    with open("client.json", "w") as f:
        json.dump(clients, f, indent= 3)
# PROJECT.JSON FUNCTIONS
def load_project_list():
    """Load projects from JSON file or return an empty dictionary if file is missing/corrupted."""
    if os.path.exists("project.json"):
        with open("project.json", "r") as f:
            try:
                projectjson = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Error: Could not load project.json. Returning an empty list.")
                return {}
        return projectjson
    else:
        print("project.json not found.")
        return {}

# Save Projects to JSON 
def save_project_list(projects):
    """Save project details into a JSON file."""
    with open("project.json", "w") as f:
        json.dump(projects, f, indent= 3)

# TASK.JSON FUNCTIONS

def load_task_list():
    """Load tasks from JSON file or return an empty dictionary if file is missing/corrupted."""
    if os.path.exists("task.json"):
        with open("task.json", "r") as f:
            try:
                taskjson = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Error: Could not load task.json. Returning an empty list.")
                return {}
        return taskjson
    else:
        print("task.json not found.")
        return {}

# Save Clients to JSON 
def save_task_list(tasks):
    """Save task details into a JSON file."""
    with open("task.json", "w") as f:
        json.dump(tasks, f, indent= 3)