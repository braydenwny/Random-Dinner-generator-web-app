from flask import Blueprint, redirect, render_template, request, session, url_for
import random
import pandas as pd
import json

pd.DataFrame()
meals = pd.read_json("website/dinners.JSON")

dinner = Blueprint("dinner", __name__)

global prevDinner
prevDinner = ""


@dinner.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        whereOptions = request.form.get("where")
        typeOptions = request.form.getlist("type")

        session["checkbox"] = whereOptions
        session["radio"] = typeOptions
        session["lastDinner"] = session.get("lastDinner", None)
        narrowedDown = meals

        if whereOptions:
            narrowedDown = narrowedDown[narrowedDown["where"] == str(whereOptions)]

        if typeOptions:
            narrowedDown = narrowedDown[narrowedDown["type"].isin(typeOptions)]

        randDinner = narrowedDown.sample(n=1)["meal"].values[0]

        if session['lastDinner']:
            while session['lastDinner'] == randDinner:
                randDinner = narrowedDown.sample(n=1)['meal'].values[0]
        session['lastDinner'] = randDinner

    whereOptions = session['checkbox']
    typeOptions = session['radio']


    return render_template('index.html', text=randDinner, whereOptions=whereOptions, typeOptions = typeOptions)

        return render_template('index.html', whereOptions=whereOptions, typeOptions = typeOptions)