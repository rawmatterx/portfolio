import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def show_publications():
    st.subheader("Publications")
    
    publications = [
        {
            "title": "Diagnostic accuracy of RBC scintigraphy and CTA for detection of patients with suspected lower gastrointestinal bleeding",
            "year": 2023,
            "citations": 20,
            "journal": "Nuclear Medicine Communications"
        },
        {
            "title": "Can machine learning decode hibernating myocardium from rest myocardial perfusion images?",
            "year": 2022,
            "citations": 15,
            "journal": "Journal of Nuclear Medicine"
        },
        {
            "title": "A Novel Approach to Identifying Hibernating Myocardium Using Radiomics-Based Machine Learning",
            "year": 2023,
            "citations": 10,
            "journal": "European Journal of Nuclear Medicine"
        }
    ]
    
    for pub in publications:
        with st.expander(pub["title"]):
            st.write(f"**Year:** {pub['year']}")
            st.write(f"**Journal:** {pub['journal']}")
            st.write(f"**Citations:** {pub['citations']}")

def show_citation_metrics():
    st.subheader("Citation Metrics")
    
    data = {
        'Year': [2021, 2022, 2023, 2024],
        'Citations': [5, 15, 25, 45]
    }
    df = pd.DataFrame(data)
    
    fig = px.line(df, x='Year', y='Citations',
                 title='Citation Growth',
                 markers=True)
    
    st.plotly_chart(fig)

def show_research_focus():
    st.subheader("Research Focus Areas")
    
    focus_areas = {
        'Area': ['AI in Nuclear Medicine', 'Medical Imaging', 'Machine Learning',
                'Diagnostic Accuracy', 'Clinical Research'],
        'Papers': [3, 2, 2, 1, 1],
        'Impact': [90, 85, 85, 80, 75]
    }
    
    df = pd.DataFrame(focus_areas)
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df['Papers'],
        y=df['Impact'],
        mode='markers+text',
        text=df['Area'],
        textposition='top center',
        marker=dict(size=df['Papers']*20, color=df['Impact'],
                   colorscale='Blues',
                   showscale=True)
    ))
    
    fig.update_layout(
        title='Research Areas Impact',
        xaxis_title='Number of Papers',
        yaxis_title='Impact Score'
    )
    
    st.plotly_chart(fig)

def show():
    st.title("Research & Publications")
    show_citation_metrics()
    st.divider()
    show_research_focus()
    st.divider()
    show_publications()
