import streamlit as st
import datetime
from PIL import Image

# Set page configuration
st.set_page_config(page_title="BIOGRAPHY", page_icon="📖", layout="wide")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "PERSONAL"  # Default page

# Navigation function
def navigate_to(page):
    st.session_state.page = page
    
st.write("---")

st.markdown(
    """
    <div style='
        text-align: center; 
        background-color: #1E90FF; 
        padding: 20px; 
        border-radius: 10px; 
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);'>
        <h1 style='
            font-family: Arial, sans-serif; 
            font-size: 48px; 
            color: #2c3e50; 
            margin-bottom: 10px;'> 
            🌟 Welcome to My Biography 🌟 
        </h1>
        <p style='
            font-family: "Courier New", Courier, monospace; 
            font-size: 18px; 
            color: #34495e;'> 
            Dive into the story of my life, where passion, creativity, and dreams come together. 📖✨
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

    
st.write("---")

# ---- PERSONAL BACKGROUND PAGE ----
if st.session_state.page == "PERSONAL":
    st.title("PERSONAL BACKGROUND")
    
    # --- LEFT SIDE --- 
    with st.container():
        left_column, right_column = st.columns(2)  # Alignment
        with left_column:
            # --- PICTURE ---
            default_image_path = "trapezoid.jpg" #image file
            
            uploaded_image = st.file_uploader("Upload a 2x2 ID", type=["jpg", "jpeg", "png"])
            if uploaded_image is not None:
                try:
                    image = Image.open(uploaded_image)
                    resized_image = image.resize((600, 600))
                    col1, col2, col3 = st.columns([1, 3, 1])  # Center the image
                    with col2:
                        st.image(image, caption = f"PROFILE", width = 275)
                except Exception as e:
                    st.error(f"Error displaying the upload image: {e}")
            else:
                try:
                    default_image = Image.open(default_image_path)
                    col1, col2, col3 = st.columns([1, 3, 1])  # Center the image
                    with col2:
                        st.image(default_image, caption = f"PROFILE", width = 275)
                except FileNotFoundError:
                    st.error("Image not found. Please check file_image_path")
                    
            st.write("---")
            name = st.text_input("NAME", "EJ Lawrence S. Comandante")
            profession = st.text_input("PROFESSION", "College Student")
            st.write("---")
            # --- AGE SELECTION ---
            age = st.selectbox("Age", [str(i) for i in range(18, 101)])
            # --- BIRTHDAY ---
            bday = st.date_input("BDAY", datetime.date(2005, 12, 12))
            # --- GENDER SELECTION ---
            gender = st.radio("GENDER", ["Male", "Female"])
            # --- HOBBIES ---
            st.subheader("HOBBIES")
            hs = st.text_area(" LIST OF HOBBIES", "  Coding\n\n  Doodling\n\n  Playing\n\n  Watching\n\n  Reading\n\n  3D Modeling\n\n")
            # --- SKILLS ---
            st.subheader("SKILLS")
            hs = st.text_area(" PERSONAL SKILLS ", " TEAMWORK\n\n  CREATIVITY\n\n  PROBLEM SOLVING\n\n")
            # --- ACHIEVEMENTS ---
            st.subheader("ACHIEVEMENTS")
            hs = st.text_area("ACHIEVEMENTS", "  3rd Placer in DSPC Desktop Publishing Filipino Category (2016-2017)\n\n   3rd Placer in Mathematics Sudoku (2015)\n\n    CRAM Participant Dance Group Competition (2018)\n\n")
            

        # --- RIGHT SIDE ---
        with right_column:
            # --- MY PROFILE ---
            st.subheader("MY PROFILE")
            hs = st.text_area("Greetings!!!", """   My name is EJ Lawrence Sutana Comandante, but you can just call me Jay. I'm 18 years old and currently a college student who views time in a unique way. I like to spend my days balancing fun and productivity, diving into activities like playing games, sleeping, coding, doodling, and, of course, studying. For me, every moment spent on these pursuits is a step toward growth and self-discovery.

    I see myself as a creative thinker with a knack for problem-solving. I enjoy coming up with innovative ideas and working in teams where I can contribute and learn from others. I thrive in environments that challenge my intellect and inspire my imagination. Whether I'm tackling a project, exploring a new hobby, or focusing on my studies, I always aim to make the most of my time and give my best to everything I do.""")
            
            # --- EDUCATIONAL BACKGROUND ---
            st.subheader("EDUCATIONAL BACKGROUND")
            es = st.write("ELEMENTARY")
            nes = st.text_input("SCHOOL NAME", "CLEMENTINO V. DIEZ MEMORIAL CENTRAL ELEMENTARY SCHOOL")
            yes = st.selectbox("YEAR GRADUATED", range(1900, 2101), index=118)
            st.write("   ")
                
            jh = st.write("JUNIOR HIGHSCHOOL")
            njh = st.text_input("SCHOOL NAME", "CARAGA REGIONAL SCIENCE HIGH SCHOOL")
            yjh = st.selectbox("YEAR GRADUATED", range(1900, 2101), index=122)
            st.write("   ")
            
            sh = st.write("SENIOR HIGHSCHOOL")
            nsh = st.text_input("SCHOOL NAME ", "CARAGA REGIONAL SCIENCE HIGH SCHOOL")
            ysh = st.selectbox("YEAR GRADUATED", range(1900, 2101), index=124)
            st.write("   ")
            
            st.write("   ")
            cg = st.write("COLLEGE")
            ncg = st.text_input("SCHOOL NAME", "SNSU")
            ycg = st.text_input("YEAR GRADUATED"," ")
            
            # ---- FAMILY BACKGROUND PAGE ----
            st.title("FAMILY BACKGROUND")
            # --- MOTHER ---
            st.write("MOTHER")
            mother = st.text_input("Name", "Janice S. Comandante")
            mbday = st.date_input("Birthday", datetime.date(1985, 11, 4))
    
            st.write("   ")  # Spacing

            # --- FATHER ---
            st.write("FATHER")
            father = st.text_input("Name", "Eddie F. Comandante")
            fbday = st.date_input("Birthday", datetime.date(1978, 7, 31))
    st.write("---")

    # --- NAVIGATION BUTTONS ---
    with st.container():
        col1, col2, col3 = st.columns([3, 1, 3])  # Center the button
    with col2:
        if st.button("NEXT"):
            navigate_to("CONTACTS")


 
# ---- CONTACT PAGE ----
elif st.session_state.page == "CONTACTS":
    st.title("CONTACTS AND MEDIA")
    with st.container():
        left_column, right_column = st.columns(2)  # Alignment
        with left_column:
            num = st.text_input("CONTACT NUMBER", "09504129544")
            gmail = st.text_input("GMAIL ACCOUNT", "ejlawrencecomandante054@gmail.com")
            discord = st.text_input("DISCORD ACCOUNT"," ")
        with right_column:
            fb = st.text_input("FACEBOOK ACCOUNT", "EJ Lawrence Comandante")
            instagram = st.text_input("INSTAGRAM ACCOUNT", "N/A")
            twitter = st.text_input("TWITTER ACCOUNT", "N/A")
            youtube = st.text_input("YOUTUBE ACCOUNT", "N/A")
    st.write("---")
    
    # --- NAVIGATION BUTTONS ---
    with st.container():
        col1, col2, col3 = st.columns([3, 1, 3])  # Center the button
    with col2:
        if st.button("BACK"):
            navigate_to("PERSONAL")
