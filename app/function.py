import streamlit as st
import os




def profilePage():
    search_term = st.text_input("Search for something on my profile", placeholder="Search on this web")
    
    if search_term:
        st.write(f"Searching for: {search_term}")

    col1, col2 = st.columns([2,2])  

    # Path gambar
    image_path = "D:\\.CODE\\Streamlit\\profilePage\\image\\sosmed\\instagram.png"

    # Cek apakah file ada
    if not os.path.exists(image_path):
        st.error(f"File gambar tidak ditemukan di {image_path}")
    else:
        with col1:
            st.image(image_path, width=300, caption="Bima Cahya Rizqullah")  

    with col2:
        st.header("Profile Page")
        st.caption("Bima Cahya Rizqullah (December 11 2004, Magetan Regency)")
        st.caption("D3 Information Technology Madiun State Polytechnic College")

        st.subheader("Introduction")
        st.caption(
            "Hello, I'm Bima Cahya Rizqullah. I'm from Magetan Regency, Indonesia. "
            "I am an Information Technology Student at the Madiun State Polytechnic. "
            "My goal in creating this website is to introduce myself in the field of IT and also to introduce some of the projects "
            "that I have developed in my college. Thank you, I hope you can find out some of the progress that I have learned during my lectures."
        )

        st.subheader("Hobby")
        st.caption(
            "I have some hobbies that are common to everyone, namely playing games, and also playing musical instruments such as guitar. "
            "I only do these hobbies when I have free time, such as playing games."
        )
        st.caption(
            "Playing games is a hobby that I always do every day. Currently, I play Mobile Legends and I hope to develop some MOBA games. "
            "The first time I played MOBA games was when I was in elementary school, and at that time I only played Mobile Legends alone. "
            "Time after time, Mobile Legends is currently one of the best MOBA games which has a large market in Indonesia."
        )




def educationPage():

    st.header("Educations")
    st.caption("Manisrejo 2 Elementary School (2010 - 2016)")
    st.caption("Karangrejo 1 Junior High School (2017 - 2019)")
    st.caption("Karas 1 Senior High School (2020 - 2023)")
    st.caption("Madiun State Polytechnic (2023 - Current)")




def socialMediaPage():

    st.header("Social Media")
    st.markdown("Follow my social media to find out some of my daily life")

    sos1, sos2 = st.columns([1,1])

    with sos1:
        st.image("D:\.CODE\Streamlit\profilePage\image\sosmed\instagram.png", width=58, use_container_width=False)
        st.caption("@bimacahyaaar")
    with sos2:
        st.image("D:\.CODE\Streamlit\profilePage\image\sosmed\instagram.png", width=58, use_container_width=False)
        st.caption("@mib.aja_")



def mobileProgrammingPage():
    st.header("Android Studio")



def webProgrammingPage():
    st.header("Laravel")
