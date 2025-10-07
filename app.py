from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "secret123"  # for flash messages

# Home route
@app.route("/")
def home():
    return render_template("home.html")

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        try:
            # Setup email
            msg = MIMEText(f"Message from {name} ({email}):\n\n{message}")
            msg["Subject"] = "New Contact Form Message"
            msg["From"] = email
            msg["To"] = "christopherumunnakwe43@gmail.com"

            # Connect to Gmail SMTP
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("christopherumunnakwe43@gmail.com", "xfuu qvko vxpk mipt")
            server.sendmail(email, "christopherumunnakwe43@gmail.com", msg.as_string())
            server.quit()

            flash("✅ Thank you! Your message has been sent.", "success")
        except Exception as e:
            flash("❌ Oops! Something went wrong.", "danger")
            print("Error:", e)

        return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
