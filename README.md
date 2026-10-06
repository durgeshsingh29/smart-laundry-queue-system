# 🧺 Smart Laundry Queue & Notification System

A Python-based smart laundry management system designed to solve common hostel laundry problems such as long queues, uncertain waiting times, and inefficient machine usage.

The application provides a simple Streamlit interface where students can register, select a washing machine, join a queue, track their position, and receive turn notifications. It also includes an admin dashboard and basic machine-learning-based waiting-time prediction.

---

## 📌 Problem Statement

In many college hostels, students have to wait for washing machines without knowing:

* How many students are already waiting
* Their position in the queue
* How long they may have to wait
* When their laundry turn is approaching

This project provides a centralized digital system to manage laundry queues and estimate waiting time.

---

## 💡 Solution

The **Smart Laundry Queue & Notification System** allows students to:

1. Register their details
2. Select an available laundry machine
3. Join the machine queue
4. View their queue position
5. Get an estimated waiting time
6. Receive a notification when their turn is approaching

Administrators can manage queues, complete laundry cycles, remove queue entries, and view usage statistics.

---

## ✨ Features

### 👨‍🎓 Student Features

* Student registration
* Washing machine selection
* Join laundry queue
* Queue position tracking
* Estimated waiting time
* Turn-approaching notification
* Current laundry status

### 👨‍💼 Admin Features

* View all active queues
* Monitor laundry machines
* Mark laundry as completed
* Remove queue entries
* View queue records

### 🤖 AI/ML Feature

The project includes a basic **Machine Learning waiting-time prediction model** using Linear Regression.

The model predicts waiting time based on the number of students ahead in the queue.

Example:

```text
Students ahead: 2
Predicted waiting time: ~60 minutes
```

The model can later be trained using real hostel laundry data for improved predictions.

### 📊 Analytics

The system provides basic analytics such as:

* Machine usage
* Queue status
* Laundry records
* Queue statistics

---

## 🛠️ Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Core development     |
| Streamlit    | Web interface        |
| SQLite       | Database             |
| Pandas       | Data processing      |
| NumPy        | Numerical operations |
| Scikit-learn | Machine Learning     |
| Matplotlib   | Data visualization   |

---

## 📂 Project Structure

```text
Smart-Laundry/
│
├── app.py
├── database.py
├── queue_manager.py
├── prediction.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

**`app.py`**
Main Streamlit application and user interface.

**`database.py`**
Creates and manages the SQLite database, students, machines, and queue records.

**`queue_manager.py`**
Handles queue positions and basic waiting-time calculations.

**`prediction.py`**
Contains the machine-learning model for waiting-time prediction.

**`requirements.txt`**
Contains the required Python libraries.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-laundry-queue-system.git
```

### 2. Open the project

```bash
cd smart-laundry-queue-system
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the virtual environment

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 🔄 System Workflow

```text
Student Registration
        ↓
Select Washing Machine
        ↓
Check Current Queue
        ↓
Join Queue
        ↓
Get Queue Position
        ↓
Waiting-Time Prediction
        ↓
Turn Notification
        ↓
Laundry Completed
        ↓
Queue Updated
```

---

## 🗄️ Database

The application uses **SQLite** for local data storage.

The database stores:

* Student information
* Laundry machines
* Queue entries
* Queue status
* Estimated waiting time
* Join time

The SQLite database file is generated automatically when the application runs.

---

## 🤖 Machine Learning

The current version uses **Linear Regression** to estimate waiting time based on the number of students ahead.

Example training relationship:

```text
0 people → 0 minutes
1 person → 30 minutes
2 people → 60 minutes
3 people → 90 minutes
```

### Future ML Improvement

The model can be improved by collecting real laundry usage data such as:

* Number of students in queue
* Time of day
* Day of week
* Machine number
* Actual washing duration
* Peak usage hours

This data can be used to train a more accurate waiting-time prediction model.

---

## 📊 Future Scope

Possible improvements include:

* 🔐 Student and admin authentication
* 📱 SMS/Email notifications
* 🔔 Real-time browser notifications
* ⏱️ Automatic machine timers
* 📈 Advanced analytics dashboard
* 🤖 Improved ML prediction
* 📅 Laundry slot booking
* 📲 Mobile-friendly interface
* ☁️ Cloud database
* 🏢 Multi-hostel support
* 📊 Peak-hour prediction

---

## 🎯 Objectives

The main objectives of this project are:

* Reduce unnecessary waiting time
* Improve laundry machine utilization
* Provide transparent queue information
* Predict approximate waiting time
* Digitize hostel laundry management
* Demonstrate practical applications of Python and Machine Learning

---

## 🎓 Academic Relevance

This project demonstrates practical implementation of:

* Python programming
* Database management
* Data processing
* Machine Learning
* User interface development
* Queue data structures
* Data visualization

It is suitable as a **B.Tech AI & Data Science Python project**.

---

## 👨‍💻 Author

**Durgesh Singh**

B.Tech — Artificial Intelligence & Data Science

Jaipur, Rajasthan

---

## 📄 License

This project is developed for educational and academic purposes.
