import streamlit as st
from encode import encode, generate_cover
from decode import decode

VERSION = "1.2"
MAX_MESSAGE_LENGTH = 2000

st.set_page_config(
    page_title="PhantomText",
    page_icon="◈",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Space+Grotesk:wght@400;500;600;700&display=swap');

.stApp {
    background: #080a0d;
    color: #d7dbe0;
}

.block-container {
    max-width: 1200px;
    padding-top: 45px;
    padding-bottom: 40px;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
}

p, label, .stMarkdown {
    font-family: 'Space Grotesk', sans-serif;
}

.hero {
    padding: 5px 0 30px 0;
    border-bottom: 1px solid #1b2026;
    margin-bottom: 28px;
}

.hero-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #626c76;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 48px;
    font-weight: 700;
    letter-spacing: -2px;
    color: #f1f3f5;
    margin: 0;
}

.hero-title span {
    color: #8aff80;
}

.hero-subtitle {
    font-family: 'JetBrains Mono', monospace;
    color: #737d87;
    font-size: 13px;
    margin-top: 9px;
}

.panel-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
}

.panel-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #8aff80;
    box-shadow: 0 0 10px rgba(138, 255, 128, 0.7);
}

.panel-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 1px;
    color: #e5e8eb;
}

.panel-description {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #59636d;
    margin-bottom: 15px;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    background: #0d1014;
    border: 1px solid #1c2229;
    border-radius: 8px;
    padding: 20px 22px 18px 22px;
}

div[data-testid="stTextArea"] textarea,
div[data-testid="stTextInput"] input {
    background: #080a0d !important;
    border: 1px solid #252c34 !important;
    border-radius: 6px !important;
    color: #e2e6e9 !important;
    font-family: 'JetBrains Mono', monospace !important;
}

div[data-testid="stTextArea"] textarea:focus,
div[data-testid="stTextInput"] input:focus {
    border-color: #53645a !important;
    box-shadow: 0 0 0 1px #53645a !important;
}

label {
    color: #89939d !important;
    font-size: 11px !important;
}

.stButton {
    margin-top: 8px;
}

.stButton > button {
    width: 100%;
    background: #8aff80 !important;
    color: #071008 !important;
    border: none !important;
    border-radius: 5px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 600 !important;
    letter-spacing: 1px;
    padding: 9px 20px;
    transition: 0.15s ease;
}

.stButton > button:hover {
    background: #a0ff98 !important;
    box-shadow: 0 0 18px rgba(138, 255, 128, 0.15);
}

.status {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: #8aff80;
    margin-top: 18px;
    margin-bottom: 8px;
}

.result-box {
    padding: 13px;
    background: #080a0d;
    border: 1px solid #20272e;
    border-radius: 6px;
}

.result-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    color: #59636d;
    letter-spacing: 1px;
    margin-bottom: 7px;
}

.counter {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    color: #59636d;
    text-align: right;
    margin-top: -8px;
    margin-bottom: 8px;
}

.footer {
    border-top: 1px solid #1b2026;
    margin-top: 32px;
    padding-top: 15px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    color: #454d55;
    display: flex;
    justify-content: space-between;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-tag">PHANTOM SYSTEM / 01</div>
    <div class="hero-title">PHANTOM<span>TEXT</span></div>
    <div class="hero-subtitle">beyond what meets the eye.</div>
</div>
""", unsafe_allow_html=True)

encode_col, decode_col = st.columns(2, gap="large")

with encode_col:
    with st.container(border=True):
        st.markdown("""
        <div class="panel-header">
            <div class="panel-dot"></div>
            <div class="panel-title">ENCODE</div>
        </div>
        <div class="panel-description">
            Prepare a message for transmission.
        </div>
        """, unsafe_allow_html=True)

        message = st.text_area(
            "MESSAGE",
            height=100,
            max_chars=MAX_MESSAGE_LENGTH,
            placeholder="Enter your message...",
            key="message"
        )

        st.markdown(
            f'<div class="counter">{len(message)} / {MAX_MESSAGE_LENGTH}</div>',
            unsafe_allow_html=True
        )

        key = st.text_input(
            "ACCESS KEY",
            type="password",
            placeholder="Enter an access key...",
            key="encode_key"
        )

        if st.button("ENCODE →", key="encode_button"):
            if not message:
                st.error("Message is required.")
            elif not key:
                st.error("Access key is required.")
            else:
                try:
                    cover = generate_cover()
                    result = encode(message, cover, key)

                    st.markdown(
                        '<div class="status">● READY</div>',
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        '<div class="result-box">'
                        '<div class="result-label">RESULT</div>',
                        unsafe_allow_html=True
                    )

                    st.code(result, language=None)

                    st.markdown("</div>", unsafe_allow_html=True)

                except Exception:
                    st.error("Unable to process the message.")

with decode_col:
    with st.container(border=True):
        st.markdown("""
        <div class="panel-header">
            <div class="panel-dot"></div>
            <div class="panel-title">DECODE</div>
        </div>
        <div class="panel-description">
            Recover the original message.
        </div>
        """, unsafe_allow_html=True)

        cipher = st.text_area(
            "INPUT",
            height=100,
            placeholder="Paste the text here...",
            key="cipher"
        )

        st.markdown(
            f'<div class="counter">{len(cipher)} characters</div>',
            unsafe_allow_html=True
        )

        decode_key = st.text_input(
            "ACCESS KEY",
            type="password",
            placeholder="Enter the access key...",
            key="decode_key"
        )

        if st.button("← DECODE", key="decode_button"):
            if not cipher:
                st.error("Input is required.")
            elif not decode_key:
                st.error("Access key is required.")
            else:
                try:
                    result = decode(cipher, decode_key)

                    if result is not None:
                        st.markdown(
                            '<div class="status">● VERIFIED</div>',
                            unsafe_allow_html=True
                        )

                        st.markdown(
                            '<div class="result-box">'
                            '<div class="result-label">RESULT</div>',
                            unsafe_allow_html=True
                        )

                        st.code(result, language=None)

                        st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.error("Invalid access key or input.")

                except Exception:
                    st.error("Invalid access key or input.")

st.markdown(f"""
<div class="footer">
    <span>PHANTOMTEXT // LOCAL INSTANCE</span>
    <span>v{VERSION}</span>
</div>
""", unsafe_allow_html=True)