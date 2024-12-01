import streamlit as st
import plotly.express as px
from PIL import Image
import numpy as np

def show_project_demo():
    st.subheader("AI Medical Image Analysis Demo")
    
    uploaded_file = st.file_uploader("Choose a medical image...", 
                                   type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        if st.button("Analyze Image"):
            # Simulated analysis
            progress_bar = st.progress(0)
            for i in range(100):
                progress_bar.progress(i + 1)
            
            # Sample results
            results = {
                'Normal': 0.85,
                'Abnormal Type A': 0.10,
                'Abnormal Type B': 0.05
            }
            
            fig = px.bar(x=list(results.keys()), 
                        y=list(results.values()),
                        title='Analysis Results')
            st.plotly_chart(fig)

def show_project_list():
    st.subheader("Recent Projects")
    
    projects = [
        {
            "title": "AI for Medical Image Classification",
            "description": "Developed deep learning models for medical image classification",
            "tech": ["Python", "TensorFlow", "Medical Imaging"]
        },
        {
            "title": "Hibernating Myocardium Detection",
            "description": "Machine learning approach to identify hibernating myocardium",
            "tech": ["Python", "scikit-learn", "Nuclear Medicine"]
        },
        {
            "title": "Gastrointestinal Bleeding Detection",
            "description": "Advanced algorithms for detecting GI bleeding",
            "tech": ["Python", "Deep Learning", "Medical Analysis"]
        }
    ]
    
    for project in projects:
        with st.expander(project["title"]):
            st.write(project["description"])
            st.write("**Technologies:**")
            st.write(", ".join(project["tech"]))

def show():
    st.title("AI Projects")
    
    tab1, tab2 = st.tabs(["Interactive Demo", "Project List"])
    
    with tab1:
        show_project_demo()
    
    with tab2:
        show_project_list()
