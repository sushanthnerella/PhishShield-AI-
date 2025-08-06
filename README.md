
# 🛡️ PhishShield AI – Real-Time Phishing Website Detection

## 📌 Problem Statement

**Problem Statement 1** – Build a robust, real-time AI system to detect phishing websites and protect users from cyber threats.

## 🎯 Objective

The *PhishShield AI* project aims to provide an instant phishing detection tool that safeguards users by analyzing website URLs, domains, and HTML-based features.
The system uses a custom **Gradient Descent classifier** trained on the **PhishTank dataset**, delivering accurate, supervised machine learning-based threat classification.

This tool enhances web security by providing users with a **real-time interface** to check URLs before interacting with them, preventing credential theft and malicious attacks.

## 🧠 Team & Approach

### Team Name: Sushanth

### Team Members:

* *Nerella Sushanth* (Machine Learning Developer)

### Your Approach:

We built this solution to address the growing threat of phishing websites, which trick users into revealing sensitive information.
The project extracts **URL-level, domain-level, and HTML-based features** from a given website and feeds them into a custom-built Gradient Descent model for classification.
Challenges included handling noisy datasets, feature engineering for better accuracy, and creating a fast inference pipeline for real-time results.

## 🛠 Tech Stack

*Core Technologies Used:*

* **Programming Language:** Python
* **Machine Learning:** Custom Gradient Descent Classifier (Supervised Learning)
* **Dataset:** PhishTank dataset
* **Frontend:** Simple user-facing interface (Python-based GUI / Web)
* **Deployment:** Local deployment for testing

*Key Libraries:*

* NumPy, Pandas (data handling)
* Scikit-learn (model evaluation & preprocessing)
* Flask / Streamlit (interface deployment)

## ✨ Key Features

* ✅ **Real-Time Detection** – Classifies websites instantly as *Phishing* or *Legitimate*
* ✅ **Feature Extraction** – Analyzes URL, domain, and HTML-based properties
* ✅ **Custom ML Model** – Trained Gradient Descent classifier achieving **82% accuracy**
* ✅ **User Interface** – Easy-to-use interface for entering URLs and getting results instantly
* ✅ **Security Enhancement** – Helps users avoid scams and data theft

## 📽 Demo & Deliverables

*(Add links if available)*

* **Demo Video:** *To be added*
* **Pitch Deck / PPT:** *To be added*

## ✅ Tasks & Achievements Checklist

* ✅ Built and trained a custom Gradient Descent classifier
* ✅ Achieved 82% accuracy on PhishTank dataset
* ✅ Developed a functional user-facing interface
* ✅ Implemented real-time inference for instant URL classification

## 🧪 How to Run the Project

### Requirements:

* Python 3.x
* Install dependencies:

```bash
pip install -r requirements.txt
```

### Local Setup:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/phishshield-ai
```

2. Navigate to the project folder:

```bash
cd phishshield-ai
```

3. Run the interface:

```bash
python app.py
```

4. Enter a URL in the interface to check for phishing threats.

---

