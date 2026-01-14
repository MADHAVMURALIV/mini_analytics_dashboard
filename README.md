# Mini Sales Analytics Dashboard

A lightweight web-based analytics dashboard that allows users to upload a sales dataset and instantly view key insights and visualizations.  
Built to demonstrate fast execution, clean UI, and practical data analysis under time constraints.

---

## Features

- Upload a CSV sales dataset
- Region-based filtering (All, Central, East, South, West)
- Key summary metrics:
  - Total Sales
  - Average Sales
  - Maximum Sale
- Interactive visualizations:
  - Total Sales by Category (Bar Chart)
  - Sales Distribution by Region (Doughnut Chart)
  - Category Share of Revenue (Doughnut Chart)
  - Sales Trend (Average vs Max of first 10 records)
- Dynamic insights generated from data
- Dark / Light theme toggle
- Live date and time display
- Processing animation during analysis
- Downloadable PDF report including charts and metrics
- Simple landing page with navigation to dashboard

---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Charts:** Chart.js
- **Backend:** Python, Flask
- **Data Processing:** Pandas
- **PDF Export:** jsPDF
- **Styling:** Custom CSS (Dark & Light themes)

---

## Project Structure

project/
│
├── app.py
│
├── templates/
│ ├── landing.html
│ └── index.html
│
└── README.md


---

## Dataset Requirements

The uploaded CSV file must contain the following columns:

- `Sales`
- `Category`
- `Region`

(Additional columns such as Year, Month, Sub-Category, etc. are supported but optional.)

---

## Setup & Run Instructions

1. Clone the repository
2. Install required dependencies:
   ```
   pip install flask flask-cors pandas

3. Run the application

python app.py

4 .The application will automatically open in your browser at:

  http://127.0.0.1:5000/


Usage Flow

1.Open the landing page

2.Click Open Dashboard

3.Upload a sales CSV file

4.(Optional) Apply region filter

5.Click Analyze

6.View metrics, charts, and insights

7.Download the PDF report if required



Insights Generated

1.Identification of top-performing sales category

2.Revenue contribution across regions

3.Comparison between average and maximum sales

4.Detection of high-value transactions



Notes

-> The application focuses on clarity and functionality over heavy styling

-> Designed to be completed and demonstrated within a short time window

-> Suitable for quick analytics and exploratory insights



## UI and OUTPUTS

<img width="1919" height="909" alt="Screenshot 2026-01-14 115026" src="https://github.com/user-attachments/assets/47d59926-97bb-40bf-919b-d5ba4fe45e15" />
<img width="1895" height="905" alt="Screenshot 2026-01-14 115841" src="https://github.com/user-attachments/assets/bf22d5f1-2d20-4b46-83be-fda03076096c" />
<img width="1894" height="903" alt="Screenshot 2026-01-14 115907" src="https://github.com/user-attachments/assets/c84601ce-29c7-4f9f-a419-74254a310045" />
<img width="1893" height="882" alt="Screenshot 2026-01-14 115939" src="https://github.com/user-attachments/assets/a3f8bec7-a781-4806-b179-28a4209fa791" />
<img width="1900" height="1027" alt="Screenshot 2026-01-14 115919" src="https://github.com/user-attachments/assets/732ca13b-7b66-479d-9e89-bff118904c3f" />
<img width="795" height="600" alt="Screenshot 2026-01-14 120009" src="https://github.com/user-attachments/assets/b81d51cb-5fbd-46db-9885-6469accb500d" />
<img width="804" height="811" alt="Screenshot 2026-01-14 120015" src="https://github.com/user-attachments/assets/784ad358-0725-4ad5-a23c-7ba3d2dacd10" />
<img width="806" height="825" alt="Screenshot 2026-01-14 120020" src="https://github.com/user-attachments/assets/689c63a5-4875-4d46-beb3-a9562b3be321" />
