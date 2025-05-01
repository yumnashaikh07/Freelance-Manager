import json
import os
import streamlit as st
from utils.file_utils import load_task_list, save_task_list, load_client_list, load_project_list, save_project_list, save_client_list


tasks = load_task_list()
clients = load_client_list()
projects = load_project_list()

class Task:
    def __init__(self, task_title, task_description, task_hourly_rate, task_total_hours,title):
        self.task_title = task_title
        self.task_description = task_description
        self.task_hourly_rate = task_hourly_rate
        self.task_total_hours = task_total_hours
        self.title = title

with st.form("save_tasks"):
    st.subheader("➕ Add Task Details")
    st.write("Fill in the details below to add a new task to your existing Project.")
    
    projects_title_display = [
        f"(Project: {project['title']})  _  (Client: {project['client']})"
        for project in projects.values()
    ]

    selected_display_title = st.selectbox("Project Title:", ["Select Any Project Name"] + projects_title_display, index=0).strip()
    raw_project_title = ""
    task_client_name = ""
    if selected_display_title.startswith("(Project:"):
        try:
            raw_project_title = selected_display_title.split(")")[0].replace("(Project:", "").strip()
            task_client_name = selected_display_title.split("(Client:")[1].replace(")", "").strip()
        except IndexError:
            st.error("❗ Error parsing selected project and client name.")

    task_description = st.text_input("Task Description:").strip()
    task_title = st.selectbox("Task Title:", ["Web Development", "Video Editing", "Logo Design", "Thumbnail Design", "UI/UX Design"])

    task_rate_map = {
        "Web Development": 100,
        "Video Editing": 50,
        "Logo Design": 20,
        "Thumbnail Design": 10,
        "UI/UX Design": 30
    }

    default_rate = task_rate_map.get(task_title, 0)
    task_hourly_rate = st.number_input("Rate per Hour:", value=default_rate, step=1, format="%d", disabled=True)
    task_total_hours = st.number_input("Total Hours:")

    try:
        total_hours = float(task_total_hours)
    except ValueError:
        total_hours = 0

    total_price = default_rate * total_hours
    st.write(f"Total Task Price: ${total_price:.2f}")

    submit_task_button = st.form_submit_button("Save Task")

    if submit_task_button:
        if task_client_name and raw_project_title and task_description and total_hours > 0:
            if task_client_name not in tasks:
                tasks[task_client_name] = {}
            if raw_project_title not in tasks[task_client_name]:
                tasks[task_client_name][raw_project_title] = []

            new_task = {
                "task_title": task_title,
                "task_description": task_description,
                "task_hourly_rate": task_hourly_rate,
                "task_total_hours": total_hours,
                "total_price": total_price
            }
            existing_titles = [t["task_title"] for t in tasks[task_client_name][raw_project_title]]
            if task_title not in existing_titles:
                tasks[task_client_name][raw_project_title].append(new_task)
                save_task_list(tasks)
                st.success(f"✅ Task '{task_title}' added under project '{raw_project_title}' for client '{task_client_name}'!")
            else:
                st.warning(f"⚠️ Task '{task_title}' already exists under this project and client.")
        else:
            st.error("❗ Please fill in all fields correctly.")

project_options = {f"{project['title']} (Client: {project['client']})" :project_id for project_id, project in projects.items()}
project_option_list= ["Select Project to see its Tasks"]+ list(project_options.keys())
selected_proj = st.selectbox("Select Project to see its Tasks", project_option_list, index=0)

if selected_proj != "Select Project to see its Tasks":
    selected_proj_id = project_options[selected_proj]
    selected_project =projects[selected_proj_id]
    st.markdown(f"### Project Title: {selected_project['title']}")
    st.markdown("### Tasks Under This Project:")

    all_tasks = []
    if selected_project["title"] in tasks:
        all_tasks.extend(tasks[selected_project["title"]])

    # if "project_maintasks" in selected_project:
    #     all_tasks.append(selected_project["project_maintasks"])

        if all_tasks:
            for t in all_tasks:
                st.markdown(f"- **Task Title:** {t['task_title']}")
                st.markdown(f"  - **Description:** {t['task_description']}")
                st.markdown(f"  - **Hourly Rate:** ${t['task_hourly_rate']}")
                st.markdown(f"  - **Total Hours:** {t['task_total_hours']} hours")
                st.markdown(f"  - **Total Price:** ${t['total_price']:.2f}")
        else:
            st.markdown("❗ No tasks found for this project.")
