#Tycc Club teams and their players list


import streamlit as st


# Display the club logo
st.image('TYCC_logo.png', use_column_width=True)


# Define the data as a dictionary of lists
data = {
    'Team 1': ['Suresh', 'Avi', 'Shirish'],
    'Team 2': ['Vicky', 'Vinayak', 'Vamsi'],
    'Team 3': ['Stu', 'Rajesh', 'Chaithu'],
    'Team 4': ['Shree', 'Deepak', 'Kumara'],
    'Team 5': ['Dinesh', 'Anjana', 'Deb']
}


# Define the playing fixtures as a dictionary of hyperlinks
fixtures = {
    'Team 1': 'https://www.cricketleinster.ie/match-centre/fixtures?category=&competition=&club=&team=0M3W06UZ35&venue=&year=&month=',
    'Team 2': 'https://www.cricketleinster.ie/match-centre/fixtures?category=&competition=&club=&team=1WXN6KTQXE&venue=&year=&month=',
    'Team 3': 'https://www.cricketleinster.ie/match-centre/fixtures?category=&competition=&club=&team=1WXN2WFQJE&venue=&year=&month=',
    'Team 4': 'https://www.cricketleinster.ie/match-centre/fixtures?category=&competition=&club=&team=KJR4GKSLJO&venue=&year=&month=',
    'Team 5': 'https://www.cricketleinster.ie/match-centre/fixtures?category=&competition=&club=&team=E302K6C4X0&venue=&year=&month='
}



# Set the page title and heading
st.set_page_config(page_title='TyCC Club Teams List', page_icon=':Cricket:')
st.title('TyCC Club Teams List')

# Display the data and fixtures as a table
for team, players in data.items():
    st.write(f"### {team}")
    st.table(players)
    st.write(f"Playing Fixtures: [{team}]({fixtures[team]})")
