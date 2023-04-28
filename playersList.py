#Tycc Club teams and their players list


import streamlit as st

# Define the data as a dictionary of lists
data = {
    'Team 1': ['Suresh', 'Avi', 'Shirish'],
    'Team 2': ['Vicky', 'Vinayak', 'Vamsi'],
    'Team 3': ['Stu', 'Rajesh', 'Chaithu'],
    'Team 4': ['Shree', 'Deepak', 'Kumara'],
    'Team 5': ['Dinesh', 'Anjana', 'Deb']
}

# Set the page title and heading
st.set_page_config(page_title='TyCC Club Teams List', page_icon=':Cricket:')
st.title('Club Teams List')

# Display the data as a table
st.table(data)
