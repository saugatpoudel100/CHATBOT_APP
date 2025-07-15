# 💬 Customer Service Chatbot (Flask + ML)

A simple machine learning-based chatbot for handling customer service queries like order status, cancellations, shipping info, returns, and more. The bot is trained using intents stored in a JSON file and uses Flask for backend APIs. Tailwind CSS is optionally used for styling the frontend.

---

## 🗂 Project Structure
```bash

chatbot_app/

├── app.py # Flask application to serve chatbot API and frontend

├── model.py # Model training script (scikit-learn + TF-IDF)

├── requirements.txt # Python dependencies

├── model/ # Folder to store trained models

│ ├── model.pkl # Trained classifier model

│ └── vectorizer.pkl # Trained TF-IDF vectorizer

├── data/ # Training data folder
│ 
  └── intents.json # Contains tags, patterns, and responses

├── templates/ # HTML templates for chatbot UI
│ └── index.html # Chatbot frontend (optional)

├── static/ # Static assets (optional)
│ └── styles.css # Tailwind CSS for styling UI


```

---

## 📊 Features

- Text classification with `scikit-learn` and `TfidfVectorizer`
- Flexible intent handling from a JSON file
- Easily expandable with more customer service intents
- Lightweight Flask backend API
- Simple web interface with Tailwind CSS (optional)

---

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/saugatpoudel100/CHATBOT_APP.git
cd chatbot_app
```
---

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Train the chatbot model
```bash
python model.py
```
This will create model/model.pkl and model/vectorizer.pkl.

### ▶️ Running the Flask App
```bash
python app.py
```
Open your browser and go to http://127.0.0.1:5000/ to interact with the chatbot.

### 🧠 Training Data Format
Example structure of intents.json:

### json
```bash
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey there"],
      "responses": ["Hello! How can I help you?", "Hi there!"]
    },
    ...
  ]
}
```
---
## 🚀 Deployment
You can deploy this app to:

Heroku

Render

Vercel (backend only)

Any VPS or server supporting Python/Flask

---

## 🛠 Tech Stack
Python 3

Flask

scikit-learn

HTML/CSS

Tailwind CSS (optional for frontend styling)

---

## 📄 License
This project is licensed under the MIT License.

---
## 🙋‍♂️ Author
Your Saugat

Feel free to contribute or report issues!

