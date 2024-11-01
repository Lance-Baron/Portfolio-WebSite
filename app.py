from flask import Flask, render_template

app = Flask(__name__,static_folder=r"D:\Programs\Portfolio WebSite\static",template_folder=r"D:\Programs\Portfolio WebSite\static\templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/about-me")
def about_me():
    return render_template("aboutMe.html")

@app.route("/contact-me")
def contact_me():
    return render_template("contactMe.html")

# @app.errorhandler(404)
# def noPage():
#     return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)