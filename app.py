#!env/bin/python3
# -*- coding: utf-8 -*-
from quart import Quart, render_template

app = Quart(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
async def index():
    return await render_template("index.html")