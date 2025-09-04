from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Chaudhary E-Ciggs</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; margin:0; padding:0; }
        header { background:#111; color:white; padding:20px; text-align:center; }
        nav { background:#222; padding:10px; text-align:center; }
        nav a { color:white; margin:0 10px; text-decoration:none; font-weight:bold; display:inline-block; }
        nav a:hover { color:#ffcc00; }
        section { padding:50px 20px; text-align:center; }
        .vapes { background:#f8f8f8; }
        .pods { background:#e0e0e0; }
        .flavours { background:#cfcfcf; }
        footer { background:#111; color:white; padding:15px; text-align:center; }
        h1 { font-size: 28px; margin:10px; }
        h2 { font-size:24px; margin:10px; }
        p { font-size:16px; margin:5px; }
        @media (max-width:600px){
            nav a { display:block; margin:5px 0; }
            h1 { font-size:24px; }
            h2 { font-size:20px; }
            p { font-size:14px; }
        }
    </style>
</head>
<body>
    <header>
        <h1>Chaudhary E-Ciggs</h1>
        <p>Your one-stop shop for Vapes, Pods & Flavours</p>
    </header>
    <nav>
        <a href="#vapes">Vapes</a>
        <a href="#pods">Pods</a>
        <a href="#flavours">Flavours</a>
    </nav>
    <section id="vapes" class="vapes">
        <h2>Vapes</h2>
        <p>Explore our latest vapes collection with top-notch quality.</p>
    </section>
    <section id="pods" class="pods">
        <h2>Pods</h2>
        <p>Check out our durable and premium pods.</p>
    </section>
    <section id="flavours" class="flavours">
        <h2>Flavours</h2>
        <p>Discover unique vape flavours to suit your taste.</p>
    </section>
    <footer>
        <p>&copy; 2025 Chaudhary E-Ciggs</p>
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
