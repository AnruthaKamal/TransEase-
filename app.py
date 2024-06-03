import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

def predict(test_sentence):
    model_name = './fine-tuned-marianmt-en-hi'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model_test = MarianMTModel.from_pretrained(model_name)
    
    input = tokenizer(test_sentence, return_tensors="pt", padding=True, truncation=True, max_length=128)
    translated_token = model_test.generate(**input)
    translated_sentence = [tokenizer.decode(t, skip_special_tokens=True) for t in translated_token]
    
    return translated_sentence[0]

def main():
    st.set_page_config(page_title="TransEase", page_icon=":earth_asia:", layout="wide")
    
    # Introduction section
    st.title("Welcome to TransEase")
    st.write("""
        Hi there! I'm TransEase, your friendly translation companion.
        I help you translate English text into Hindi effortlessly.
        Whether you're learning Hindi, communicating with friends, or exploring a new language,
        I'm here to assist you. Just type in your English text and let me handle the rest.
    """)
    
    # Translation section
    st.header("Translate English to Hindi")
    user_input = st.text_area("Enter English Text:")
    
    if st.button("Translate"):
        if user_input.strip():
            translated_text = predict([user_input])
            st.success(f"Translated Text: {translated_text}")
        else:
            st.warning("Please enter text to translate.")

if __name__ == "__main__":
    main()
