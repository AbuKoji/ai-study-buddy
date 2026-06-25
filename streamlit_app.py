import streamlit as st
from openai import OpenAI

st.title("📚 AI Study Buddy")

api_key = st.text_input("OpenAI API Key", type="password")

topic = st.text_area(
    "What do you want to study?",
    placeholder="Example: Berlin Conference"
)

if st.button("Study"):
    if not api_key:
        st.error("Please enter your OpenAI API key.")
    elif not topic:
        st.error("Please enter a topic.")
    else:
        client = OpenAI(api_key=api_key)

        prompt = f"""
You are a Study Buddy AI.

Topic: {topic}

Provide:
1. Simple explanation
2. Short summary
3. Three quiz questions
4. Three flashcards
5. One study tip
"""

        response = client.chat.completions.create(
model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        st.write(response.choices[0].message.content)
