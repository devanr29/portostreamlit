import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Set page config
st.set_page_config(page_title="Devan Ramadhana's Portfolio", page_icon="📚", layout="wide")

# Load an image for the profile
profile_image = Image.open("profile.jpeg")  # Replace with the path to your profile photo

# Navigation bar
selected_page = option_menu(
    menu_title=None,  # Set None to display only icons
    options=["About Me", "Portfolio", "Experience", "Education", "Certifications & Skills", "Contact"],
    icons=["person", "folder", "briefcase", "mortarboard", "trophy", "phone"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Page content
if selected_page == "About Me":
    st.title("Hello, I'm Devan Ramadhana 👋")
    st.image(profile_image, width=200, caption="Devan Ramadhana")
    st.markdown(
        """ 
        ### Overview
        A visionary and detail-oriented fresh graduate in **Telecommunication Engineering** with strong expertise in **data science**, **machine learning**, and **IoT**. Experienced in developing predictive models and real-time monitoring systems using **Python**, **C++**, and data visualization tools like **Tableau**.

        I am actively seeking opportunities in **technology consulting** and **data-driven decision-making roles** to deliver impactful solutions.

        - ✅ Analytical Thinker
        - ✅ Detail-Oriented Professional
        - ✅ Collaborative Leader
        """
    )

elif selected_page == "Portfolio":
    st.title("My Portfolio")
    st.markdown("Here are some of the projects I have worked on:")
    
    with st.container():
        st.subheader("1. GoatGuard (Innovillage 2023)")
        st.image("goatguard_screenshot.jpg", caption="GoatGuard Project", use_column_width=True)
        st.write("- **Description**: An IoT-based device integrated with machine learning to detect goat diseases early.")
        st.write("- **Technology**: Python, IoT, Machine Learning")
        st.write("- **Outcome**: Improved livestock health monitoring and secured Innovillage funding.")
        st.markdown("[GoatGuard Project Link](https://ibb.co.com/FsPHmRB)")

    with st.container():
        st.subheader("2. MyIpond: A Water Quality Monitoring System")
        st.image("myipond_screenshot.jpg", caption="MyIpond Project", use_column_width=True)
        st.write("- **Description**: Real-time monitoring system for catfish ponds, measuring temperature, turbidity, and pH levels.")
        st.write("- **Technology**: Python, IoT, Machine Learning")
        st.write("- **Outcome**: Enhanced pond management and productivity.")
        st.markdown("[MyIpond Project Link](https://myi-pond.vercel.app/)")

elif selected_page == "Experience":
    st.title("Work Experience")
    st.markdown(
        """ 
        - **Vice President**, Himpunan Mahasiswa Teknik Telekomunikasi (2024 - Present)
          - Supervised and coordinated activities across 5 departments.
          - Facilitated collaboration between ministries and departments to ensure smooth operations.

        - **Research Assistant**, Big Data Division, Cybersecurity, Multimedia, and Big Data Laboratory (2022 - Present)
          - Developed machine learning models for water quality analysis and created Tableau dashboards.
          - Participated in data challenges like Kaggle, JOINTS DATA COMPETITION, and COMPFEST Data Analytics Dash.
          - Conducted sentiment analysis using web scraping and natural language processing (NLP).

        - **Head of Public Relations**, Cybersecurity, Multimedia, and Big Data Laboratory (2024 - Present)
          - Established media partnerships and led branding initiatives to enhance public image.
        """
    )

elif selected_page == "Education":
    st.title("Education")
    st.markdown(
        """ 
        - **Bachelor’s Degree in Telecommunication Engineering**, Telkom University (2021-2025)
          - GPA: 3.30 / 4.00
          - Thesis: Analyzing water quality parameters (Temperature, pH, Turbidity) for catfish growth using Machine Learning.
        """
    )

elif selected_page == "Certifications & Skills":
    st.title("Certifications & Skills")
    st.markdown(
        """ 
        ### Certifications
        - [Intro to Data Science (Cisco)](https://www.credly.com/badges/05cdc46b-3062-48c4-8840-659497579078/linked_in_profile)
        - [Belajar Visualisasi Data (Dicoding Academy)](https://www.dicoding.com/certificates/QLZ9QV0M9Z5D)
        - [Intro to Machine Learning (Kaggle)](https://www.kaggle.com/learn/certification/devanrmdhna/intro-to-machine-learning)
        - [Belajar Machine Learning untuk Pemula (Dicoding Academy)](https://www.dicoding.com/certificates/RVZKOE5V4PD5)
        - [Memulai Pemrograman dengan Python (Dicoding Academy)](https://www.dicoding.com/certificates/N9ZO6Y15RXG5)
        - [Networking Basics (Cisco)](https://www.credly.com/badges/ed5129c7-c4e5-4267-a474-78c5ac0755c5/linked_in_profile)
        - [Data Analytics Essentials (Cisco)](https://www.credly.com/badges/1461f9e5-ce2e-41c3-8f5c-233e3c17b2f2/linked_in_profile)
        - [Microsoft Excel from Beginner to Advanced (Udemy)](https://www.udemy.com/certificate/UC-326f3c8e-41e0-453d-981f-bf9a6800d944/)
        - [Intro to Data Analytics (RevoU)](https://certificates.revou.co/devan-ramadhana-certificate-completion-damc23.pdf)
        - [Belajar Dasar Structured Query Language SQL (Dicoding Academy)](https://www.dicoding.com/certificates/81P27O35QZOY)
        - [Intermediate SQL (Sololearn)](https://www.sololearn.com/certificates/CC-UTFTEBFL)
        - [Red Hat System Administration II (Red Hat)](https://media.licdn.com/dms/image/v2/D562DAQG5uFBHcSoGRw/profile-treasury-document-cover-images_480/profile-treasury-document-cover-images_480/0/1713541275665?e=1736604000&v=beta&t=tz5q86nzGZaRdwjrgqFbJnuH1E9ERh9mZqp0Vj3ewsA)
        - [Latihan Keterampilan Manajemen Mahasiswa - Tingkat Menengah (Kemdikbudristek)](https://media.licdn.com/dms/image/v2/D562DAQEpdMK1dAV1JA/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1723105090837?e=1736604000&v=beta&t=80EEdgv984HwjpXjYOA0GBbHzbCgyz-soapEfrhx0f0)
        
        ### Skills
        - **Technical Skills**: Python, C, SQL, Machine Learning, Data Visualization, IoT System Design
        - **Soft Skills**: Leadership, Teamwork, Critical Thinking, Time Management, Decision-Making
        - **Tools**: Tableau, Microsoft Office, Cisco Packet Tracer
        """
    )

elif selected_page == "Contact":
    st.title("Contact Me")
    st.markdown(
        """ 
        I am always open to professional discussions, collaborations, or new opportunities.

        - 📧 **Email**: [devanr2911@gmail.com](mailto:devanr2911@gmail.com)
        - 📞 **Phone**: +62 857-2251-6521
        - 🔗 **LinkedIn**: [linkedin.com/in/devanrmdhna](https://linkedin.com/in/devanrmdhna)
        - 🎨 **GitHub**: [github.com/devanrmdhna](https://github.com/devanrmdhna)
        """
    )
    st.markdown("Thank you for visiting my portfolio!")
