import base64
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Aissha Monceda", page_icon="📌", layout="wide")

CREAM = "#efddcf"
INK = "#171717"
NAVY = "#14265c"
LIME = "#c3d44a"
LAVENDER = "#9a86c6"

# Logo is embedded as base64 so it can sit inside the custom HTML brand link
icon_path = Path(__file__).parent / "assets" / "icon.png"
icon_b64 = base64.b64encode(icon_path.read_bytes()).decode()

st.markdown(
    f"""
    <style>
    /* ---------- Font (skips Material icons so they don't turn into text) ---------- */
    html, body, .stApp,
    .stApp :is(p, h1, h2, h3, h4, h5, h6, a, li, label, button, div, span):not([data-testid="stIconMaterial"]) {{
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif !important;
    }}

    /* ---------- Page: cream background, ink text ---------- */
    .stApp {{ background-color: {CREAM}; color: {INK}; }}
    h1, h2, h3, h4, h5, h6, p, li, span, label {{ color: {INK}; }}

    /* Default header is replaced by the custom navbar below */
    [data-testid="stHeader"] {{ display: none; }}

    /* Full-bleed layout: no side padding, no gaps between top-level sections */
    [data-testid="stMainBlockContainer"] {{
        max-width: 100% !important;
        padding: 0 0 4rem 0 !important;
    }}
    [data-testid="stMainBlockContainer"] > [data-testid="stVerticalBlock"] {{
        gap: 0;
    }}

    /* ---------- Navbar ---------- */
    .st-key-navbar {{
        background-color: {CREAM};
        padding: 1.6rem 8% !important;
    }}
    /* Logo column takes all free space; pill columns shrink to fit their button */
    .st-key-navbar [data-testid="stHorizontalBlock"] {{
        gap: 0.8rem;
        justify-content: flex-end;
    }}
    .st-key-navbar [data-testid="stColumn"] {{
        flex: 0 0 auto !important;
        width: auto !important;
        min-width: 0 !important;
    }}
    .st-key-navbar [data-testid="stColumn"]:first-child {{
        flex: 1 1 auto !important;
    }}

    .brand a {{
        display: inline-flex;
        align-items: center;
        gap: 0.8rem;
        text-decoration: none;
        color: {INK} !important;
    }}
    .brand img {{
        height: 3.2rem;
        image-rendering: pixelated;
    }}
    .brand span {{
        font-size: 2.1rem;
        font-weight: 700;
        letter-spacing: -0.02em;
    }}

    /* Pill buttons */
    .st-key-navbar [data-testid="stPageLink"] a {{
        justify-content: center;
        border-radius: 999px;
        padding: 0.6rem 2rem;
        min-height: 2.9rem;
        text-decoration: none;
    }}
    .st-key-navbar [data-testid="stPageLink"] a p {{
        font-weight: 700;
        font-size: 1.1rem;
        white-space: nowrap;
    }}

    /* About Me = navy / lime */
    .st-key-navbar [data-testid="stColumn"]:nth-child(2) a {{ background-color: {NAVY}; }}
    .st-key-navbar [data-testid="stColumn"]:nth-child(2) a p {{ color: {LIME}; }}

    /* Projects = lavender / ink */
    .st-key-navbar [data-testid="stColumn"]:nth-child(3) a {{ background-color: {LAVENDER}; }}
    .st-key-navbar [data-testid="stColumn"]:nth-child(3) a p {{ color: {INK}; }}

    .st-key-navbar [data-testid="stPageLink"] a:hover {{ filter: brightness(1.12); }}

    /* ---------- Type ---------- */
    h1 {{
        font-weight: 800 !important;
        font-size: 3.4rem !important;
        letter-spacing: -0.02em;
        padding-top: 0 !important;
    }}
    [data-testid="stMarkdownContainer"] p {{
        font-size: 1.2rem;
        line-height: 1.5;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

pages = [
    st.Page("views/home.py", title="Home", default=True),
    st.Page("views/aboutme.py", title="About Me"),
    st.Page("views/projects.py", title="Projects"),
]

# Built-in nav is hidden; the custom navbar below replaces it
pg = st.navigation(pages, position="hidden")

with st.container(key="navbar"):
    brand_col, about_col, projects_col = st.columns(
        [5, 1.15, 1], gap="small", vertical_alignment="center"
    )
    with brand_col:
        st.markdown(
            f"""
            <div class="brand">
                <a href="/" target="_self">
                    <img src="data:image/png;base64,{icon_b64}" alt="Portfolio logo">
                    <span>Portfolio</span>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with about_col:
        st.page_link(pages[1], label="About Me")
    with projects_col:
        st.page_link(pages[2], label="Projects")

pg.run()