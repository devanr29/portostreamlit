import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from base64 import b64encode

# Set page config
st.set_page_config(page_title="Devan Ramadhana's Portfolio", page_icon="📚", layout="wide")

# Function to resize images to the same size
from PIL import ImageOps

def resize_image(image_path, size=(300, 300)):
    img = Image.open(image_path)
    return img.resize(size)

# Resize and standardize images for GoatGuard
goatguard_images = [
    resize_image("goatguard1.JPG").rotate(-90, expand=True),
    resize_image("goatguard2.JPG").rotate(-90, expand=True),
    resize_image("goatguard3.JPG").rotate(-90, expand=True),
    resize_image("goatguard4.jpeg")
]

# Resize and standardize images for MyIpond
myipond_images = [
    resize_image("ipond1.jpeg"),
    resize_image("ipond2.jpeg"),
    resize_image("ipond3.jpeg")
]

# Navigation bar
selected_page = option_menu(
    menu_title=None,  # Set None to display only icons
    options=["About Me", "Projects", "Experience", "Certifications & Skills", "Contact"],
    icons=["person", "folder", "briefcase", "mortarboard", "trophy", "phone"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Page content
if selected_page == "About Me":
    st.title("Hello, I'm Devan Ramadhana 👋")
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.image("profile.jpeg", width=380, caption="Devan Ramadhana")
    
    with col2:
        st.markdown(
            """ 
            ### Overview
            I am a **responsible** and **visionary** fresh graduate with a bachelor's degree in Telecommunication Engineering and experience as a laboratory assistant in *Data Analytics*, **Data Science** and **Internet of Things**. As Vice President of my student association and former head of advanced education for a nature enthusiasts' club, I have developed strong **leadership**, **teamwork**, and **communication** skills. My active involvement in campus and community activities has broadened my insights, enhanced my **problem-solving** abilities, and fostered a **deep curiosity** for learning.

            I am actively seeking opportunities in **technology consulting** and **data-driven decision-making roles** to deliver impactful solutions.

            - ✅ Analytical Thinker
            - ✅ Detail-Oriented Professional
            - ✅ Collaborative Leader
            
            ### Education
             - **Bachelor’s Degree in Telecommunication Engineering**, Telkom University (2021-2025)
              - GPA: 3.30 / 4.00
              - Thesis: Analyzing water quality parameters (Temperature, pH, Turbidity) for catfish growth using Machine Learning.
            """
        )
        # Reading Profile
    with open("CV Devan Ramadhana.pdf", "rb") as pdf_file:
       pdf_bytes = pdf_file.read()

    st.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="CV Devan Ramadhana.pdf", mime="application/pdf",)

elif selected_page == "Projects":
    st.title("My Projects")
    st.markdown("Here are some of the projects I have worked on:")
    
    with st.container():
        st.subheader("1. GoatGuard (Innovillage 2023)")
        st.write("- **Description**: An IoT-based device integrated with machine learning to detect goat diseases early.")
        st.write("- **Technology**: Python, IoT, Machine Learning")
        st.write("- **Achievement**: Top 163 and Secured Innovillage 2023 funding.")
        st.markdown("[Innovillage 2023 Certificated](https://ibb.co.com/FsPHmRB)")

        # Photo Gallery for GoatGuard project
        st.markdown("#### Project Gallery")
        cols = st.columns(4)  # Create 4 columns for the gallery
        for idx, image in enumerate(goatguard_images):
            with cols[idx]:
                st.image(image, caption=f"GoatGuard Image {idx+1}", use_container_width=True)

    with st.container():
        st.subheader("2. MyIpond: A Water Quality Monitoring System")
        st.write("- **Description**: Real-time monitoring system for catfish ponds, measuring temperature, turbidity, and pH levels.")
        st.write("- **Technology**: Python, IoT, Machine Learning")
        st.write("- **Outcome**: Enhanced pond management and productivity.")
        st.markdown("[MyIpond Website Link](https://myi-pond.vercel.app/)")

        # Photo Gallery for MyIpond project
        st.markdown("#### Project Gallery")
        cols = st.columns(3)  # Create 3 columns for the gallery
        for idx, image in enumerate(myipond_images):
            with cols[idx]:
                st.image(image, caption=f"MyIpond Image {idx+1}", use_container_width=True)

    with st.container():
        st.subheader("3. Sentiment Analysis")
        st.write("- **Description**: Collected review data on film series using web scraping techniques from IMDb and conducted sentiment analysis using NLTK to identify audience sentiment trends and patterns.")
        st.write("- **Technology**: Python, NLTK, Web Scraping")
        st.write("- **Outcome**: Sentiment analysis of series reviews.")
        st.markdown("[Read the Medium Article](https://medium.com/@devanr2911/analyzing-house-of-the-dragon-user-reviews-on-imdb-using-sentiment-analysis-with-nltk-1f5a6129b2ce)")

    with st.container():
        st.subheader("4. Predicting Air Quality Using Machine Learning")
        st.write("- **Description**: Utilized machine learning approaches to forecast the level of air quality based on environmental variables present in the provided dataset.")
        st.write("- **Technology**: Python, Machine Learning")
        st.write("- **Outcome**: Machine learning model to predict air quality.")
        st.markdown("[Read the Medium Article](https://medium.com/@devanr2911/predicting-air-quality-with-machine-learning-af654d8a259e)")

elif selected_page == "Experience":
    st.title("Experience")
    st.markdown(
        """ 
    - **Multimedia, Big Data and Cybersecurity Laboratory** (2022 - 2025)
        - **Head of Public Relation**
          - Establishing media partnerships with organizations outside the campus.
          - Acting as a liaison between the internal laboratory and external parties.
          - Led branding initiatives to enhance the lab's public image and visibility.    
        - **Research Assistant**
          - Developed machine learning models for water quality analysis and created Tableau dashboards.
          - Participated in data challenges like Kaggle, JOINTS DATA COMPETITION, and COMPFEST Data Analytics Dash.
          - Conducted sentiment analysis using web scraping and natural language processing (NLP).

     - **Himpunan Mahasiswa Teknik Telekomunikasi** (2023 - 2025)
        - **Vice President**
          - Supervised and coordinated activities across 5 departments.
          - Facilitated collaboration between ministries and departments to ensure smooth operations.
          - Ensure effective management and operation of 5 departments under the Ministries
          - Monitor progress and performance of ministry initiatives and projects
          - Maintain readiness to lead the association in emergency situations or when the President is unavailable
        - **Senior Staff of Public Relations Department**
          - Coordinator of Monthly Talk show event with the Alumni of Telecommunication Engineering to sharing experience or knowledge about them.
          - Leading a “Telco Thanksgiving” Event to appreciate external organization for keep supporting our event and programs.
        - **Junior Staff of Public Relations Department**
          - Moderating one of the Public Relation events, "Telcotalks," on Live Instagram for HMTT, I ensure smooth operations and engaging discussions.Leading a “Telco Thanksgiving” Event to appreciate external organization for keep supporting our event and programs.

    - **Perhimpunan Penjelajah Alam Jamadagni** (2021 - 2024)
        - **Head of DIKLAT 47**
          - Creating a plan for the development of young members.
          - Ensuring the attainment of values instilled in young members.
          - As the highest authority, making the decision to appoint young members as full members.
        - **Head of Secretariat and Logistic Division**
          - Recording all the equipment owned by the Organization.
          - Managing all borrowed equipment and equipment borrowings.
          - Organizing a monthly office cleaning activity in secretariat
        - **Field Coordinator of Mt.Sindoro Expedition DIKLAT 43 **
          - Keeping the event on track from the preparation.
          - Making decisions from any problem on the field.
          - Ensure the safety of all young staff 43 Jamadagni.
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
