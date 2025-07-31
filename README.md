# AI Resume Scanner

A Streamlit web app that analyzes your resume PDF to provide instant feedback on structure, keywords, grammar, readability, and overall quality.

---

## Features

- Upload resume in PDF format
- Detect key resume sections (Education, Experience, Skills, Projects, Contact, Certifications)
- Identify important keywords related to tech and data science
- Check grammar issues using LanguageTool
- Calculate readability score (Flesch Reading Ease)
- Provide an overall resume quality score and suggestions
- Friendly and interactive Streamlit UI for easy use

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-scanner.git
cd ai-resume-scanner
(Optional) Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
Running the App
Start the Streamlit app with:

bash
Copy
Edit
streamlit run app.py
This will open a new tab in your default web browser at http://localhost:8501, where you can upload your resume PDF and see the analysis results.

How It Works
The app extracts text from the uploaded PDF using PyMuPDF

It scans for key resume sections by looking for section headers

Keywords relevant to data science and software development are detected

Grammar is checked using language-tool-python

Readability is measured with textstat

Finally, the app scores the resume and displays actionable feedback

Project Structure
bash
Copy
Edit
ai-resume-scanner/
│
├── app.py              # Streamlit app code
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .gitignore          # Git ignore rules
Dependencies
Streamlit

PyMuPDF (fitz)

language-tool-python

textstat

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
Created by Vyaas R. Subramanian
Email: vsubs28@gmail.com
Portfolio: https://vyaasportfolio.netlify.app/
LinkedIn: https://linkedin.com/in/vyaas-subramanian-427468237

