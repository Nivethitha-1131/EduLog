# 📘 EduLog – Meeting Management System

EduLog is a simple web-based application built using **Flask** to record, manage, and store meeting details in an **Excel file**.
It includes secure login, structured meeting logging, and controlled access to stored data.

---

## 🚀 Features

* 🔐 **Login Authentication** (CSV-based users)
* 📝 **Meeting Log Form** with structured inputs
* ⏱️ **Custom Time Picker** (Hour / Minute / AM–PM)
* 👥 **Attendees & Absentees Selection** (with Select All)
* 📊 **Excel Storage** (`responses.xlsx`) with real time format
* ☁️ **OneDrive Sharing** for restricted access
* 🎨 Clean & user-friendly UI

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Data Storage:** Excel (`openpyxl`, `pandas`)
* **Authentication:** CSV file
* **Deployment:** Localhost (Flask Dev Server)

---

## 📁 Project Structure

```
EduLog/
│
├── app.py
├── README.md
│
├── data/
│   ├── users.csv
│   └── responses.xlsx
│
├── templates/
│   ├── index.html
│   ├── login.html
│   └── dashboard.html
│
├── static/
│   └── css/
│       └── style.css
│
└── venv/
```

---

## ⚙️ Installation & Setup

1. **Clone or extract the project**
2. **Create virtual environment**

   ```bash
   python -m venv venv
   ```
3. **Activate venv**

   ```bash
   venv\Scripts\activate
   ```
4. **Install dependencies**

   ```bash
   pip install flask pandas openpyxl
   ```
5. **Run the app**

   ```bash
   python app.py
   ```
6. Open browser → `http://127.0.0.1:5000`

---

## 🔑 Login Credentials

Stored in:

```
data/users.csv
```

Format:

```
username,password,role
```

Example:

```
sauvik_deb,admin@321,CEO
```

---

## 📊 Data Storage

* All submitted meetings are stored in:

```
data/responses.xlsx
```

* Start & End times are saved as **real Excel time values**
* File can be shared securely via **OneDrive (View/Edit access control)**

---

## 🔒 Access Control (Excel)

* Excel file is uploaded to **OneDrive**
* Access limited to **selected members only**
* Others cannot view or edit the data

---

## 📌 Future Enhancements

* Role-based dashboard access
* Cloud database (MySQL / Firebase)
* PDF export of meeting logs
* Analytics dashboard

---

## 👩‍💻 Author

**Nivethitha R**
AI & Data Science | Flask | Excel Automation

