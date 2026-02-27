from __future__ import annotations

import streamlit as st


IMDB_YELLOW = "#F5C518"
IMDB_BLACK = "#121212"
IMDB_WHITE = "#FFFFFF"


def apply_theme() -> None:
    st.set_page_config(
        page_title="IMDb Movies Analytics Dashboard",
        page_icon=":clapper:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(
        """
        <style>
        .stApp { background: #121212; color: #FFFFFF; }
        .block-container { padding-top: 1.2rem; padding-bottom: 1.2rem; }
        .imdb-logo {
            display: inline-block;
            background: #F5C518;
            color: #121212;
            font-weight: 800;
            font-size: 1.2rem;
            border-radius: 6px;
            padding: 0.15rem 0.7rem;
            letter-spacing: 0.5px;
            margin-right: 0.6rem;
        }
        .subtitle {
            color: #D0D0D0;
            font-size: 0.95rem;
            margin-top: -0.35rem;
            margin-bottom: 0.8rem;
        }
        .section-title {
            color: #F5C518;
            font-size: 1.15rem;
            font-weight: 700;
            margin-top: 0.7rem;
            margin-bottom: 0.35rem;
        }
        .kpi-card {
            background: #1B1B1B;
            border: 1px solid #2A2A2A;
            border-radius: 14px;
            padding: 14px 16px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.28);
        }
        .kpi-label { color: #BDBDBD; font-size: 0.85rem; margin-bottom: 4px; }
        .kpi-value { color: #FFFFFF; font-size: 1.35rem; font-weight: 700; }

        .filters-shell {
            background: rgba(17,17,17,0.95);
            border: 1px solid #2B2B2B;
            border-radius: 14px;
            padding: 10px 14px 8px 14px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.30);
            margin-top: 0.15rem;
            margin-bottom: 0.4rem;
        }
        .filters-title {
            color: #C6A437;
            font-size: 0.88rem;
            font-weight: 700;
            letter-spacing: 0.08em;
        }
        .filters-subtitle {
            color: #9A9A9A;
            font-size: 0.72rem;
            margin-top: 0;
            margin-bottom: 2px;
            letter-spacing: 0.03em;
        }
        .filters-rule {
            margin-top: 6px;
            margin-bottom: 0;
            width: 100%;
            height: 1px;
            background: linear-gradient(90deg, rgba(198,164,55,0.9) 0%, rgba(198,164,55,0.1) 100%);
        }
        .filter-label {
            color: #F5F5F5;
            font-size: 0.76rem;
            letter-spacing: 0.03em;
            margin-top: 0.05rem;
            margin-bottom: 0.22rem;
        }

        div[data-testid="stSlider"] {
            background: #151515;
            border: 1px solid #2B2B2B;
            border-radius: 10px;
            padding: 4px 8px 0 8px;
            margin-bottom: 0.15rem;
        }
        div[data-testid="stSlider"] label {
            color: #C6A437 !important;
            font-size: 0.74rem !important;
            letter-spacing: 0.03em;
        }
        div[data-testid="stSlider"] [data-testid="stTickBarMin"],
        div[data-testid="stSlider"] [data-testid="stTickBarMax"],
        div[data-testid="stSlider"] [data-testid="stThumbValue"] {
            color: #C6A437 !important;
        }
        div[data-testid="stSlider"] p,
        div[data-testid="stSlider"] span,
        div[data-testid="stSlider"] div {
            color: #C6A437 !important;
        }
        div[data-testid="stSlider"] [role="slider"] {
            background: #C6A437 !important;
            border: 2px solid #E2C150 !important;
            box-shadow: 0 0 0 2px rgba(198,164,55,0.25);
        }
        div[data-testid="stSlider"] [data-baseweb="slider"] > div > div {
            background: #2A2A2A !important;
            height: 4px !important;
        }
        div[data-testid="stSlider"] [data-baseweb="slider"] > div > div > div {
            background: linear-gradient(90deg, #7A6110 0%, #C6A437 100%) !important;
        }

        div[data-testid="stMultiSelect"] {
            background: #151515;
            border: 1px solid #2B2B2B;
            border-radius: 10px;
            padding: 4px 8px 6px 8px;
            margin-bottom: 0.15rem;
        }
        div[data-testid="stMultiSelect"] label {
            color: #F5F5F5 !important;
            font-size: 0.74rem !important;
            letter-spacing: 0.03em;
        }
        div[data-testid="stMultiSelect"] [data-baseweb="tag"] {
            border-radius: 999px !important;
            background: #1A1A1A !important;
            color: #F5F5F5 !important;
            border: 1px solid #2D2D2D !important;
        }
        div[data-testid="stMultiSelect"] [data-baseweb="tag"] span[role="button"] {
            color: #AFAFAF !important;
        }
        div[data-testid="stMultiSelect"] [data-baseweb="select"] > div {
            background: #151515 !important;
            border-color: #343434 !important;
            color: #F5F5F5 !important;
        }
        div[data-testid="stMultiSelect"] [data-baseweb="select"] input {
            color: #F5F5F5 !important;
            caret-color: #C6A437 !important;
        }
        div[data-testid="stMultiSelect"] [data-baseweb="select"] input::placeholder {
            color: #9A9A9A !important;
            opacity: 1 !important;
        }

        /* Minimum Votes (number input): simplified style */
        div[data-testid="stNumberInput"] {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            outline: none !important;
            padding: 0 !important;
            margin-bottom: 0.15rem !important;
        }
        div[data-testid="stNumberInputContainer"] {
            background: #151515 !important;
            border: 1px solid #2B2B2B !important;
            border-radius: 10px !important;
            padding: 4px 8px !important;
            box-shadow: none !important;
            outline: none !important;
        }
        div[data-testid="stNumberInput"] [data-baseweb="input"],
        div[data-testid="stNumberInput"] [data-baseweb="base-input"],
        div[data-testid="stNumberInputContainer"] [data-baseweb="input"],
        div[data-testid="stNumberInputContainer"] [data-baseweb="base-input"] {
            background: #000000 !important;
            border: none !important;
            box-shadow: none !important;
        }
        div[data-testid="stNumberInput"] label {
            color: #C6A437 !important;
            font-size: 0.74rem !important;
            letter-spacing: 0.03em;
        }
        div[data-testid="stNumberInput"] input,
        div[data-testid="stNumberInputContainer"] input {
            background: #000000 !important;
            color: #C6A437 !important;
            border: none !important;
            border-radius: 8px !important;
            box-shadow: none !important;
            outline: none !important;
        }
        div[data-testid="stNumberInput"]:focus-within,
        div[data-testid="stNumberInputContainer"]:focus-within {
            border-color: #2B2B2B !important;
            box-shadow: none !important;
            outline: none !important;
        }
        div[data-testid="stNumberInput"] button,
        div[data-testid="stNumberInputContainer"] button,
        button[data-testid="stNumberInputStepDown"],
        button[data-testid="stNumberInputStepUp"] {
            display: none !important;
        }
        div[data-testid="stNumberInput"] input[type="number"],
        div[data-testid="stNumberInputContainer"] input[type="number"] {
            appearance: textfield !important;
            -moz-appearance: textfield !important;
        }
        div[data-testid="stNumberInput"] input[type="number"]::-webkit-outer-spin-button,
        div[data-testid="stNumberInput"] input[type="number"]::-webkit-inner-spin-button,
        div[data-testid="stNumberInputContainer"] input[type="number"]::-webkit-outer-spin-button,
        div[data-testid="stNumberInputContainer"] input[type="number"]::-webkit-inner-spin-button {
            -webkit-appearance: none !important;
            margin: 0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    st.markdown(
        """
        <div>
          <span class="imdb-logo">IMDb</span>
          <span style="font-size:1.5rem;font-weight:700;color:#FFFFFF;">Movies Analytics Dashboard</span>
        </div>
        <div class="subtitle">Insights from IMDB_movies dataset</div>
        """,
        unsafe_allow_html=True,
    )


def section_title(text: str) -> None:
    st.markdown(f'<div class="section-title">{text}</div>', unsafe_allow_html=True)
