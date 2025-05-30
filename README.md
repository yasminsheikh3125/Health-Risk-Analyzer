HEALTH RISK PREDICTOR DASHBOARD:
-
Description
-
Health Risk Predictor Dashboard is an interactive Streamlit app that allows users
to input personal health information and get an immediate prediction of their health 
risk level (Low, Medium, or High). The app also stores all inputs and predictions, 
enabling users to view the historical health data and visualize risk distribution trends.

Features:
-
-User-friendly form for entering health-related parameters
-Risk prediction based on simple heuristic scoring
-Saves user data and predictions locally in a CSV file
-View and analyze accumulated health data with tabular display and bar chart
-Real-time feedback and warnings for incomplete inputs

Installation:
-
1. Clone this repository:

git clone https://github.com/yasminsheikh3125/Health-Risk-Analyzer.git

2. Create and activate a virtual environment (optional but recommended):

-python -m venv venv
-source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required packages:

-pip install -r requirements.txt

Usage
-
-To run the app, execute:
streamlit run app.py

-Select Check My Health Risk to enter your details and get a risk prediction.
-Select View Health Data & Stats to see all saved entries and a bar chart of risk levels.

Technologies Used:
-
-Python 3.x
-Streamlit (for interactive UI)
-Pandas (for data handling)
-CSV module (for simple data persistence)

License
This project is licensed under the MIT License. See the LICENSE file for details.
