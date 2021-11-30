import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("index.html", tasks=tasks)


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/alltask")
def alltask():
    tasks = list(mongo.db.tasks.find())
    return render_template("profile_alltask.html", tasks=tasks)


@app.route("/mytasks")
def mytasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("profile_mytasks.html", tasks=tasks)


@app.route("/get_users")
def get_users():
    users = list(mongo.db.users.find())
    return render_template("profile.html", users=users)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("profile_alltask.html", tasks=tasks)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "danger")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "age": request.form.get("age").lower(),
            "address_l1": request.form.get("address_l1").lower(),
            "address_l2": request.form.get("address_l2").lower(),
            "city": request.form.get("city").lower(),
            "postcode": request.form.get("postcode").lower(),
            "cell": request.form.get("cell"),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!", "success")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password", "danger")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    user = mongo.db.users.find_one(
        {"username": session["user"].lower()})

    if request.method == "POST":
        mongo.db.users.update_many(
            {"username": user["username"]},
            {"$set": {"username": request.form.get("username").lower(),
                      "fname": request.form.get("fname"),
                      "lname": request.form.get("lname"),
                      "age": int(request.form.get("age")),
                      "address_l1": request.form.get("address_l1"),
                      "address_l2": request.form.get("address_l2"),
                      "city": request.form.get("city"),
                      "postcode": int(request.form.get("postcode")),
                      "cell": request.form.get("cell"),
                      "email": request.form.get("email")}})

        flash("Your Profile Has Been Updated", "success")
        session["user"] = request.form.get("username").lower()
        username = user["username"]

        return redirect(url_for("profile", username=username, user=user))

    return render_template(
        "profile.html",
        username=user["username"], user=user)   


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out", "success")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/new_task", methods=["GET", "POST"])
def new_task():
    if request.method == "POST":
        is_car = "on" if request.form.get("is_car") else "off"
        is_outdoor = "on" if request.form.get("is_outdoor") else "off"
        is_heavy_lift = "on" if request.form.get("is_heavy_lift") else "off"

        task = {
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "compensation": request.form.get("compensation"),
            "due_date": request.form.get("due_date"),
            "duration": request.form.get("duration"),
            "comment": request.form.get("comment"),
            "created_by": session["user"],
            "bestcontact_requester": request.form.get("bestcontact_requester"),
            "is_car": is_car,
            "is_outdoor": is_outdoor,
            "is_heavy_lift": is_heavy_lift,
        }
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Added", "success")
        return redirect(url_for("new_task"))

    return render_template("profile_new_task.html")


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted", "success")
    return redirect(url_for("alltask"))


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        is_car = "on" if request.form.get("is_car") else "off"
        is_outdoor = "on" if request.form.get("is_outdoor") else "off"
        is_heavy_lift = "on" if request.form.get("is_heavy_lift") else "off"

        submit = {
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "compensation": request.form.get("compensation"),
            "due_date": request.form.get("due_date"),
            "duration": request.form.get("duration"),
            "comment": request.form.get("comment"),
            "created_by": session["user"],
            "bestcontact_requester": request.form.get("bestcontact_requester"),
            "is_car": is_car,
            "is_outdoor": is_outdoor,
            "is_heavy_lift": is_heavy_lift
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Task Successfully Updated", "success")

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    return render_template("profile_edit_task.html", task=task)


@app.route("/apply_for_task/<task_id>", methods=["GET", "POST"])
def apply_for_task(task_id):
    if request.method == "POST":
        is_car = "on" if request.form.get("car_needed") == "YES" else "off"
        is_outdoor = "on" if request.form.get(
            "outdoor_needed") == "YES" else "off"
        is_heavy_lift = "on" if request.form.get(
            "heavy_lift_needed") == "YES" else "off"

        submit = {
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "compensation": request.form.get("compensation"),
            "due_date": request.form.get("due_date"),
            "duration": request.form.get("duration"),
            "comment": request.form.get("comment"),
            "created_by": request.form.get("created_by"),
            "bestcontact_provider": request.form.get("bestcontact_provider"),
            "is_car": is_car,
            "is_outdoor": is_outdoor,
            "is_heavy_lift": is_heavy_lift,
            "is_booked": "on",
            "booked_by": session["user"]            
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Applied Successfully", "success")

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    return render_template("profile_apply_task.html", task=task)


@app.route("/about")
def about():
    return render_template("about.html")

@app.errorhandler(404)
def not_found(e):
    """
        Render 404 page if errors occur
        Code credit to Carla Buongiorno (The Collector project)
        https://github.com/CarlaBuongiorno/The-Collector
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(e):
    """
        Render 500 page if errors occur
        Code credit to Carla Buongiorno (The Collector project)
        https://github.com/CarlaBuongiorno/The-Collector
    """
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
