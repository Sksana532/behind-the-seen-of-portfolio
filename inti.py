from flask import Flask,render_template, request,session,redirect, url_for
import uuid 
import os
import schedule
app = Flask(__name__,static_folder='static')
app.secret_key="secretkey"

@app.route("/")
def home():  
    return render_template("home.html")

@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/form1/<string:design>", methods=["GET", "POST"])
def form1(design):
    session["design_sess"] = design
    return render_template("form1.html")

@app.route("/design1")
def design1():
    return render_template("design1.html")

@app.route("/design2")
def design2():
    return render_template("design2.html")

@app.route("/design3")
def design3():
    return render_template("design3.html")

@app.route("/design4")
def design4():
    return render_template("design4.html")

@app.route("/design5")
def design5():
    return render_template("design5.html")

@app.route("/design6")
def design6():
    return render_template("design6.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    

    design_upload = session.get("design_sess")
    if design_upload == "design1":
        design_name = "design1.html"
    elif design_upload == "design2":
        design_name = "design2.html"
    elif design_upload == "design3":
        design_name = "design3.html"
    elif design_upload == "design4":
        design_name = "design4.html"

    if request.method == "POST":
        name = request.form.get("name")
        job_title = request.form.get("job_title")
        contact = request.form.get("contact")
        email = request.form.get("email")
        skill1 = request.form.get("skill1")
        skill2 = request.form.get("skill2")
        skill3 = request.form.get("skill3")
        skill4 = request.form.get("skill4")
        address = request.form.get("address")
        about_us = request.form.get("about_us")
        skill5 = request.form.get("skill5")
        skill6 = request.form.get("skill6")
        skill7 = request.form.get("skill7")
        skill8= request.form.get("skill8")
        project1 = request.form.get("project1")
        project2 = request.form.get("project2")
        uni = request.form.get("uni")
        clg = request.form.get("clg")
        about_project1 = request.form.get("about_project1")
        about_project2= request.form.get("about_project2")
        
        about_us = request.form.get("about_us")
        key=uuid.uuid1()
        about_eduation = request.form.get("about_education")
        instagram= request.form.get("instagram")
        github = request.form.get("github")

        
        print(name )
        print(job_title)
        print(contact )
        print(email )
        print(address )
        print(skill1 )
        print(skill2 )
        print(skill3 )
        print(skill4 )
        print(skill5 )
        print(skill6 )
        print(skill7 )
        print(skill8 )
        print(about_us)
        print(uni)
        print(clg)
        
        print(about_us )
        print(project1 )
        print(project2 )
        
        print(about_project1)
        print(about_project2)
        
        print(github)
        print(instagram)



    
        key = uuid.uuid1()  # Assuming you've imported the uuid module
        img = request.files["dp"]
        img.save(f"static/image/{img.filename}")
        img_new_name = f"{key}{img.filename}"
        os.rename(f"static/image/{img.filename}", f"static/image/{img_new_name}")


        


       


    return render_template(design_name, uni=uni, clg=clg, uinstagram=instagram, ugithub=instagram,
                               uname=name, img=img_new_name,
                               uemail=email, unumber=contact, uaddress=address, uskill1=skill1,
                               uskill2=skill2,uskill3=skill3, uskill4=skill4, uskill5=skill5,uskill6=skill6,
                                uskill7=skill7,uskill8=skill8, uproject1=project1, uproject2=project2,ujob_title=job_title,
                               aboutproject1=about_project1, aboutproject2=about_project2, uabout_us=about_us)
        
        








def delete():
    files =os.listdir("static/image")
    for f in files:
        os.remove(f"static/image/{f}")


if __name__ == "__main__":
    schedule.every().day.at("11:59").do(delete)
    app.run(debug=True)

        