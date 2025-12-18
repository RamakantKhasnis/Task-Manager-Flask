from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from models import db, Task
import os

def create_app():
    app = Flask(__name__)

    # SQLite DB in instance folder
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "instance", "taskmanager.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Make sure instance folder exists
    os.makedirs(os.path.join(basedir, "instance"), exist_ok=True)

    db.init_app(app)

    # Create tables once when app starts
    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        tasks = Task.query.order_by(Task.due_date.asc().nullslast()).all()
        return render_template("index.html", tasks=tasks)

    @app.route("/add", methods=["GET", "POST"])
    def add_task():
        if request.method == "POST":
            title = request.form.get("title")
            description = request.form.get("description")
            due_date_str = request.form.get("due_date")

            if not title:
                return "Title is required", 400

            due_date = None
            if due_date_str:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

            new_task = Task(
                title=title,
                description=description,
                due_date=due_date,
                completed=False
            )
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("index"))

        return render_template("add_task.html")

    @app.route("/edit/<int:task_id>", methods=["GET", "POST"])
    def edit_task(task_id):
        task = Task.query.get_or_404(task_id)

        if request.method == "POST":
            task.title = request.form.get("title")
            task.description = request.form.get("description")
            due_date_str = request.form.get("due_date")
            completed = request.form.get("completed") == "on"

            if not task.title:
                return "Title is required", 400

            if due_date_str:
                task.due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            else:
                task.due_date = None

            task.completed = completed

            db.session.commit()
            return redirect(url_for("index"))

        return render_template("edit_task.html", task=task)

    @app.route("/delete/<int:task_id>", methods=["POST"])
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for("index"))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
