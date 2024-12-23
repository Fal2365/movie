import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Title of the app
st.title('Movie Performance Analysis')

# Sidebar for uploading the data
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the data
    df = pd.read_csv(uploaded_file)

    # Display dataset
    st.subheader("Dataset Overview")
    st.write(df.head())

   

    # Visualizing the data
    st.subheader("Visualize Data")

    # Rating vs Budget scatter plot
    st.write("Budget vs Rating")
    fig = px.scatter(df, x="budget", y="rating", title="Budget vs Rating")
    st.plotly_chart(fig)

    # Box plot of rating distribution by genre
    st.write("Rating by Genre (Box Plot)")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='genre', y='rating', data=df, ax=ax)
    ax.set_title('Rating Distribution by Genre')
    st.pyplot(fig)

    # Rating trend over years (Line plot)
    st.write("Rating Trend Over Years (Line Plot)")
    rating_trend = df.groupby('year')['rating'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(x='year', y='rating', data=rating_trend, ax=ax)
    ax.set_title('Rating Trend Over Years')
    st.pyplot(fig)

    # Display some specific analysis
    st.subheader("Advanced Analysis")

    # Filter movies by rating
    rating_threshold = st.slider("Select Rating Threshold", min_value=0, max_value=10, value=5)
    filtered_movies = df[df['rating'] > rating_threshold]
    st.write(f"Movies with rating greater than {rating_threshold}:", filtered_movies)

    # Additional analysis could be added here based on the data, such as clustering, regression models, etc.

else:
    st.warning("Please upload a CSV file to begin analysis.")

