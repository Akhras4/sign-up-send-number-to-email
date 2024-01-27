from flask import Flask,render_template,request

app = Flask(__name__)
app.secret_key = "123qaz"
@app.route('/')
def home1():
    return render_template("indix.html", content="")


@app.route("/X.html", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        passworduser = request.form["password"]
        berth = request.form["berth"]
        username = request.form["username"]
        more = request.form["more"]
        findyourX = request.form["findyourX"]
        personalizeads = request.form["personalizeads"]
        import mysql.connector
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0000",
            database="profile",
        )
        mycursor = mydb.cursor()
        n = "SELECT username FROM xuserinfo"
        m = "SELECT email FROM xuserinfo "
        mycursor.execute(n)
        myresult = mycursor.fetchall()
        for x in myresult:
            if x == (username,):
                return render_template("X.html", msname=" username is already exist")

            mycursor.execute(m)
            myresult1 = mycursor.fetchall()
            for y in myresult1:
                if y == (email,):
                    return render_template("X.html", msemail=" email has already Used")

        else:
            import random
            number1 = random.randint(1001, 9999)
            import smtplib, ssl
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            sender_email = "******@gmail.com"
            receiver_email = email
            appPassword = "*******"
            message = MIMEMultipart("alternative")
            message["Subject"] = "multipart test"
            message["From"] = sender_email
            message["To"] = receiver_email
            text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
            f'{number1}'
            html = f'{number1}' """\
            <html>
              <body>
                <p>Hi,<br>
                   the number<br>
                </p>
              </body>
            </html>
            """
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
            message.attach(part1)
            message.attach(part2)
            # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, appPassword)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )
                session['name'] = name
                session['email'] = email
                session['password'] = passworduser
                session['berth'] = berth
                session["username"] = username
                session['getmoreoutofx'] = more
                session['Connectwithpeopleyouknow'] = findyourX
                session["Personalizedads"] = personalizeads
            return render_template("X.html")
    else:
        return render_template("X.html")



if __name__ == '__main__':
    app.run(host="localhost", port="2003", debug=True)
