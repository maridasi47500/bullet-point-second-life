from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,email,phone,country_id,password) values (:username,:email,:phone,:country_id,:password)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','email','phone','country_id','password']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','email','phone','country_id','password']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','email','phone','country_id','password']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_room", methods=["GET","POST"])
def add_one_room():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into room (name) values (:name)",hey)
        user = query_db('select * from room')

        return render_template("roomform.html", rooms=user, one_user=one_user, the_title="add new room")


    user = query_db('select * from room')
    one_user = query_db("select * from room limit 1", one=True)
    return render_template("roomform.html", rooms=user, one_user=one_user, the_title="add new room")

@app.route("/add_one_user_items_table", methods=["GET","POST"])
def add_one_user_items_table():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesroom= query_db("select * from room")

        one_user = query_db("insert into user_items_table (user_id,room_id,name) values (:user_id,:room_id,:name)",hey)
        user = query_db('select * from user_items_table')

        return render_template("user_items_tableform.html", user_items_tables=user, one_user=one_user, the_title="add new user_items_table", touslesuser=touslesuser, touslesroom=touslesroom)


    touslesuser= query_db("select * from user")

    touslesroom= query_db("select * from room")

    user = query_db('select * from user_items_table')
    one_user = query_db("select * from user_items_table limit 1", one=True)
    return render_template("user_items_tableform.html", user_items_tables=user, one_user=one_user, the_title="add new user_items_table", touslesuser=touslesuser, touslesroom=touslesroom)

@app.route("/add_one_user_job", methods=["GET","POST"])
def add_one_user_job():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesjob= query_db("select * from job")

        one_user = query_db("insert into user_job (user_id,job_id) values (:user_id,:job_id)",hey)
        user = query_db('select * from user_job')

        return render_template("user_jobform.html", user_jobs=user, one_user=one_user, the_title="add new user_job", touslesuser=touslesuser, touslesjob=touslesjob)


    touslesuser= query_db("select * from user")

    touslesjob= query_db("select * from job")

    user = query_db('select * from user_job')
    one_user = query_db("select * from user_job limit 1", one=True)
    return render_template("user_jobform.html", user_jobs=user, one_user=one_user, the_title="add new user_job", touslesuser=touslesuser, touslesjob=touslesjob)

@app.route("/add_one_user_ai_job", methods=["GET","POST"])
def add_one_user_ai_job():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesjob= query_db("select * from job")

        one_user = query_db("insert into user_ai_job (user_id,job_id) values (:user_id,:job_id)",hey)
        user = query_db('select * from user_ai_job')

        return render_template("user_ai_jobform.html", user_ai_jobs=user, one_user=one_user, the_title="add new user_ai_job", touslesuser=touslesuser, touslesjob=touslesjob)


    touslesuser= query_db("select * from user")

    touslesjob= query_db("select * from job")

    user = query_db('select * from user_ai_job')
    one_user = query_db("select * from user_ai_job limit 1", one=True)
    return render_template("user_ai_jobform.html", user_ai_jobs=user, one_user=one_user, the_title="add new user_ai_job", touslesuser=touslesuser, touslesjob=touslesjob)

@app.route("/add_one_bullet_point_workflows", methods=["GET","POST"])
def add_one_bullet_point_workflows():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesUser_Job= query_db("select * from User_Job")

        one_user = query_db("insert into bullet_point_workflows (User_Job_id,content) values (:User_Job_id,:content)",hey)
        user = query_db('select * from bullet_point_workflows')

        return render_template("bullet_point_workflowsform.html", bullet_point_workflowss=user, one_user=one_user, the_title="add new bullet_point_workflows", touslesUser_Job=touslesUser_Job)


    touslesUser_Job= query_db("select * from User_Job")

    user = query_db('select * from bullet_point_workflows')
    one_user = query_db("select * from bullet_point_workflows limit 1", one=True)
    return render_template("bullet_point_workflowsform.html", bullet_point_workflowss=user, one_user=one_user, the_title="add new bullet_point_workflows", touslesUser_Job=touslesUser_Job)

@app.route("/add_one_ai_job_link_table", methods=["GET","POST"])
def add_one_ai_job_link_table():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesUser_Ai_Job= query_db("select * from User_Ai_Job")

        one_user = query_db("insert into ai_job_link_table (User_Ai_Job,content) values (:User_Ai_Job,:content)",hey)
        user = query_db('select * from ai_job_link_table')

        return render_template("ai_job_link_tableform.html", ai_job_link_tables=user, one_user=one_user, the_title="add new ai_job_link_table", touslesUser_Ai_Job=touslesUser_Ai_Job)


    touslesUser_Ai_Job= query_db("select * from User_Ai_Job")

    user = query_db('select * from ai_job_link_table')
    one_user = query_db("select * from ai_job_link_table limit 1", one=True)
    return render_template("ai_job_link_tableform.html", ai_job_link_tables=user, one_user=one_user, the_title="add new ai_job_link_table", touslesUser_Ai_Job=touslesUser_Ai_Job)

