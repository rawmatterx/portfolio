import streamlit as st
import plotly.express as px
import pandas as pd

def show_profile():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("Dr. Arup Roy")
        st.subheader("Senior Resident | MD Nuclear Medicine | AIIMS NEW DELHI")
        
        st.write("""
        The intersection of healthcare and artificial intelligence is where our team at AIIMS 
        is making groundbreaking strides, particularly in the realm of Nuclear Medicine. 
        With a focus on the application of AI for medical diagnostics, prognosis, and treatment, 
        our research is at the forefront of revolutionizing patient care.
        """)
    
    with col2:
        # Contact Information
        st.subheader("Contact")
        st.write("📧 arup.fav@gmail.com")
        st.write("🔗 [LinkedIn](www.linkedin.com/in/aruproy09)")
        st.write("📱 8348524209")

def show_metrics():
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Publications", "3", "+1")
    with col2:
        st.metric("Citations", "45", "+12")
    with col3:
        st.metric("Projects", "5", "+2")
    with col4:
        st.metric("h-index", "3", "+1")

def show_skills():
    st.subheader("Skills & Expertise")
    
    skills_data = {
        'Skill': ['AI/ML', 'Nuclear Medicine', 'Medical Imaging', 
                 'Research', 'Patient Care', 'Data Analysis'],
        'Level': [90, 95, 85, 80, 90, 85]
    }
    
    df = pd.DataFrame(skills_data)
    fig = px.bar(df, x='Skill', y='Level', 
                title='Skills Overview',
                color='Level',
                color_continuous_scale='blues')
    
    st.plotly_chart(fig)

def show():
    show_profile()
    st.divider()
    show_metrics()
    st.divider()
    show_skills()
