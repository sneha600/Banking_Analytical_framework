import streamlit as st
import pandas as pd
import joblib


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="Loan Risk Prediction",
    page_icon="🏦",
    layout="wide"
)


# =========================
# Login Credentials
# =========================

USER_CREDENTIALS = {
    "admin": "admin123",
    "bank_user": "bank123"
}


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False



# =========================
# Login Function
# =========================

def login():

    st.title("🏦 Loan Risk Prediction System")

    st.subheader("Login")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )


    if st.button("Login"):

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:

            st.session_state.logged_in = True

            st.success("Login Successful")

            st.rerun()


        else:

            st.error("Invalid Username or Password")



# =========================
# Logout Function
# =========================

def logout():

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()



# =========================
# Load Model
# =========================

# =========================
# Load Model
# =========================

model = joblib.load("loan_risk_model.joblib")


# =========================
# Main App
# =========================

if not st.session_state.logged_in:

    login()



else:


    st.sidebar.success("User Logged In")

    logout()


    st.title("🏦 Loan Risk Prediction System")


    st.write(
        "Enter customer and loan details to predict risk."
    )


    # -------------------------
    # Input Fields
    # -------------------------


    st.header("Loan Details")


    amount = st.number_input(
        "Loan Amount"
    )


    duration = st.number_input(
        "Loan Duration"
    )


    payments = st.number_input(
        "Monthly Payment"
    )



    st.header("Customer Details")


    age = st.number_input(
        "Customer Age",
        min_value=18,
        max_value=100
    )


    sex = st.selectbox(
        "Gender",
        ["Female","Male"]
    )



    st.header("Transaction Behaviour")


    total_transactions = st.number_input(
        "Total Transactions"
    )


    total_transaction_amount = st.number_input(
        "Total Transaction Amount"
    )


    avg_transaction_amount = st.number_input(
        "Average Transaction Amount"
    )


    avg_balance = st.number_input(
        "Average Balance"
    )


    max_balance = st.number_input(
        "Maximum Balance"
    )


    min_balance = st.number_input(
        "Minimum Balance"
    )



    st.header("Product Details")


    total_orders = st.number_input(
        "Total Orders"
    )


    avg_order_amount = st.number_input(
        "Average Order Amount"
    )


    total_cards = st.number_input(
        "Total Cards"
    )



    st.header("District Information")


    population = st.number_input(
        "Population"
    )


    urban_population_ratio = st.number_input(
        "Urban Population Ratio"
    )


    average_salary = st.number_input(
        "Average Salary"
    )


    unemployment_rates2 = st.number_input(
        "Unemployment Rate"
    )


    entrepreneurs_per_1000_resident = st.number_input(
        "Entrepreneurs per 1000 Resident"
    )


    crime_statistics2 = st.number_input(
        "Crime Statistics"
    )



    # -------------------------
    # Prediction
    # -------------------------


    if st.button("Predict Loan Risk"):


        sex_Male = 1 if sex=="Male" else 0


        input_data = pd.DataFrame({

            'amount':[amount],

            'duration':[duration],

            'payments':[payments],

            'age':[age],

            'total_transactions':[total_transactions],

            'total_transaction_amount':[total_transaction_amount],

            'avg_transaction_amount':[avg_transaction_amount],

            'avg_balance':[avg_balance],

            'max_balance':[max_balance],

            'min_balance':[min_balance],

            'total_orders':[total_orders],

            'avg_order_amount':[avg_order_amount],

            'total_cards':[total_cards],

            'population':[population],

            'urban_population_ratio':[urban_population_ratio],

            'average_salary':[average_salary],

            'unemployment_rates2':[unemployment_rates2],

            'entrepreneurs_per_1000_resident':[entrepreneurs_per_1000_resident],

            'crime_statistics2':[crime_statistics2],

            'sex_Male':[sex_Male]

        })


        prediction = model.predict(input_data)[0]


        probability = model.predict_proba(input_data)[0][1]



        st.subheader(
            f"Risk Probability: {probability*100:.2f}%"
        )



        if prediction == 1:

            st.error(
                "⚠️ High Risk Loan"
            )


            st.write(
                "Customer has higher probability of loan default."
            )


        else:

            st.success(
                "✅ Low Risk Loan"
            )


            st.write(
                "Customer has lower probability of loan default."
            )