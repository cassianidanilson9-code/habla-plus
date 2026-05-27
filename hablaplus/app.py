from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("TU_CORREO@gmail.com", "TU_APP_PASSWORD")

        subject = "Nuevo mensaje Habla+"
        text = f"Nombre: {name}\nEmail: {email}\nMensaje: {message}"

        msg = f"Subject: {subject}\n\n{text}"

        server.sendmail("TU_CORREO@gmail.com", "TU_CORREO@gmail.com", msg)
        server.quit()

        return "Mensaje enviado ✔"
    except:
        return "Error al enviar ❌"

if __name__ == "__main__":
    app.run(debug=True)
