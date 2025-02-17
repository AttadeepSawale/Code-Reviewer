import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyBi_uWNhR7V0ISrXNwJc618euVjCPhp3L4")

# Page configuration
st.set_page_config(
    page_title="AI Code Analyzer",
    page_icon="🧠",
    layout="centered"
)

# Custom Styling
st.markdown(
    """
    <style>
        body { background-color: #1E1E1E; color: #D4D4D4; }
        .stTextArea textarea {
            background-color: #252526;
            color: #D4D4D4;
            border-radius: 8px;
            border: 2px solid #4CAF50;
            font-family: 'Courier New', monospace;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 12px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover { background-color: #45A049; }
        .result-box {
            background-color: #333;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #4CAF50;
            color: #D4D4D4;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def analyze_code(code, detailed):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    Analyze this Python code and provide a {"detailed" if detailed else "concise"} review:
    ```python
    {code}
    ```
    """
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("🧠 AI Code Analyzer")
    st.write("### Paste your Python code below and get instant analysis!")
    
    code = st.text_area("🔹 Enter your Python Code:", height=200)
    detailed = st.toggle("Enable Detailed Review")
    
    if st.button("Analyze Code"):
        if code.strip():
            with st.spinner("Processing your code..."):
                result = analyze_code(code, detailed)
            
            st.markdown("### 📊 Analysis Results")
            st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter some Python code to analyze.")

if __name__ == "__main__":
    main()
