from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
import os

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
            # Prepare email
            msg = MIMEText(f"Message from {name} ({email}):\n\n{message}")
            msg["Subject"] = "New Contact Form Message"
            msg["From"] = email
            msg["To"] = os.environ.get("EMAIL_USER")  # send to your Gmail

            # Connect to Gmail SMTP
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASS"))
            server.sendmail(email, os.environ.get("EMAIL_USER"), msg.as_string())
            server.quit()

            flash("✅ Thank you! Your message has been sent.", "success")
        except Exception as e:
            flash("❌ Oops! Something went wrong.", "danger")
            print("Error:", e)

        return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    # Bind to port 0.0.0.0 for Heroku
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
