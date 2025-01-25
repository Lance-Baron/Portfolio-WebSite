from flask import Flask, render_template

app = Flask(__name__,static_folder=r"static",template_folder=r"static\templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html",data=makeBetterWords())

@app.route("/<id>")
def default_render(id):
    return render_template(id+".html")

@app.route("/projects/<id>")
def default_project_render(id):
    return render_template("projects/"+id)

@app.errorhandler(404)
def noPage(error):
    return render_template("index.html")

def makeBetterWords(path:str=r"static\templates\projects") -> dict[str]:
    """Here to get data for listing each project file in templates""" 
    import os
    foundFiles = []
    for root, dirs, files in os.walk(path):
        for file in files:
            foundFiles.append(file)  

    formatedNames = []
    for file in foundFiles:
        words = file.split("_")
        formatedName = ""
        for word in words:
            formatedName += word.replace(".html","").capitalize() + " "
        formatedNames.append(formatedName.strip())

    dict = {formatedNames[i]: foundFiles[i] for i in range(len(foundFiles))}
    return dict
    
if __name__ == "__main__":
    app.run(debug=True)
