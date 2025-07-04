# 🩺 Diabetes Prediction Web App using Machine Learning

This project is a capstone submission for the AICTE Internship, developed by **Shravan Bharat Devrukhkar** under the Department of Computer Engineering at Dr. Babasaheb Ambedkar Technological University (Diploma Wing), Lonere.

 [Live GitHub Repo](https://github.com/Shravan6125/diabetes-prediction-app-aicte)

---

##  Problem Statement

Millions of people worldwide suffer from diabetes without early detection. Timely prediction can help manage lifestyle and reduce medical emergencies. Manual diagnosis is time-consuming, and there's a need for a system that quickly identifies high-risk individuals using key medical data.

---

##  Proposed Solution

The project implements a real-time web-based system using Streamlit and a machine learning model (SVM) trained on the Pima Indians Diabetes Dataset. It takes user input (like glucose level, BMI, etc.) and predicts the likelihood of diabetes.

---

## ⚙ Technologies & Tools Used

- **Python 3.12**
- **scikit-learn** (SVM classifier)
- **Streamlit** (Frontend)
- **Pandas / NumPy**
- **StandardScaler** (Data normalization)

---

## 📊 Features

- Form-based web UI for patient data entry
- Real-time prediction
- Model trained on standardized data
- Deployment-ready with saved model (`model.pkl`)

---

## 💻 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Shravan6125/diabetes-prediction-app-aicte.git
cd diabetes-prediction-app-aicte
# diabetes-prediction-app-aicte



2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate  #
On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run the app
streamlit run main.py
