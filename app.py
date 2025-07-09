from flask import Flask, render_template, request
import plotly.express as px
from data_utils import load_and_transform_data

app = Flask(__name__)

@app.route('/')
def index():
    df = load_and_transform_data("dashboard_data.csv")

    # 🧠 Get dropdown values
    selected_region = request.args.get("region", "All")
    selected_shape = request.args.get("blockshape", "All")

    # 🧼 Apply filters
    if selected_region != "All":
        df = df[df["Region"] == selected_region]
    if selected_shape != "All":
        df = df[df["BlockShape"] == selected_shape]

    # 📊 Bar chart
    bar_fig = px.bar(df, x="Region", y="Revenue", color="BlockShape", title="Revenue by Region and BlockShape")
    bar_html = bar_fig.to_html(full_html=False)

    # 📊 Pie chart
    pie_fig = px.pie(df, names="BlockShape", values="Revenue", title="Revenue Distribution by BlockShape")
    pie_html = pie_fig.to_html(full_html=False)

    # 📋 Dropdown lists
    all_regions = sorted(df["Region"].unique().tolist())
    all_regions.insert(0, "All")

    all_shapes = sorted(df["BlockShape"].unique().tolist())
    all_shapes.insert(0, "All")

    return render_template("index.html",
                           bar_html=bar_html,
                           pie_html=pie_html,
                           selected_region=selected_region,
                           selected_shape=selected_shape,
                           all_regions=all_regions,
                           all_shapes=all_shapes)

if __name__ == "__main__":
    app.run(debug=True)