import streamlit as st

# Function to display education section
def display_education():
    st.header("EDUCATION")
    st.subheader("Bachelor of Technology in Computer Science")
    st.write("Vignan’s Institute of Engineering for Women (Expected 2026)")
    st.write("Specialization: Artificial Intelligence and Machine Learning")
    st.write("Current CGPA: 8.17")

    st.subheader("Intermediate")
    st.write("Ascent Junior College")
    st.write("MPC")
    st.write("CGPA: 8.11")

    st.subheader("SSC")
    st.write("Sri Chaitanya E.M School")
    st.write("CGPA: 10")

# Function to display skills section
def display_skills():
    st.header("SKILLS")
    st.write("**Technical Skills**: Power BI, Natural Language Processing, Comfy UI, NumPy, Pandas, Streamlit, Data Analysis")
    st.write("**Frameworks**: TensorFlow, Scikit-learn")
    st.write("**Languages**: Java, Python")
    st.write("**Cybersecurity**: Basics of Nmap Commands, Kali Linux, Burp Suite, Metasploit Framework")
    st.write("**Soft Skills**: Communication, Leadership, Team Work, Adaptability")

# Function to display internship section
def display_internships():
    st.header("INTERNSHIP")
    st.subheader("AI Intern")
    st.write("Edunet")
    st.write("• Worked on 'Image Generation using stable diffusion models and comfy UI'")
    st.write("• Published Articles on the U-net Architecture, diffusion models ([Read It here](#))")

    st.subheader("AI/ML Intern")
    st.write("ExcelR")
    st.write("• Worked on a minor project 'Rule based chat bot'")
    st.write("• Prepared a Report on how Alexa works")
    st.write("• Gained knowledge on AI, ML, NLP")

# Function to display projects section
def display_projects():
    st.header("PROJECTS")
    st.subheader("Image generation with stable diffusion using Comfy UI (Jan 2025, Remote)")
    st.write("• Stable Diffusion Image Generation: Implemented Stable Diffusion models via ComfyUI and Hugging Face for image synthesis")
    st.write("• Diffusion Architecture Exploration: Investigated forward/reverse diffusion processes and model mechanics through practical experimentation")
    st.write("• ComfyUI Node-Based Pipelines: Built and manipulated diffusion pipelines using ComfyUI’s node-based interface")
    st.write("• Pre-trained Model Integration: Utilized pre-trained Stable Diffusion models from Hugging Face")
    st.write("• Image Generation and Analysis: Successfully generated images and gained insights into diffusion model functionality")

    st.subheader("Crime Data Analysis and Visualization Project - Power BI (June 2024-July 2024, Remote)")
    st.write("• Interactive Crime Data Visualization: Developed a Power BI dashboard visualizing trends in a Kaggle crime dataset")
    st.write("• Data Cleaning and Feature Engineering: Enhanced the dataset through cleaning and feature engineering for improved analysis")
    st.write("• Temporal, Geographic, and Demographic Analysis: Explored trends across time, location, and demographics using interactive visualizations")
    st.write("• Ethical Data Handling: Prioritized ethical considerations, responsible visualization, and thorough documentation")
    st.write("• Objective Crime Pattern Analysis: Focused on objective analysis of potential behavioral patterns, avoiding sensationalism ([View it here](#))")

    st.subheader("Exploratory Data Analysis of Cyber Security Breaches")
    st.write("• Cybersecurity Breach EDA: Performed exploratory data analysis of cybersecurity breaches using Python, Pandas, and Matplotlib")
    st.write("• Data Cleaning and Visualization: Cleaned and visualized security incident data using histograms, heatmaps, and box plots to reveal breach patterns")
    st.write("• Actionable Insights and Reproducibility: Generated insights to inform security strategy improvements, with reproducible code ensuring data integrity ([View it here](#))")

# Function to display certifications section
def display_certifications():
    st.header("CERTIFICATIONS")
    st.write("• Elite Certificate of NPTEL on AI: Search Methods For Problem Solving ([View it here](#))")
    st.write("• EDX Certificate On Python and Pandas For Data Engineering ([View it here](#))")
    st.write("• AI/ML for Geodata Analysis from Indian Institute Of Remote Sensing ([View it here](#))")
    st.write("• Badges and Certificates On Hackerrank ([View it here](#))")

# Function to display extra-curricular activities section
def display_extra_curricular():
    st.header("EXTRA-CURRICULAR ACTIVITIES")
    st.write("• Actively write Articles On Medium")
    st.write("• AI Club core member of our College")
    st.write("• 2X Google Developer Student Club study jams Participant")
    st.write("• 1X Google Developer Groups study jam participant")
    st.write("• Participated in a 10-day and a 2-day Cybersecurity Training Workshop")

def main():
    st.title("VALLABHAJOSYULA SRI HARSHINI")
    st.write("+91 9398544024 ⋄ Visakhapatnam, Andhra Pradesh")
    st.write("vallabhajosyulasriharshini@gmail.com ⋄ [LinkedIn](https://linkedin.com) ⋄ [GitHub](https://github.com)")

    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Go to", ["Education", "Skills", "Internships", "Projects", "Certifications", "Extra-Curricular Activities"])

    if options == "Education":
        display_education()
    elif options == "Skills":
        display_skills()
    elif options == "Internships":
        display_internships()
    elif options == "Projects":
        display_projects()
    elif options == "Certifications":
        display_certifications()
    elif options == "Extra-Curricular Activities":
        display_extra_curricular()

if __name__ == "__main__":
    main()