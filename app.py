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
    return render_template("profile_alltask.html", tasks=tasks)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("profile.html", tasks=tasks)


@app.route("/home")
def home():
    tasks = mongo.db.tasks.find()
    return render_template("index.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
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
            "cell": request.form.get("cell").lower(),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
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
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    fname = mongo.db.users.find_one(
        {"username": session["user"]})["fname"]
    lname = mongo.db.users.find_one(
        {"username": session["user"]})["lname"]
    address_l1 = mongo.dlname = mongo.db.users.find_one(
        {"username": session["user"]})["lname"]
    address_l1 = mongo.db.users.find_one(
        {"username": session["user"]})["address_l1"]
    address_l2 = mongo.db.users.find_one(
        {"username": session["user"]})["address_l2"]
    city = mongo.db.users.find_one(
        {"username": session["user"]})["city"]
    postcode = mongo.db.users.find_one(
        {"username": session["user"]})["postcode"]
    cell = mongo.db.users.find_one(
        {"username": session["user"]})["cell"]
    email = mongo.db.users.find_one(
        {"username": session["user"]})["email"]

    if session["user"]:
        return render_template("profile.html", 
            username=username, fname=fname,
            lname=lname, address_l1=address_l1, 
            address_l2=address_l2, city=city, 
            postcode=postcode, cell=cell, email=email)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
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
            "is_car": is_car,
            "is_outdoor": is_outdoor,
            "is_heavy_lift": is_heavy_lift,
            "is_booked": "off"
        }
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Added")
        return redirect(url_for("get_tasks"))

    return render_template("profile_new_task.html")


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))


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
            "is_car": is_car,
            "is_outdoor": is_outdoor,
            "is_heavy_lift": is_heavy_lift,
            "is_booked": "off"
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Task Successfully Updated")

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    return render_template("profile_edit_task.html", task=task)


@app.route("/apply_for_task/<task_id>", methods=["GET", "POST"])
def apply_for_task(task_id):
    if request.method == "POST":
        is_car = "on" if request.form.get("car_needed") == "YES" else "off"
        is_outdoor = "on" if request.form.get("outdoor_needed") == "YES" else "off"
        is_heavy_lift = "on" if request.form.get("heavy_lift_needed") == "YES" else "off"

        submit = {
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "compensation": request.form.get("compensation"),
            "due_date": request.form.get("due_date"),
            "duration": request.form.get("duration"),
            "comment": request.form.get("comment"),
            "created_by": request.form.get("created_by"),
            "is_car": is_car,
            "is_outdoor": is_outdoor,
            "is_heavy_lift": is_heavy_lift,
            "is_booked": "on",
            "booked_by": session["user"],
            "comment_helper": request.form.get("comment_helper")
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Applied Successfully")

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    return render_template("profile_apply_task.html", task=task)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
