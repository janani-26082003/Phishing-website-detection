Ensemble Machine Learning Model for Phishing Website Detection :
A high-performance cybersecurity solution that uses Machine Learning to identify phishing URLs in real-time. This project analyzes URL structures to protect users from identity theft and financial fraud.

Why This Project?
Phishing is one of the most common cyber threats. This project moves beyond simple "blacklists" by using Machine learning to predict if a URL is malicious based on its characteristics (like length, special symbols, and redirection).

How It Works:
1. Feature Extraction: The system looks at a URL and extracts 30+ features (e.g., presence of `@`, URL length, `//` redirection).
2. Ensemble Learning: Instead of one model, it uses a "team" of models (MLP, SVM, and XGBoost) to vote on the result for higher accuracy.
3. Web Interface: Users can paste a URL into a **Flask web app** and get an instant "Safe" or "Phishing" result.

Key Features
1. Real-time Detection: Instant classification via a web dashboard.
2. Smart Analysis: Detects hidden patterns in URLs that humans might miss.
3. Confidence Scores: Shows how certain the AI is about its prediction.
4. Safety Tips: Provides suggestions on how to stay safe online.

Technologies Used
1. Language: Python
2. ML Libraries: Scikit-learn, XGBoost, PyTorch, NumPy, Pandas
3. Web Framework: Flask (Backend), HTML/CSS (Frontend)
4. Environment: VS Code / Kaggle

How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `python app.py`
3. Open `http://127.0.0.1:5000` in your browser.

