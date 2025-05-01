import streamlit as st  
import pandas as pd
from pages import project, task, client, invoice
from utils.file_utils import load_project_list, save_project_list, load_task_list, save_task_list, load_client_list, save_client_list


st.set_page_config(page_title="Freelance Manager", page_icon="💼")
st.markdown(
        """
    <style>
    .title {
        font-size: 57px;
        font-weight: bold;
        color: #0b4b0e;
        text-align: center;
        margin-bottom: 5px;
        font-family: 'sans-serif;
    }
    .subtitle {
        font-size: 18px;
        color:#537455;
        text-align: center;
    }
    .subsubtitle {
        font-size: 23px;
        font-family: arial;
        color: #9ce435;
        text-align: left;
        border-bottom: 5px double #9ce435;
        display: inline-block;

    }
    </style>
        """,
    unsafe_allow_html=True
    )
st.markdown('<div class="title">FREELANCE MANAGER</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">This is a simple web application to help freelancers manage their work.\nTo manage your projects, tasks, clients, and invoices go to Navigation Bar."</div>', unsafe_allow_html=True)
("_" *30)

st.markdown('<div class="subsubtitle">CURRENT CLIENTS</div>', unsafe_allow_html=True)
clients = load_client_list()

# Convert client data to a pandas DataFrame
client_data = {
    "Client ID": [],
    "Name": [],
    "Email": [],
    "Phone": [],
    "Number of Projects": []
}

for client_id, client_info in clients.items():
    client_data["Client ID"].append(client_id)
    client_data["Name"].append(client_info["name"])
    client_data["Email"].append(client_info["email"])
    client_data["Phone"].append(client_info["phone"])
    client_data["Number of Projects"].append(client_info["numberofproj"])

df_clients = pd.DataFrame(client_data)
st.dataframe(df_clients, use_container_width=True)
("_" *30)



st.markdown('<div class="subsubtitle">CURRENT PROJECTS</div>', unsafe_allow_html=True)
projects = load_project_list()

project_data = {
    "Project Title" :[],
    "Project ID" :[],
    "Project Status" :[],
    "Main Task":[],
    "Deadline": [],
    "Client Name": []
}

for project_id, project_info in projects.items():
    project_data["Project ID"].append(project_id)
    project_data["Project Title"].append(project_info["title"])
    project_data["Deadline"].append(project_info["deadline"])
    project_data["Project Status"].append(project_info["status"])
    project_data["Main Task"].append(project_info["tasks"])
    project_data["Client Name"].append(project_info["client"])

df_proj = pd.DataFrame(project_data)
st.dataframe(df_proj, use_container_width=True)
("_" *30)



# st.markdown('<div class="subsubtitle">CURRENT TASKS</div>', unsafe_allow_html=True)
# tasks = load_task_list()
# task_data = {
#     # "Project Title": [],
#     "Task Title" : [],
#     "Task Description" :[],
#     "Hourly Rate" : [],
#     "Total Hours" : [],
#     "Total Price":[]
# }

# for task_title , task_info in tasks.items():
#     # task_data["Project Title"].append(task_info["raw_project_title"])
#     task_data["Task Title"].append(task_title)
#     task_data["Task Description"].append(task_info["task_description"])
#     task_data["Hourly Rate"].append(task_info["task_hourly_rate"])
#     task_data["Total Hours"].append(task_info["task_total_hours"])
#     task_data["Total Price"].append(task_info["total_price"])

# df_task= pd.DataFrame(task_data)
# st.dataframe(df_task, use_container_width=True)
# ("_" *30)
