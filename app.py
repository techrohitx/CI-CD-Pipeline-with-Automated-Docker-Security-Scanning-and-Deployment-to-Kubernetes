from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Secure DevOps App</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #1e3c72, #2a5298);
                color: white;
                text-align: center;
            }
            .container {
                margin-top: 150px;
            }
            h1 {
                font-size: 50px;
                margin-bottom: 20px;
            }
            p {
                font-size: 20px;
                opacity: 0.9;
            }
            .btn {
                margin-top: 30px;
                padding: 12px 25px;
                font-size: 18px;
                border: none;
                border-radius: 25px;
                background-color: #ff9800;
                color: white;
                cursor: pointer;
                transition: 0.3s;
            }
            .btn:hover {
                background-color: #e68900;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1> Secure DevOps App</h1>
            <p>Jenkins + Docker + Kubernetes + Trivy</p>
            <button class="btn" onclick="alert('App is Running Securely!')">
                Check Status
            </button>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)