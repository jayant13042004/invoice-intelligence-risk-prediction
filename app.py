import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from inference.predict_freight import predict_freight_cost
from inference.predict_invoice import predict_invoice_flag


# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    page_icon="📦",
    layout="wide"
)


# ------------------------------------------------------------
# Your styling (kept as-is, one typo fixed: "1important" -> "!important")
# ------------------------------------------------------------

def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>

                """
            ,unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>

                """
            ,unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');


         /* Hide Top Bar of streamlit */

            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top:1.5rem !important;
            }

            h1 {
                font-family: 'Sora', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
            }


            h2 {
                font-family: 'Sora', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }

            h3, h4, p {
                font-family: 'Outfit', sans-serif;
            }


            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>

                """
            ,unsafe_allow_html=True)


# ------------------------------------------------------------
# Extra styling for this portal, using the same palette
# (blurple #5865F2, lavender #E0E3FF, pink #EB459E, black)
# ------------------------------------------------------------

def style_portal():

    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Mrs+Saint+Delafield&family=Herr+Von+Muellerhoff&family=Poppins:wght@400;500;600&display=swap');

            :root {
                --accent: #8B5CF6;
                --accent-dark: #6D3FD9;
                --page-bg: #E0E3FF;
            }

            html, body, [class*="css"], label, input, span, div {
                font-family: 'Outfit', sans-serif;
            }

            /* Page title: long text, so a bit smaller than the default h1 */
            /* Page title: signature-style script */
            h1 {
                font-family: 'Mrs Saint Delafield', 'Herr Von Muellerhoff', cursive !important;
                font-size: 4.6rem !important;
                font-weight: 400 !important;
                letter-spacing: 0 !important;
                line-height: 1 !important;
                color: #000000 !important;
            }

            /* accent bar under the page title (follows the selected module) */
            h1::after {
                content: "";
                display: block;
                width: 90px;
                height: 8px;
                border-radius: 8px;
                background: var(--accent);
                margin-top: .9rem;
            }

            .page-sub {
                font-family: 'Poppins', 'Outfit', sans-serif;
                font-weight: 500;
                font-size: 1.15rem;
                color: #3b3f6b;
                margin: .6rem 0 1.6rem 0;
            }

            .module-title {
                font-family: 'Poppins', 'Outfit', sans-serif;
                font-weight: 600;
                font-size: 1.5rem;
                color: var(--accent);
                line-height: 1.1;
                margin: 0 0 .5rem 0;
            }

            .module-desc {
                font-family: 'Poppins', 'Outfit', sans-serif;
                font-weight: 400;
                font-size: 1.05rem;
                color: #2b2e55;
                max-width: 640px;
                line-height: 1.5;
                margin-bottom: 1.2rem;
            }

            /* Form card */
            [data-testid="stForm"] {
                background: #ffffff;
                border: none;
                border-radius: 2rem;
                padding: 2rem 2rem 1.5rem 2rem;
            }

            [data-testid="stForm"] label p {
                font-family: 'Outfit', sans-serif;
                font-weight: 600;
                color: #000000;
            }

            [data-testid="stNumberInput"] input {
                border-radius: 1rem;
            }

            [data-testid="stForm"] {
                border-top: 8px solid var(--accent);
            }

            [data-testid="stFormSubmitButton"] > button {
                background-color: var(--accent) !important;
            }

            [data-testid="stFormSubmitButton"] > button:hover {
                background-color: var(--accent-dark) !important;
            }

            /* Number input +/- buttons follow the module accent */
            [data-testid="stNumberInputStepUp"],
            [data-testid="stNumberInputStepDown"] {
                background-color: var(--accent) !important;
                color: #ffffff !important;
                padding: 0 !important;
                border-radius: .8rem !important;
            }

            [data-testid="stNumberInputStepUp"]:hover,
            [data-testid="stNumberInputStepDown"]:hover {
                background-color: var(--accent-dark) !important;
            }

            [data-testid="stNumberInputStepUp"] svg,
            [data-testid="stNumberInputStepDown"] svg {
                fill: #ffffff !important;
                color: #ffffff !important;
            }

            /* Result cards */
            .result {
                margin-top: 1.5rem;
                border-radius: 2rem;
                padding: 1.6rem 2rem;
                color: #ffffff;
                background: var(--accent);
                border-bottom: 10px solid var(--accent-dark);
            }

            .result .label {
                font-size: 1rem;
                opacity: .85;
            }

            .result .value {
                font-family: 'Sora', sans-serif;
                font-weight: 800;
                font-size: 2.2rem;
                line-height: 1.1;
                margin-top: .3rem;
            }

            .result .note {
                font-size: 1rem;
                margin-top: .5rem;
                opacity: .9;
            }

            .result.flag {
                background: var(--accent);
                border-bottom: 10px solid #000000;
            }

            .result.flag .value,
            .result.ok .value {
                font-size: 1.5rem;
            }

            .result.ok {
                background: #000000;
                border-bottom: 10px solid var(--accent);
            }

            /* Sidebar */
            [data-testid="stSidebar"] {
                background: #5865F2;
            }

            [data-testid="stSidebar"] * {
                color: #ffffff !important;
            }

            [data-testid="stSidebar"] h1 {
                font-family: 'Sora', sans-serif !important;
                font-size: 1.2rem !important;
                font-weight: 800 !important;
                color: #ffffff !important;
            }

            .side-note {
                border-left: 8px solid var(--accent);
                background: var(--page-bg);
                border-radius: 1.5rem;
                padding: 1rem 1.2rem;
                line-height: 1.5;
            }

            [data-testid="stSidebar"] .side-note,
            [data-testid="stSidebar"] .side-note * {
                color: #2b2e55 !important;
            }

        </style>
        """,
        unsafe_allow_html=True
    )




def style_module(selected):
    """Purple for Freight Cost Prediction, pink for Invoice Manual Approval Flag."""

    if selected == "Freight Cost Prediction":
        accent, dark, bg = "#8B5CF6", "#6D3FD9", "#E0E3FF"
    else:
        accent, dark, bg = "#EB459E", "#D12E86", "#FCE1F0"

    st.markdown(
        f"""
        <style>
            :root {{
                --accent: {accent};
                --accent-dark: {dark};
                --page-bg: {bg};
            }}

            .stApp {{
                background: {bg} !important;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )


style_background_dashboard()
style_base_layout()
style_portal()


# ------------------------------------------------------------
# Header
# ------------------------------------------------------------

st.title("Vendor Invoice Intelligence Portal")

st.markdown(
    '<p class="page-sub">Estimate freight costs and check whether an invoice needs manual approval.</p>',
    unsafe_allow_html=True
)


# ------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------

st.sidebar.title("Module")

selected_model = st.sidebar.radio(
    "Choose a prediction module",
    [
        "Freight Cost Prediction",
        "Invoice Manual Approval Flag"
    ]
)

style_module(selected_model)

st.sidebar.markdown("""
<div class="side-note">
<b>What this helps with</b><br>
Better freight forecasts, fewer anomalous invoices getting through,
and less time spent on manual review.
</div>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# Freight Cost Prediction
# ------------------------------------------------------------

if selected_model == "Freight Cost Prediction":

    st.markdown("""
    <p class="module-title">Freight cost prediction</p>
    <p class="module-desc">
    Enter the quantity and invoice amount to get an estimated freight cost.
    Useful for budgeting, forecasting, and vendor negotiations.
    </p>
    """, unsafe_allow_html=True)

    with st.form("freight_form"):

        col1, col2 = st.columns(2)

        with col1:
            quantity = st.number_input(
                "Quantity",
                min_value=1,
                value=1200
            )

        with col2:
            dollars = st.number_input(
                "Invoice dollars",
                min_value=1.0,
                value=18500.0
            )

        submit_freight = st.form_submit_button(
            "Predict freight cost"
        )

    if submit_freight:

        input_data = {
            "Quantity": [quantity],
            "Dollars": [dollars]
        }

        prediction = predict_freight_cost(
            input_data
        )["predicted_freight"]

        st.markdown(f"""
        <div class="result">
            <div class="label">Estimated freight cost</div>
            <div class="value">${prediction[0]:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)


# ------------------------------------------------------------
# Invoice Flag Prediction
# ------------------------------------------------------------

else:

    st.markdown("""
    <p class="module-title">Invoice manual approval check</p>
    <p class="module-desc">
    Checks whether an invoice should go to manual approval, based on
    unusual cost, freight, or delivery patterns.
    </p>
    """, unsafe_allow_html=True)

    with st.form("invoice_flag_form"):

        col1, col2, col3 = st.columns(3)

        with col1:

            invoice_quantity = st.number_input(
                "Invoice quantity",
                min_value=1,
                value=50
            )

            freight = st.number_input(
                "Freight cost",
                min_value=0.0,
                value=1.73
            )

        with col2:

            invoice_dollars = st.number_input(
                "Invoice dollars",
                min_value=1.0,
                value=352.95
            )

            total_item_quantity = st.number_input(
                "Total item quantity",
                min_value=1,
                value=162
            )

        with col3:

            total_item_dollars = st.number_input(
                "Total item dollars",
                min_value=1.0,
                value=2476.0
            )

        submit_flag = st.form_submit_button(
            "Check invoice"
        )

    if submit_flag:

        input_data = {
            "invoice_quantity": [invoice_quantity],
            "invoice_dollars": [invoice_dollars],
            "Freight": [freight],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars]
        }

        flag_prediction = predict_invoice_flag(
            input_data
        )["predicted_flag"]

        is_flagged = bool(flag_prediction[0])

        if is_flagged:
            st.markdown("""
            <div class="result flag">
                <div class="label">Result</div>
                <div class="value">Send for manual approval</div>
                <div class="note">The cost, freight, or delivery pattern looks unusual.</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result ok">
                <div class="label">Result</div>
                <div class="value">Safe to auto-approve</div>
                <div class="note">No unusual patterns found.</div>
            </div>
            """, unsafe_allow_html=True)