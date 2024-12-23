import streamlit as st
import pandas as pd

# Load data from CSV
@st.cache_data
def load_data():
    return pd.read_csv('indian_movie_data_final.csv')

# Load the dataset
data = load_data()

# App Title
st.title("Indian Movie Analysis")

# Sidebar filters
st.sidebar.header("Filters")
selected_genre = st.sidebar.selectbox("Select Genre", ["All"] + list(data['Genre'].unique()))
selected_language = st.sidebar.selectbox("Select Language", ["All"] + list(data['Language'].unique()))

# Filter data based on selection
filtered_data = data.copy()
if selected_genre != "All":
    filtered_data = filtered_data[filtered_data['Genre'] == selected_genre]
if selected_language != "All":
    filtered_data = filtered_data[filtered_data['Language'] == selected_language]

# Display filtered data
st.write("### Movie Data Table")
st.dataframe(filtered_data)

# Visualization: Bar chart of budget
st.write("### Budget Comparison (in ₹ Crores)")
st.bar_chart(filtered_data.set_index('Movie Title')['Budget (in crore ₹)'])

# Hit or Flop Analysis
st.write("### Hit or Flop Distribution")
st.bar_chart(filtered_data['Hit or Flop'].value_counts())

# Additional Information
st.write("### Insights")
st.markdown("- **High Budget Movies** are not always hits.")
st.markdown("- Genre and Language can influence the movie's success.")

# Create requirements.txt
requirements = """\nstreamlit\npandas\n"""
with open('requirements.txt', 'w') as f:
    f.write(requirements)
