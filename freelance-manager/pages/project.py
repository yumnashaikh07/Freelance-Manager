import streamlit as st 
import pandas as pd
from utils.file_utils import load_project_list, save_project_list, load_task_list, save_task_list, load_client_list, save_client_list

class Project:
    def __init__(self, title, project_id, status, tasks, deadline, client):
        self.title = title
        self.project_id = project_id
        self.status = status
        self.tasks = []
        self.deadline = deadline
        self.client = client    #same client name as in client.py   

projects = load_project_list()
tasks = load_task_list()

st.title("📊 Project Management")

with st.form("add_project"):
    st.subheader("➕ Add New Project")

    project_title = st.text_input("Project Title:").upper().strip()
    project_id = st.text_input("Project ID (eg. 0001):").strip()
    project_status = st.selectbox("Project Status", ["Completed" , "In Progress", "Not Started"])
    project_deadline = st.text_input("Deadline : ").strip()
    project_maintasks = st.selectbox("Main Tasks :", ["Web Development", "Video Editing", "Logo Design", "Thumbnail Design", "UI/UX Design" ])
   

    clients = load_client_list()  # Load the list of clients
    clients_names = [client["name"] for client in clients.values()]  # Extract client names
    project_client = st.selectbox("Select Client: ", clients_names )  # Display client names in the dropdown
 
    
    saveproject = st.form_submit_button("Save Project")
    if saveproject:
        if project_title and project_id and project_status and project_deadline and project_maintasks and project_client:
            if project_id.isdigit() and 1 <= int(project_id) <= 5000:
                if project_id not in projects:
                    projects[project_id] ={
                    "title" : project_title,
                    "status" : project_status,
                    "tasks" : project_maintasks,
                    "deadline" : project_deadline,
                    "client" : project_client
                    }
                    save_project_list(projects)
                    st.success(f"✅ Project '{project_title}' added successfully!")
               
                else:
                    st.warning("❌ Client ID already exists! Please use a different ID.")
            else:
                st.warning("❌ Invalid ID! Please enter a valid number between 1 and 5000.")
        else:
            st.error("❌ Please fill all fields correctly.")
    else:
        st.info("Please fill in the client details and click 'Add Client' to proceed.")
