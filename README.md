# 📩 SMS Spam Classifier

A machine learning project built using **Streamlit** to classify SMS messages as **Spam** or **Ham (Not Spam)** in real time.

---

## 🚀 Features

- Classifies user-input text messages
- Preprocessing with NLTK (tokenization, stemming, stopwords removal)
- TF-IDF vectorization
- Trained using a machine learning model (e.g., Naive Bayes / Logistic Regression)
- Clean and interactive Streamlit interface

---

## 🖥️ Live Demo (Optional)

👉 [Deploy on Streamlit Cloud / Render / Hugging Face Spaces]  
*(Add your live link here when deployed)*

---

## 📂 Project Structure

spam-classifier/
│
├── app.py # Streamlit web app
├── utils.py # Text transformation function
├── vectorizer.pkl # TF-IDF vectorizer (if under 100MB)
├── spam_model.pkl # Trained ML model (download separately)
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md


---

## ⚙️ Installation & Setup

1. **Clone the repository**:


    git clone https://github.com/hulkalan/spam-classifier.git
    cd spam-classifier

**Create a virtual environment (optional but recommended):**

        python -m venv .venv
        .venv\Scripts\activate


**Install dependencies:**


     pip install -r requirements.txt

**Download model file:**

    The trained model file spam_model.pkl exceeds GitHub's 100MB limit, so please download it manually:

    📥 Download spam_model.pkl
    📥 Download vectorizer.pkl (if not included)

    Place both files in the project root folder (spam-classifier/)



**▶️ Run the App**

    streamlit run app.py


**🧠 Model Details**
 
    Text preprocessing: NLTK (lowercasing, stopwords, stemming)

    Vectorization: TF-IDF

    Classifier: [Logistic Regression / Naive Bayes / SVM]


**📚 Dependencies**
 
    streamlit

    scikit-learn

    nltk

    You can see the full list in requirements.txt.

**📸 Screenshot**

    (Optional: Add an image or animated demo)

**🛡️ License**
    
    MIT License – use freely, give credit 🎉

**🤝 Contributions**

    Pull requests are welcome. For major changes, please open an issue first.

🙋‍♂️ Author
    Alan Mathew
    GitHub