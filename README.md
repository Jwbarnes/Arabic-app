# 🕌 Arabic Semantic Engine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jwbarnes-arabic-app-app-jhtzan.streamlit.app/)

**A Python-based linguistic analysis tool designed to deconstruct Modern Standard Arabic (MSA) from first principles.**

## 📖 Overview
This application acts as a "Prism" for Arabic text. Instead of simple translation, it fractures phrases into their elemental components to aid students in understanding the *logic* of the language. It was built to bridge the gap between rote memorization and morphological understanding.

## 🚀 Key Features

* **Dual-Stream Audio Engine:**
    * Generates native-pronunciation audio (using `gTTS`).
    * Includes a "Slow Mode" specifically designed for learners to distinguish phonemes.
* **Morphological Analysis:**
    * Strips diacritics (Tashkeel) for accurate root extraction.
    * Identifies the 3-letter Root (e.g., K-T-B) regardless of conjugation.
* **Pattern Detective:**
    * Automatically detects grammatical patterns (Wazn) such as:
        * The "Mim" prefix (Place/Tool).
        * The "Ist" prefix (Seeking/Requesting).
        * The "Ta-Marbuta" suffix (Noun/Unit).
* **Semantic Field Mapping:**
    * Cross-references roots with English concepts to build vocabulary associations.

## 🛠️ Tech Stack

* **Python 3.9+**
* **Streamlit:** For the web interface and mobile responsiveness.
* **NLTK (Natural Language Toolkit):** For tokenization and stemming (ISRI Stemmer).
* **Deep Translator:** For context-aware translation.
* **RegEx:** For advanced string manipulation and vowel filtering.

## 💻 How to Run Locally

If you want to run this on your own machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[YOUR-USERNAME]/arabic-app.git
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

## 📸 Screenshots

*(You can upload a screenshot of your app here later!)*

---
*Built by [Jeff Barnes]*
