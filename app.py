import streamlit as st

# Keyword translations
keywords = {
    "en": ["General", "Politics", "Sports", "Entertainment", "Technology", "Health", "Fashion", "Science"],
    "hi": ["सामान्य", "राजनीति", "खेल", "मनोरंजन", "प्रौद्योगिकी", "स्वास्थ्य", "फैशन", "विज्ञान"],
    "te": ["సాధారణం", "రాజకీయాలు", "క్రీడలు", "వినోదం", "సాంకేతికత", "ఆరోగ్యం", "ఫ్యాషన్", "సైన్స్"]
}
years = ["1950", "1960", "1970", "1980", "1990", "2000"]

st.set_page_config(page_title="📰 Retro Newspaper Explorer", layout="centered")

st.title("📰 Retro Newspaper Explorer")

# Sidebar for input
st.sidebar.header("Explore Newspaper")
language = st.sidebar.selectbox("Language", options=["en", "hi", "te"], format_func=lambda x: {"en":"English","hi":"Hindi","te":"Telugu"}[x])
year = st.sidebar.selectbox("Year", options=years)
keyword = st.sidebar.selectbox("Keyword", options=keywords[language])
description = st.sidebar.text_area("Article Description", placeholder="Enter your article description...")
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Default description if not provided
if not description:
    if language == "en":
        description = f"This is a featured article from the year {year} focusing on {keyword}. Discover what was happening in that year."
    elif language == "hi":
        description = f"{year} का यह विशेष लेख {keyword} पर केंद्रित है। जानिए उस साल क्या हो रहा था।"
    elif language == "te":
        description = f"{year} లో {keyword} పై ఇది ఒక ప్రత్యేక వ్యాసం. ఆ సంవత్సరం ఏమి జరుగుతుందో తెలుసుకోండి."

# Output "newspaper"
st.markdown(
    f"""
    <div style='background:#fff8dc; border:2px solid #333; border-radius:12px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.2);'>
        <div style='font-size:28px; font-weight:bold; color:darkred; text-align:center;'>📰 {keyword} News ({year})</div>
        <div style='font-size:16px; color:navy; margin:10px 0;'>{'Staff Reporter' if language=='en' else 'स्टाफ रिपोर्टर' if language=='hi' else 'స్టాఫ్ రిపోర్టర్'}</div>
        <div style='border:2px solid black; display:inline-block; padding:5px 15px; margin:15px 0; font-weight:bold;'>🗞 {keyword}</div>
        <div style='font-size:18px; text-align:justify; margin:20px 0;'>{description}</div>
    </div>
    """,
    unsafe_allow_html=True
)

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)