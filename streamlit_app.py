import streamlit as st
import requests

# Function to call the GPT API
def generate_text(prompt):
    url = "YOUR_GPT_API_ENDPOINT"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100  # Adjust as needed
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()["choices"][0]["text"].strip()

# Streamlit UI
def main():
    st.title("GPT Text Generation")

    # User input
    prompt = st.text_area("Enter your prompt:", "")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating..."):
                generated_text = generate_text(prompt)
                st.success("Text generated successfully!")
                st.write(generated_text)
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
