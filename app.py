import os

import openai
from flask import Flask, redirect, render_template, request, url_for

def create_app():
    app = Flask(__name__)
    openai.api_key = os.getenv("OPENAI_API_KEY")


    @app.route("/", methods=("GET", "POST"))
    def index():
        if request.method == "POST":
            temperature = float(request.form["temperature"])
            prompt = request.form["prompt"]
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=generate_prompt(prompt),
                temperature=temperature,
                max_tokens=2040,
                # stream=True,
            )
            return redirect(url_for("index", result=response.choices[0].text))

        result = request.args.get("result")
        return render_template("index.html", result=result)
    
    return app


def generate_prompt(prompt):
    return """ 
    {}
    """.format(
        prompt.capitalize()
    )

app = create_app()