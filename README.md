# Task Manager Flask

A simple task management web application built with **Flask**, **SQLite**, and **Bootstrap 5**.  
Users can create, update, mark as completed, and delete tasks through a clean, responsive UI.

## 🚀 Features

- Add tasks with title, description, and optional due date
- View all tasks in a card-based dashboard
- Edit tasks and mark them as completed
- Delete tasks with confirmation
- Status badges for **Pending** and **Done**
- SQLite database using SQLAlchemy ORM
- Responsive Bootstrap 5 layout

## 🛠 Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy  
- **Database:** SQLite  
- **Frontend:** HTML, Jinja2 templates, Bootstrap 5, Bootstrap Icons  

## 📂 Project Structure

task-manager-flask/
├── app.py # Main Flask application (routes, app factory)
├── models.py # Database models (Task)
├── requirements.txt # Python dependencies
├── instance/ # SQLite database (created at runtime, ignored by Git)
├── templates/ # Jinja2 HTML templates
│ ├── base.html # Base layout with navbar and container
│ ├── index.html # Task list (cards view)
│ ├── add_task.html # Add task form
│ └── edit_task.html # Edit task form
└── venv/ # Virtual environment (ignored by Git)


## ⚙️ Setup and Run (Local)

1. **Clone the repository**

git clone https://github.com/<your-username>/Task-Manager-Flask.git
cd Task-Manager-Flask


2. **Create and activate virtual environment (macOS / Linux)**

python3 -m venv venv
source venv/bin/activate


3. **Install dependencies**

pip install -r requirements.txt

4. **Run the app**

python app.py


The app will be available at:

http://127.0.0.1:5000


## 📸 Screenshots

> _Add screenshots here once you take them._

Example:

![Task dashboard](screenshots


## 🔮 Possible Improvements

- User authentication (login/signup, per-user tasks)
- Task categories / labels (Work, Personal, Study)
- Priority levels (Low / Medium / High)
- Search and filters (by status or date)
- Deploy to a cloud platform (Render, Railway, Heroku, etc.)

## 👤 Author

- **Ramakant Khasnis** – [@your-github](https://github.com/your-github)

Feel free to open issues or submit pull requests if you want to improve this project.
