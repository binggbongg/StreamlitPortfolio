import streamlit as st

st.markdown(
    """
    <style>
    .project-card {
        background-color: #efddcf;
        border: 2px solid #171717;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 2.5rem;
    }
    .project-title {
        font-weight: 800;
        font-size: 2rem;
        margin-bottom: 0.2rem;
    }
    .badge-tool {
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
        font-size: 0.85rem;
    }
    div[class*="st-key-project_card"] {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

_, col_content, _ = st.columns([0.1, 3, 0.1], gap="large")

with col_content:
    st.title("Projects")
    st.caption("Aissha Monceda | Section: F2")
    st.write("A collection of featured works, applications, and experiments.")

st.markdown("---")


# ==========================================
# PROJECT 1 TEMPLATE
# ==========================================
with st.container(key="project_card_1"):
    st.markdown('<div class="project-title">Project 1: BantAI Buddy</div>', unsafe_allow_html=True)
    
    col_img1, col_desc1 = st.columns([1.2, 1], gap="large")

    with col_img1:
        # Carousel via tabs: lets you add 1 to 3+ screenshots per project
        tab1, tab2 = st.tabs(["Preview 1", "Preview 2"])
        with tab1:
            # Replace with your image file path (e.g. "assets/proj1_img1.png")
            st.image("assets/buddy_1.jpg", use_container_width=True)
        with tab2:
            # Replace with your image file path (e.g. "assets/proj1_img1.png")
            st.image("assets/buddy_1.jpg", use_container_width=True)

    with col_desc1:
        st.markdown("#### Overview")
        st.write(
            """
            BantAI Buddy BantAI Buddy is an intelligent browser extension designed to enhance user 
            interaction and provide real-time content analysis through a sophisticated AI-powered pipeline. 
            It integrates a lightweight Chrome extension with a robust Node.js backend to deliver seamless AI 
            assistance and content moderation directly within the browser.
            This project was submitted for the IBPAP Hackathon.
            """
        )
        
        st.markdown("**Role:** Front-End Developer")
        
        st.markdown("**Tools & Technologies:**")
        st.markdown(
            """
            <span class="badge-tool">HTML</span>
            <span class="badge-tool">CSS</span>
            <span class="badge-tool">Javascript</span>
            <span class="badge-tool">Python</span>
            """,
            unsafe_allow_html=True,
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        # Direct GitHub Link Button
        st.link_button("View on GitHub ↗", "https://github.com/yerdnarthc/bantAI-buddy")

st.markdown("---")

# ==========================================
# PROJECT 2 TEMPLATE
# ==========================================
with st.container(key="project_card_2"):
    st.markdown('<div class="project-title">Project 2: Vinyl Vault</div>', unsafe_allow_html=True)
    
    col_img2, col_desc2 = st.columns([1.2, 1], gap="large")

    with col_img2:
        tab1, tab2 = st.tabs(["Preview A", "Preview B"])
        with tab1:
            st.image("assets/vinyl_1.png", use_container_width=True)
        with tab2:
            st.image("assets/vinyl_2.png", use_container_width=True)

    with col_desc2:
        st.markdown("#### Overview")
        st.write(
            """
            Vinyl Vault is a music vinyl service website designed for users to explore, discover, and purchase vinyl records.
            Other services include custom vinyl record creation and vinyl cleaning. This website was built only with pure HTML, CSS, and Javascript
            as a final project for the Web Development course.
            """
        )
        
        st.markdown("**Role:** UI/UX Developer")
        
        st.markdown("**Tools & Technologies:**")
        st.markdown(
            """
            <span class="badge-tool">HTML</span>
            <span class="badge-tool">CSS</span>
            <span class="badge-tool">Javascript</span>
            """,
            unsafe_allow_html=True,
        )
        
        st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# PROJECT 3 TEMPLATE
# ==========================================
with st.container(key="project_card_3"):
    st.markdown('<div class="project-title">Project 3: DaoMing Fit (Outfit Maker)</div>', unsafe_allow_html=True)
    
    col_img3, col_desc3 = st.columns([1.2, 1], gap="large")

    with col_img3:
        tab1, tab2 = st.tabs(["Preview 1", "Preview 2"])
        with tab1:
            st.image("assets/daoming_2.png", use_container_width=True)
        with tab2:
            st.image("assets/daoming_1.png", use_container_width=True)

    with col_desc3:
        st.markdown("#### Overview")
        st.write(
            """
            a Java-based desktop application designed to help users digitally manage their wardrobe, create outfits, 
            and organize clothing collections. Built with a custom retro aesthetic reminiscent of Windows 95/98, 
            it combines nostalgia with modern functionality like API-driven background removal and file persistence
            """
        )
        
        st.markdown("**Role:** Lead Front-End Developer")
        
        st.markdown("**Tools & Technologies:**")
        st.markdown(
            """
            <span class="badge-tool">Java</span>
            """,
            unsafe_allow_html=True,
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.link_button("View on GitHub ↗", "https://github.com/Condatum/Daoming-Fit")


# ==========================================
# PROJECT 4 TEMPLATE
# ==========================================

with st.container(key="project_card_4"):
    st.markdown('<div class="project-title">Project 4: Sir Jay Simulator</div>', unsafe_allow_html=True)
    
    col_img3, col_desc3 = st.columns([1.2, 1], gap="large")

    with col_img3:
        tab1, tab2 = st.tabs(["View 1", "View 2"])
        with tab1:
            st.image("assets/sirjay_1.png", use_container_width=True)
        with tab2:
            st.image("assets/sirjay_2.png", use_container_width=True)

    with col_desc3:
        st.markdown("#### Overview")
        st.write(
            """
            Sir Serator Simulator is a high-stake arcade classroom management simulator game where 
            you act as the iconic teacher, Sir Jay Vince Serato, proctoring a set of students that are taking your quizzes. 
            Of course, being a teacher comes with its own set of problems. You must be vigilant in ensuring that your 
            students do not attempt to cheat or else you will lose your patience and your sanity. 
            This game was a submission for our Object-Oriented Programming 2 course as a final project.

            """
        )
        
        st.markdown("**Role:** Game Developer")
        
        st.markdown("**Tools & Technologies:**")
        st.markdown(
            """
            <span class="badge-tool">Java</span>
            """,
            unsafe_allow_html=True,
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.link_button("View on GitHub ↗", "https://github.com/binggbongg/CSIT228-Capstone-Sir-Jay-Simulator")

# ==========================================
# PROJECT 4 TEMPLATE
# ==========================================

with st.container(key="project_card_5"):
    st.markdown('<div class="project-title">Project 5: Salamin at Bakal</div>', unsafe_allow_html=True)
    
    col_img3, col_desc3 = st.columns([1.2, 1], gap="large")

    with col_img3:
        tab1, tab2 = st.tabs(["Preview 1", "Preview 2"])
        with tab1:
            st.image("assets/sb_1.png", use_container_width=True)
        with tab2:
            st.image("assets/sb_2.png", use_container_width=True)

    with col_desc3:
        st.markdown("#### Overview")
        st.write(
            """
            Salamin at Bakal is a strategic, turn-based deckbuilder game about reclaiming the 
            voice of your people through the power of sign language. Cast your spells and combos to make your way 
            through the Iron City, facing stronger opponents as you progress through the game. Find out what happened 
            to the voices of your people and follow your destiny as the child of the silent blessing to seek the truth behind the silence.
            """
        )
        
        st.markdown("**Role:** Lead Game Developer")
        
        st.markdown("**Tools & Technologies:**")
        st.markdown(
            """
            <span class="badge-tool">GDScript</span>
            <span class="badge-tool">C#</span>
            """,
            unsafe_allow_html=True,
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.link_button("Play on Itch ↗", "https://b1nggb0ngg.itch.io/salamin-at-bakal")