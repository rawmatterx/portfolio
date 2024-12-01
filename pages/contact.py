import streamlit as st

def show_contact_form():
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
            subject = st.text_input("Subject")
        
        with col2:
            message = st.text_area("Message", height=130)
        
        submit = st.form_submit_button("Send Message")
        
        if submit:
            st.success("Thank you for your message! I'll get back to you soon.")

def show_contact_info():
    st.subheader("Quick Connect")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Contact Details
        📧 arup.fav@gmail.com  
        📱 8348524209
        
        ### Social Media
        🔗 [LinkedIn](www.linkedin.com/in/aruproy09)
        """)
    
    with col2:
        st.markdown("""
        ### Location
        All India Institute of Medical Sciences (AIIMS)  
        New Delhi, Delhi, India
        
        ### Office Hours
        Monday - Friday: 9:00 AM - 5:00 PM  
        Saturday: 9:00 AM - 1:00 PM
        """)

def show():
    st.title("Get in Touch")
    show_contact_info()
    st.divider()
    show_contact_form()
