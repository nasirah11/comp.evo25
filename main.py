import streamlit as st

st.set_page_config(page_title="My Resume", page_icon=":briefcase:", layout="wide")

# ---- HEADER ----
st.title("🌟 Siti Nasirah")
st.subheader("Year 3 Student at University Malaysia Kelantan (2023)")
st.write("---")

# ---- CONTACT INFO ----
st.header("📞 Contact Information")
st.write("Email: snasirah7l@gmail.com")
st.write("Phone: +60 19-470 53 61")
st.write("LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)")

st.write("---")

# ---- EDUCATION ----
st.header("🎓 Education")
st.write("**Bachelor of Information Technology** — University Malaysia Kelantan (Year 3, 2023 - Present)")

st.write("---")

# ---- WORK EXPERIENCE ----
st.header("💼 Work Experience")
st.write("Intern at Hospital Sultan Ismail 2021 / Part-time Experience at Aeon")
st.write("- My internship at Hospital Sultan Ismail, Johor Bahru was 8 months.")

st.write("---")

# ---- SKILLS ----
st.header("🛠 Skills")
st.write("- Python")
st.write("- Streamlit")
st.write("- SQL")
st.write("- Data Analysis")
st.write("- Communication & Teamwork")

st.write("---")

# ---- PROJECTS ----
st.header("🚀 Projects & Achievements")
st.write("**Resume Web App** — Built my resume page with Streamlit and deployed online.")
st.write("**Final Year Project** — I take my final year project 1 this semester.")

st.write("---")

# ---- FOOTER ----
st.markdown(
    "<p style='text-align: center; color: grey;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
