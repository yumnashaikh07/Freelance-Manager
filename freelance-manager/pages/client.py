import streamlit as st 
import json
import os
from utils.file_utils import load_client_list, save_client_list, load_project_list, save_project_list

class Client:
    def __init__(self, id, name, email, phone, numberofproj):
        self.id = id
        self.name = name
        self.email= email
        self.phone = phone
        self.numberofproj = numberofproj

            
    def get_projects_from_projectjson(self, project_list):
        """Return list of project titles where client name matches."""
        return [p["title"] for p in project_list.values() if p["client"] == self.name]
        

clients = load_client_list()
st.title("👤 Client & Project Management")

with st.form("add_client"):
    st.subheader("➕ Add a New Client")
    client_id = st.text_input("Client ID (eg. 0001)").strip()
    client_name = st.text_input("Client Name").upper().strip()
    client_email = st.text_input("Client Email").strip()
    client_phone = st.text_input("Client Phone").strip()
    numberofproj = st.text_input("Number of Projects").strip()

    submitted_client = st.form_submit_button("Add Client")
    if submitted_client:
        if client_id and client_name and client_email and client_phone and numberofproj:
            if client_id.isdigit() and 1 <= int(client_id) <= 5000 :
                # client_id = int(client_id )
                if client_id not in clients:
                    clients[client_id] = {
                    "name": client_name,
                    "email": client_email,
                    "phone": client_phone,
                    "numberofproj": numberofproj,
                    }
                    save_client_list(clients)
                    st.success(f"✅ Client '{client_name}' added successfully!")

                else:
                    st.warning("❌ Client ID already exists! Please use a different ID.")
            else:
                st.warning("❌ Invalid ID! Please enter a valid number between 1 and 5000.")
        else:
            st.error("❌ Please fill all fields correctly.")
    else:
        st.info("Please fill in the client details and click 'Add Client' to proceed.")