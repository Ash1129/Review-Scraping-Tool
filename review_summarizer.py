import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from textblob import TextBlob

# Function to load CSV
def load_data(file):
    data = pd.read_csv(file)
    return data

# Function to analyze ratings
def analyze_ratings(data):
    st.subheader('Rating Distribution')
    fig, ax = plt.subplots()
    sns.countplot(data['rating'], ax=ax)
    st.pyplot(fig)

# Function to analyze review content
def analyze_reviews(data):
    st.subheader('Review Content Analysis')
    
    # Generate word cloud
    all_reviews = ' '.join(data['review content'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_reviews)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

    # Sentiment analysis
    data['sentiment'] = data['review content'].apply(lambda x: TextBlob(x).sentiment.polarity)
    st.subheader('Sentiment Analysis')
    fig, ax = plt.subplots()
    sns.histplot(data['sentiment'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)
    
    st.subheader('Sample Reviews')
    for i in range(5):
        st.write(data['review content'][i])
        st.write(f"Sentiment: {data['sentiment'][i]:.2f}")
        st.write('---')

# Streamlit web app
st.title('Review and Rating Analysis')

uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file:
    data = load_data(uploaded_file)
    
    st.write('## Data Preview')
    st.write(data.head())

    analyze_ratings(data)
    analyze_reviews(data)
