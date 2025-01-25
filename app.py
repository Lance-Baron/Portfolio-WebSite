from flask import Flask, render_template

app = Flask(__name__,static_folder=r"static",template_folder=r"static\templates")

app.config["proj_path"] = r"static\templates\projects"

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

def findDesc(fileName:str) -> str:
    import os

    description:str = ""
    for root, dirs, files in os.walk(app.config["proj_path"]): #Adds all of the files that are in the given path to a list
        for file in files:
            if file == fileName:
                with open(f"{app.config['proj_path']}\{fileName}","r") as proj_file: 
                    for line in proj_file:
                        if 'id="pro-desc"' in line:
                            description = line
                            break
    description = description.replace('<p id="pro-desc">',"")
    description = description.replace('</p>',"")
    return description

def makeBetterWords(path:str = app.config["proj_path"]) -> list[list[str]]:
    """Here to get data for listing each project file in templates""" 
    foundFiles:list[str] = findFiles(path)

    finalData = [[],[],[]]
    for file in foundFiles: #Changes files names to normal words
        words = file.split("_")
        formatedName = ""
        for word in words:
            formatedName += word.replace(".html","").capitalize() + " "
        desc = findDesc(file)
        tempList = [file,formatedName,desc]
        finalData.append(tempList)

    return finalData
    
def findFiles(path:str=r"static\templates\projects") -> list[str]:
    import os
    foundFiles = []

    for root, dirs, files in os.walk(path): #Adds all of the files that are in the given path to a list
        for file in files:
            foundFiles.append(file)  
    
    return foundFiles

if __name__ == "__main__":
    # files = findFiles()
    # for file in files:
    #     print(findDesc(file))
    app.run()