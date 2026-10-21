from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = [
    {
        "name": "Gaurav Gade",
        "email": "gaurav@example.com",
        "branch": "Information Technology",
        "cgpa": "9.50",
        "company": "Prescient Technologies",
        "status": "Shortlisted"
    },
    {
        "name": "Akshada Pawar",
        "email": "akshada@example.com",
        "branch": "Computer Science",
        "cgpa": "8.40",
        "company": "TCS",
        "status": "Shortlisted"
    }
]


@app.route("/")
def index():
    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add_student():
    student = {
        "name": request.form["name"],
        "email": request.form["email"],
        "branch": request.form["branch"],
        "cgpa": request.form["cgpa"],
        "company": request.form["company"],
        "status": request.form["status"]
    }

    students.append(student)

    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete_student(index):
    if 0 <= index < len(students):
        students.pop(index)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)