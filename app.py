import streamlit as st
import nltk
from nltk.stem.isri import ISRIStemmer
from deep_translator import GoogleTranslator
from gtts import gTTS
import re

import streamlit as st
import nltk
from nltk.stem.isri import ISRIStemmer
from deep_translator import GoogleTranslator
from gtts import gTTS
import re
import os

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Arabic Etymologist", page_icon="🕌")

# --- NLTK DATA FIX ---
# We point NLTK to a local folder to avoid permission errors
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)
nltk.data.path.append(nltk_data_dir)

# Download 'punkt' specifically to this folder
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=nltk_data_dir)
    nltk.download('punkt_tab', download_dir=nltk_data_dir) # Just in case

# ... The rest of your code (Section 2: The Logic) continues here ...

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Arabic Etymologist", page_icon="🕌")

# Download NLTK data quietly
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# --- 2. THE LOGIC (The Brains) ---
# Initialize tools once (cached) to speed up the app
@st.cache_resource
def load_tools():
    stemmer = ISRIStemmer()
    translator = GoogleTranslator(source='auto', target='en')
    return stemmer, translator

stemmer, translator = load_tools()

decoder_ring = {
    'ا': 'A', 'أ': 'A', 'إ': 'A', 'آ': 'A', 'ب': 'B', 'ت': 'T', 'ث': 'Th',
    'ج': 'J', 'ح': 'H', 'خ': 'Kh', 'د': 'D', 'ذ': 'Dh', 'ر': 'R', 'ز': 'Z',
    'س': 'S', 'ش': 'Sh', 'ص': 'S', 'ض': 'D', 'ط': 'T', 'ظ': 'Z', 'ع': '3',
    'غ': 'Gh', 'ف': 'F', 'ق': 'Q', 'ك': 'K', 'ل': 'L', 'م': 'M', 'ن': 'N',
    'ه': 'H', 'و': 'W', 'ي': 'Y', 'ة': 'ah', 'ى': 'a'
}

def get_english_root(root):
    return "-".join([decoder_ring.get(L, L) for L in root])

def strip_tashkeel(text):
    noise = re.compile(""" ّ | َ | ً | ُ | ٌ | ِ | ٍ | ْ | ـ """, re.VERBOSE)
    return re.sub(noise, '', text)

def pattern_detective(word):
    clues = []
    if word.startswith('م') and len(word) > 3:
        clues.append("Starts with 'Mim' (م) -> Often a Place, Tool, or Doer.")
    if word.startswith('است'):
        clues.append("Starts with 'Ist-' (است) -> Often means 'Seeking'.")
    if word.endswith('ة'):
        clues.append("Ends with 'Ta-Marbuta' (ة) -> Likely a Noun/Unit.")
    if word.startswith('ي') and len(word) > 3:
        clues.append("Starts with 'Ya' (ي) -> Likely Present Tense.")
    return clues

# --- 3. THE INTERFACE (The Skin) ---
st.title("🕌 Arabic Root Explorer")
st.markdown("Enter a Modern Standard Arabic phrase below.")

# Input Box
text_input = st.text_input("Arabic Phrase:", placeholder="Example: أَحُبُّ الْقَهْوَةَ")

if text_input:
    # A. Translate Full Context
    clean_text = strip_tashkeel(text_input)
    full_translation = translator.translate(clean_text)
    
    st.success(f"**Meaning:** {full_translation}")
    
    # B. Audio Section
    st.subheader("🔊 Audio")
    col1, col2 = st.columns(2)
    
    with col1:
        st.caption("Normal Speed")
        tts_fast = gTTS(text_input, lang='ar', slow=False)
        tts_fast.save("fast.mp3")
        st.audio("fast.mp3")
        
    with col2:
        st.caption("Slow Speed (Study)")
        tts_slow = gTTS(text_input, lang='ar', slow=True)
        tts_slow.save("slow.mp3")
        st.audio("slow.mp3")

    # C. Analysis Section
    st.divider()
    st.subheader("🔍 Root Breakdown")
    
    words = clean_text.split()
    
    for w in words:
        root = stemmer.stem(w)
        phonetic = get_english_root(root)
        word_meaning = translator.translate(w)
        root_concept = translator.translate(root)
        clues = pattern_detective(w)

        # Create a visually distinct card for each word
        with st.container():
            st.markdown(f"### **{w}** ({word_meaning})")
            st.markdown(f"**Root:** :red[{root}] [{phonetic}] → :blue[{root_concept}]")
            
            for clue in clues:
                st.warning(f"🕵️ {clue}")
            st.divider()
