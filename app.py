from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_sales():
    print("Analyze endpoint hit")  # DEBUG

    if "file" not in request.files:
        print("No file in request")  # DEBUG
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    print("Received file:", file.filename)  # DEBUG

    try:
        df = pd.read_csv(file)
        print("CSV loaded, rows:", len(df))  # DEBUG

        df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
        df = df.dropna(subset=["Sales"])

        print("After cleaning, rows:", len(df))  # DEBUG

        result = {
            "summary": {
                "total_sales": round(df["Sales"].sum(), 2),
                "average_sales": round(df["Sales"].mean(), 2),
                "max_sales": round(df["Sales"].max(), 2)
            },
            "sales_by_category": df.groupby("Category")["Sales"].sum().round(2).to_dict(),
            "sales_by_region": df.groupby("Region")["Sales"].sum().round(2).to_dict()
        }

        print("Result prepared")  # DEBUG
        return jsonify(result)

    except Exception as e:
        print("ERROR:", e)  # DEBUG
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)
