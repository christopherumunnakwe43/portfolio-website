from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "secret123")  # safer

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        try:
            # Prepare email
            msg = MIMEText(f"Message from {name} ({email}):\n\n{message}")
            msg["Subject"] = "New Contact Form Message"
            msg["From"] = os.environ.get("EMAIL_USER")
            msg["To"] = os.environ.get("EMAIL_RECEIVER")  # who receives the mail

            # Send email
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASS"))
                server.send_message(msg)

            flash("✅ Thank you! Your message has been sent successfully.", "success")
        except Exception as e:
            flash("❌ Internal error while sending your message.", "danger")
            print("Error:", e)

        return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
