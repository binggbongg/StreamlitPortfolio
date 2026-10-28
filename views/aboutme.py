import streamlit as st
import pandas as pd

# Page container styling to match cream palette
st.markdown(
    """
    <style>
    .about-wrapper {
        padding: 2rem 10% 4rem 10%;
    }
    .section-card {
        background-color: rgba(255, 255, 255, 0.45);
        border: 2px solid #171717;
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 2rem;
    }
    .badge {
        display: inline-block;
        background-color: #14265c;
        color: #c3d44a;
        padding: 0.3rem 0.8rem;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.85rem;
        margin-bottom: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

_, col_content, _ = st.columns([0.1, 1, 0.1], gap="large")

with col_content:
    # ---------- Header & Student Tag ----------
    st.title("About Me")
    # Requirement: Name and section visible on the page
    st.caption("Aissha Monceda | Section: F2") 
st.markdown("---")

# ---------- 1. Autobiography & Background ----------
_, col_bio, col_milestones, _ = st.columns([0.2, 1.4, 1, 0.2], gap="large")

with col_bio:
    st.markdown("## Autobiography")
    
    st.subheader("Background")
    st.write(
        """
        I am currently a third-year Computer Science student at Cebu Institute of Technology - University.
        I have always been interested in learning about different technological and programmin concepts, and here I am doing my best to learn and improve what I can day by day.
        I started learning basic programming concepts in junior high school, which sparked my interest in the field of computer science. Since then, 
        I have been exploring various programming languages and technologies, and I am eager to continue growing my skills and knowledge in this ever-evolving field.
        """
    )
    
    st.subheader("Education")
    st.write(
        """
        **College**
        - **Degree:** Bachelor of Science in Computer Science
        - **Institution:** Cebu Institute of Technology - University
        - **Year Level:** 3rd Year

        **Senior High School**
        - **Strand:** Science, Technology, Engineering, and Mathematics (STEM)
        - **Institution:** Cebu Institute of Technology - University

        **Junior High School**
        - **Institution:** University of San Carlos - South Campus

        **Elementary**
        - **Institution:** Saint Theresa's College - Cebu City
        """
    )

    st.subheader("Interests")
    st.write(
        """
        - Playing Video Games
        - Watching Movies
        - Hiking
        - Playing Musical Instruments
        - Game Development
        - Web Development
        - UI/UX Research and Design
        """
    )

with col_milestones:
    st.markdown("### Achievements & Milestones")
    # Interactive expander for milestones
    with st.expander("Second Place | Can You Hack It? IBPAP Hackathon", expanded=True):
        st.write("The IBPAP Hackathon tackles smart prototypes to AI-powered solutions tackling digital safety, health, education, gender empowerment, and disaster response.")
        
    with st.expander("Best Team Project Concept | APX 2025: Project Pitch Competition"):
        st.write("The APX 2025: Project Pitch Competition highlights a 3-day course where students learn how to develop innovative and sustainable project concepts for campus sustainability.")
        
    with st.expander("Fourth Runner-Up | DOST Next Level: Esports Game Dev Challenge"):
        st.write("This competition invites aspiring game developers to showcase their talent, explore emerging technologies, and create games that demonstrate innovation, creativity, excellence, and social impact")

st.markdown("---")

# ---------- 2. Skills: Chart and Table ----------
_, main_col, _ = st.columns([0.1, 1, 0.1], gap="large")

with main_col:
    st.markdown("### Skills & Competencies")

# Edit your skill names and scores (out of 100) below
    skills_data = {
        "Skill / Technology": [
            "Python",
            "Android / Kotlin Development",
            "HTML/CSS Web Development",
            "Game Development",
            "UI/UX Design"
        ],
        "Proficiency (%)": [60, 70, 75, 80, 70],
        "Experience Level": ["Advanced", "Intermediate", "Intermediate", "Intermediate", "Advanced"]
    }

    df_skills = pd.DataFrame(skills_data)

    col_chart, col_table = st.columns([1.3, 1], gap="large")

    with col_chart:
        st.write("**Proficiency Chart**")
        # Horizontal/bar chart of skills using your own numbers
        chart_data = df_skills.set_index("Skill / Technology")[["Proficiency (%)"]]
        st.bar_chart(chart_data)

    with col_table:
        st.write("**Skills Breakdown**")
        st.dataframe(df_skills, use_container_width=True, hide_index=True)

st.markdown("---")

# ---------- 3. Contact & Feedback Form ----------

_, contact_col, _ = st.columns([0.1, 1, 0.1], gap="large")

with contact_col:

    st.markdown("### Get In Touch")
    st.write("Have a question, feedback, or want to collaborate? Leave a message below.")

    with st.form("contact_form", clear_on_submit=True):
        col_name, col_email = st.columns(2)
        with col_name:
            sender_name = st.text_input("Name")
        with col_email:
            sender_email = st.text_input("Email")
            
        topic = st.selectbox(
            "Reason for Contact",
            ["General Inquiry", "Project Collaboration", "Feedback", "Other"]
        )
        
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            if sender_name.strip() and message.strip():
                # Response after submission satisfies the component requirement
                st.success(f"Thank you, {sender_name}! Your message has been sent successfully.")
            else:
                st.error("Please fill in both your name and message before submitting.")