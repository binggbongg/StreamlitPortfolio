import streamlit as st

# Orange band is styled here so only the home page gets it
st.markdown(
    """
    <style>
    .st-key-hero {
        background-color: #d76326;
        padding: 4rem 12% !important;
        min-height: 28rem;
        justify-content: center;
    }
    [data-testid="stImage"] img {
        box-sizing: border-box;
        border: 18px solid #efddcf;
        border-radius: 0;
    }

    /* Olive call-to-action button in the bottom cream band */
    .st-key-cta {
        padding: 2.5rem 0 !important;
        align-items: center !important;
    }
    .st-key-cta [data-testid="stElementContainer"] {
        width: auto !important;
    }
    .st-key-cta [data-testid="stPageLink"] {
        display: flex;
        justify-content: center;
    }
    .st-key-cta [data-testid="stPageLink"] a {
        width: auto;
        justify-content: center;
        background-color: #6b7a3d;
        border-radius: 999px;
        padding: 1rem 3rem;
        text-decoration: none;
    }
    .st-key-cta [data-testid="stPageLink"] a p {
        color: #efddcf;
        font-weight: 700;
        font-size: 1.5rem;
        white-space: nowrap;
    }
    .st-key-cta [data-testid="stPageLink"] a:hover {
        filter: brightness(1.12);
    }
    .st-key-cta [data-testid="stIconEmoji"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container(key="hero"):
    col1, col2 = st.columns([1, 2], gap="large", vertical_alignment="center")

    with col1:
        st.image("assets/profile.jpg", width=320)

    with col2:
        st.title("Hello, World!")
        st.write("**A short introduction about me**")
        st.write(
            """
            I am Aissha Monceda, a third year Computer Science student at Cebu Institute of Technology.
            I like to create weird and fun things. Check it out on my other pages!
            """
        )

with st.container(key="cta"):
    st.page_link("views/projects.py", label="Check Out My Projects!")