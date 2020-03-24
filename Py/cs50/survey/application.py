import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    if not request.form.get("firstName") or not request.form.get("lastName"):
        return render_template("error.html", message="Error submitting survey.")
    elif request.form["boolSibs"] == "checker":
        if not request.form.get("numSibs"):
            return render_template("error.html", message="Error submitting survey.")
    with open("survey.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["firstName", "lastName", "numSibs"])
        writer.writerow({"firstName": request.form.get("firstName"), "lastName": request.form.get("lastName"), "numSibs": request.form.get(
            "numSibs") or "0"})
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    with open("survey.csv", "r") as file:
        reader = csv.DictReader(file)
        users = list(reader)
    return render_template("sheet.html", users=users)
