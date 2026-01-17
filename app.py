from flask import Flask, render_template, request, redirect
import csv
import pandas as pd
import os
from datetime import datetime, time

app = Flask(__name__)

# ---------- HELPER FUNCTION ----------
def to_24hr_time(hour, minute, ampm):
    if not hour or not minute or not ampm:
        return None

    hour = int(hour)
    minute = int(minute)

    if ampm == "PM" and hour != 12:
        hour += 12
    if ampm == "AM" and hour == 12:
        hour = 0

    return time(hour, minute)


# ---------------- HOME ----------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        with open("data/users.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username and row["password"] == password:
                    return redirect("/dashboard")

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":

        start_time = to_24hr_time(
            request.form.get("Start_Time"),
            request.form.get("Start_Minute"),
            request.form.get("Start_AMPM")
        )

        end_time = to_24hr_time(
            request.form.get("End_Time"),
            request.form.get("End_Minute"),
            request.form.get("End_AMPM")
        )

        data = {
            "Date_of_Meeting": request.form.get("Date_of_Meeting"),
            "Department": request.form.get("Department"),
            "Meeting_Type": request.form.get("Meeting_Type"),
            "Meeting_Mode": request.form.get("Meeting_Mode"),
            "Objective": request.form.get("Objective"),
            "Agenda": request.form.get("Agenda"),
            "Start_Time": start_time,
            "End_Time": end_time,
            "Attendees": ", ".join(request.form.getlist("Attendees")),
            "Absentees": ", ".join(request.form.getlist("Absentees")),
            "Absence_Reason": request.form.get("Absence_Reason"),
            "Key_Decisions": request.form.get("Key_Decisions"),
            "Productive": request.form.get("Productive"),
            "Productivity_Issue": request.form.get("Productivity_Issue"),
            "Blockers": request.form.get("Blockers"),
            "Follow_Up": request.form.get("Follow_Up"),
            "Follow_Up_Date": request.form.get("Follow_Up_Date"),
            "Submitted_By": request.form.get("Submitted_By"),
            "Department_Head": request.form.get("Department_Head"),
            "Timestamp": datetime.now()
        }

        print("FORM DATA RECEIVED:", data)

        os.makedirs("data", exist_ok=True)
        excel_path = os.path.join("data", "responses_data.xlsx")

        if os.path.exists(excel_path):
            df_existing = pd.read_excel(excel_path)
            df = pd.concat([df_existing, pd.DataFrame([data])], ignore_index=True)
        else:
            df = pd.DataFrame([data])

        # ✅ CORRECTLY INDENTED WITH BLOCK
        with pd.ExcelWriter(
            excel_path,
            engine="openpyxl",
            mode="w"
        ) as writer:
            df.to_excel(writer, index=False)

        return render_template("dashboard.html", success=True)

    return render_template("dashboard.html")


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
