from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def dashboard():
    df = pd.read_scv("tetris_sales.csv")
    total_sales = df["Total"].sum()
    return render_template("dashboard.html", table=df.to_html(classes='table table-striped', index=False), total=total_sales)

if __name__=="__main__":
    app.run(debug=True)
