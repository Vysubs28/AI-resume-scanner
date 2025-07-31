import streamlit as st
import fitz  # PyMuPDF
import language_tool_python
import textstat
import re

# Functions from before
def find_sections(text):
    sections = []
    section_keywords = {
        'summary': ['summary', 'objective'],
        'education': ['education', 'degree', 'university', 'college'],
        'experience': ['experience', 'internship', 'work', 'employment'],
        'skills': ['skills', 'technologies', 'tools'],
        'projects': ['projects', 'project'],
        'contact': ['phone', 'email', 'linkedin', 'contact'],
        'certifications': ['certification', 'certificate'],
    }
    text_lower = text.lower()
    for section, keywords in section_keywords.items():
        if any(k in text_lower for k in keywords):
            sections.append(section)
    return sections

def count_keywords(text, keywords):
    found = []
    text_lower = text.lower()
    for kw in keywords:
        if kw.lower() in text_lower:
            found.append(kw)
    return found

def count_grammar_issues(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    return len(matches)

def readability_score(text):
    return textstat.flesch_reading_ease(text)

def score_resume(sections, keywords_found, grammar_issues, word_count, readability):
    score = 0
    score += len(sections) * 1.5
    score += len(keywords_found) * 1.0
    score -= (grammar_issues / 50)
    if word_count < 200 or word_count > 2000:
        score -= 2
    if readability < 30:
        score -= 1
    elif readability > 80:
        score -= 1
    score = max(0, min(10, score))
    return round(score, 1)

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def analyze_resume(text):
    sections = find_sections(text)
    keywords_to_search = ['python', 'java', 'sql', 'machine learning', 'ai', 'c#', 'data science']
    keywords_found = count_keywords(text, keywords_to_search)
    grammar_issues = count_grammar_issues(text)
    word_count = len(re.findall(r'\w+', text))
    readability = readability_score(text)
    score = score_resume(sections, keywords_found, grammar_issues, word_count, readability)

    missing_sections = ['summary', 'education', 'experience', 'skills', 'projects', 'contact']
    missing_sections = [m for m in missing_sections if m not in sections]

    return {
        'sections': sections,
        'missing_sections': missing_sections,
        'keywords_found': keywords_found,
        'word_count': word_count,
        'grammar_issues': grammar_issues,
        'readability': readability,
        'score': score
    }

# Streamlit UI
st.title("📄 AI Resume Scanner")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner('Analyzing your resume...'):
        text = extract_text_from_pdf(uploaded_file)
        result = analyze_resume(text)

    st.subheader("📋 Resume Analysis Results")
    st.markdown(f"**Sections present:** {', '.join(result['sections'])}")
    st.markdown(f"**Missing sections:** {', '.join(result['missing_sections'])}")
    st.markdown(f"**Keywords found:** {', '.join(result['keywords_found'])}")
    st.markdown(f"**Word count:** {result['word_count']}")
    st.markdown(f"**Grammar issues detected:** {result['grammar_issues']}")
    st.markdown(f"**Readability score (Flesch):** {result['readability']:.2f}")
    st.markdown(f"**Overall score:** {result['score']} / 10")

    if result['score'] >= 7:
        st.success("✅ Your resume looks good!")
    elif result['score'] >= 4:
        st.warning("⚠️ Your resume is okay but could use improvements.")
    else:
        st.error("❌ Your resume needs serious work.")
