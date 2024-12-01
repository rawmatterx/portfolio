# Interactive Medical Professional Portfolio

A Streamlit-based interactive portfolio website designed for medical professionals, featuring research visualization, AI project demonstrations, and professional achievements.

## 🌟 Features

### 📊 About Section
- Professional profile overview
- Interactive skills visualization
- Key metrics dashboard
- Professional timeline

### 🔬 Research Section
- Publication analytics
- Citation metrics visualization
- Research focus areas with interactive graphs
- Publication list with detailed views

### 💻 Projects Section
- Interactive AI medical image analysis demo
- Project showcase with expandable details
- Technology stack visualization
- Live demo capabilities

### 📫 Contact Section
- Interactive contact form
- Professional information display
- Location and availability details
- Social media integration

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd interactive-portfolio
```

2. Create and activate a virtual environment (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📁 Project Structure
```
portfolio/
├── app.py                  # Main application file
├── requirements.txt        # Project dependencies
├── README.md              # Project documentation
└── pages/                 # Application pages
    ├── __init__.py
    ├── about.py           # About page component
    ├── research.py        # Research page component
    ├── projects.py        # Projects page component
    └── contact.py         # Contact page component
```

## 🛠️ Technology Stack

- **Streamlit**: Main web application framework
- **Plotly**: Interactive data visualization
- **Pandas**: Data manipulation and analysis
- **PIL**: Image processing
- **NumPy**: Numerical computations

## 📦 Dependencies

```text
streamlit==1.24.0
plotly==5.15.0
pandas==2.0.3
numpy==1.24.3
pillow==9.5.0
```

## 🎨 Customization

### Modifying the Theme
You can customize the appearance by modifying the custom CSS in `app.py`:

```python
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
    ...
    </style>
""", unsafe_allow_html=True)
```

### Adding New Pages
1. Create a new Python file in the `pages` directory
2. Define a `show()` function in your page file
3. Import and add the page to the navigation in `app.py`

## 🔧 Configuration

You can modify the page configuration in `app.py`:

```python
st.set_page_config(
    page_title="Your Name - Portfolio",
    page_icon="🏥",
    layout="wide"
)
```

## 📱 Responsive Design

The portfolio is designed to be responsive and works well on:
- Desktop browsers
- Tablets
- Mobile devices

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the `LICENSE` file for details

## 🙏 Acknowledgments

- Thanks to the Streamlit team for the amazing framework
- Plotly for the interactive visualization capabilities
- The open-source community for various inspiration and components

## 📞 Support

For support, email arup.fav@gmail.com or open an issue in the repository.

## 🚧 Future Improvements

- [ ] Add authentication system
- [ ] Implement dark mode
- [ ] Add more interactive AI demos
- [ ] Enhance visualization options
- [ ] Add multi-language support
- [ ] Integrate with publication APIs
