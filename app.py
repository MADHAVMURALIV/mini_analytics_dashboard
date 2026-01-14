from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import webbrowser

app = Flask(__name__)
CORS(app)

# landing route 
@app.route("/")
def landing():
    return render_template("landing.html")


# dashboard route 
@app.route("/dashboard")
def dashboard():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_sales():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    try:
        df = pd.read_csv(file)
        df.columns = df.columns.str.strip()

        required_cols = {"Sales", "Category", "Region"}
        if not required_cols.issubset(df.columns):
            return jsonify({
                "error": f"CSV must contain columns: {list(required_cols)}"
            }), 400

        region = request.form.get("region", "All")
        if region != "All":
            df = df[df["Region"] == region]

        df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
        df = df.dropna(subset=["Sales"])

        if df.empty:
            return jsonify({"error": "No data after filtering"}), 400

        result = {
            "summary": {
                "total_sales": round(df["Sales"].sum(), 2),
                "average_sales": round(df["Sales"].mean(), 2),
                "max_sales": round(df["Sales"].max(), 2)
            },
            "sales_by_category": (
                df.groupby("Category")["Sales"]
                .sum().round(2).to_dict()
            ),
            "sales_by_region": (
                df.groupby("Region")["Sales"]
                .sum().round(2).to_dict()
            ),
            "first_10_sales": (
                df["Sales"].head(10).round(2).tolist()
            ),
            "applied_region": region
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True, use_reloader=False)
