# 🎬 Movie Recommender System
webapp live at https://sahasranshu-movie-recommender.streamlit.app/

A content-based movie recommender web app built using the **TMDb 5000 Movie Dataset**. This project combines data preprocessing, EDA, vectorization, and cosine similarity to deliver top 5 movie recommendations based on user input.

---

## 🔍 Features

- 📊 **Exploratory Data Analysis (EDA)**  
  Gained insights into genres, popularity, ratings, and other trends in the dataset.

- 🧹 **Data Preprocessing**  
  Cleaned and transformed raw data to ensure high-quality, consistent inputs.

- 🧠 **Content-Based Filtering**  
  Utilized NLP techniques like **CountVectorizer** and **cosine similarity** to compare movie metadata and generate recommendations.

- 🎥 **Top 5 Movie Recommendations**  
  Suggests similar movies from a pool of **5000+ titles**.

- 🌐 **Interactive Web App**  
  Built with **Streamlit** and integrated with the **TMDb API** to fetch dynamic movie posters.

---

## 🚀 How It Works

1. Choose a movie from the dropdown list.  
2. Click the **"Recommend"** button.  
3. Instantly view 5 similar movies with their posters.

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy, Scikit-learn  
- Streamlit  
- Requests (for TMDb API)  
- Pickle (for model persistence)

---

## 💡 Future Improvements

- Add collaborative filtering for user-personalized recommendations  
- Include movie trailers and ratings  
- Deploy on Streamlit Cloud or Hugging Face Spaces  
