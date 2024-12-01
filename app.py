import streamlit as st
import pages.about as about
import pages.research as research
import pages.projects as projects
import pages.contact as contact

# Page configuration
st.set_page_config(
    page_title="Dr. Arup Roy - Portfolio",
    page_icon="🏥",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .title {
        font-size: 3rem;
        font-weight: bold;
        color: #1E3A8A;
    }
    .subtitle {
        font-size: 1.5rem;
        color: #475569;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
def sidebar():
    with st.sidebar:
        st.image("https://via.placeholder.com/150", caption="Dr. Arup Roy")
        st.title("Navigation")
        return st.radio(
            "Go to",
            ["About", "Research", "Projects", "Contact"]
        )

# Main App
def main():
    page = sidebar()
    
    if page == "About":
        about.show()
    elif page == "Research":
        research.show()
    elif page == "Projects":
        projects.show()
    elif page == "Contact":
        contact.show()

if __name__ == "__main__":
    main()
