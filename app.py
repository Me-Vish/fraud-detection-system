from flask import Flask, request, render_template_string, redirect, url_for
import joblib
import pandas as pd
import os

app = Flask(__name__)

model = joblib.load("fraud_model.pkl")

HISTORY_FILE = "history.csv"

if not os.path.exists(HISTORY_FILE):
    pd.DataFrame(columns=["amount","Result"]).to_csv(HISTORY_FILE,index=False)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Fraud Detection</title>
<style>
body {
    font-family: Arial;
    background: url('/static/bg.jpg') no-repeat center center fixed;
    background-size: cover;
    color:white;
    display:flex;
    justify-content:center;
    align-items:center;
    min-height:100vh;
}

.card {
    background: rgba(17,24,39,0.85);
    backdrop-filter: blur(6px);
    padding:25px;
    border-radius:12px;
    width:450px;
    text-align:center;
}

input {
    width:90%;
    padding:10px;
    margin-top:10px;
    border-radius:6px;
}

button {
    margin-top:10px;
    padding:10px;
    background:#2563eb;
    border:none;
    color:white;
    border-radius:6px;
    cursor:pointer;
}

.clear {
    background:#dc2626;
}

table {
    width:100%;
    margin-top:15px;
    border-collapse:collapse;
}

th,td {
    padding:6px;
    border-bottom:1px solid #333;
}

.green {color:#22c55e;}
.red {color:#ef4444;}
</style>
</head>

<body>
<div class="card">

<h2>Fraud Detection System</h2>

<form method="post">
<input type="number" step="any" name="amount" placeholder="Enter Transaction Amount" required>
<button type="submit">Check Transaction</button>
</form>

<form action="/clear" method="post">
<button class="clear">Clear History</button>
</form>

{% if result %}
<h3 class="{{color}}">Result: {{result}}</h3>
{% endif %}

<h3>Transaction History</h3>

<table>
<tr><th>Amount</th><th>Status</th></tr>
{% for row in history %}
<tr>
<td>{{row.amount}}</td>
<td class="{{'red' if row.Result=='Fraud' else 'green'}}">{{row.Result}}</td>
</tr>
{% endfor %}
</table>

</div>
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    result=None
    color=None

    history=pd.read_csv(HISTORY_FILE).tail(8).to_dict("records")

    if request.method=="POST":
        amount=float(request.form["amount"])

        df=pd.DataFrame([[amount]], columns=[model.feature_names_in_[0]])

        # 🔥 MANUAL FRAUD RULE (for demo)
        if amount > 5000:
            pred=[-1]
        else:
            pred=model.predict(df)

        if pred[0]==-1:
            result="Fraud"
            color="red"
        else:
            result="Normal"
            color="green"

        new_row=pd.DataFrame([[amount,result]],columns=["amount","Result"])
        new_row.to_csv(HISTORY_FILE,mode="a",header=False,index=False)

    return render_template_string(HTML,result=result,color=color,history=history)

@app.route("/clear", methods=["POST"])
def clear():
    pd.DataFrame(columns=["amount","Result"]).to_csv(HISTORY_FILE,index=False)
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True)
