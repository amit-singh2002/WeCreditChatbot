import streamlit as st
import openai  # Or your preferred LLM library

# Set your OpenAI API key (or equivalent) - SECURELY, ideally not directly in code
openai.api_key = st.secrets["OPENAI_API_KEY"] # Best practice for API keys

st.title("WeCredit Chatbot")import streamlit as st
import openai
import os

# Streamlit App Title
st.title("WeCredit Dynamic FinTech Chatbot 💬")
st.write("Ask me anything about loans, credit reports, interest rates, CIBIL scores, and more!")

# OpenAI API Key Setup
if "OPENAI_API_KEY" in st.secrets:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
elif os.getenv("OPENAI_API_KEY"):
    openai.api_key = os.getenv("OPENAI_API_KEY")
else:
    st.error("🚨 OpenAI API Key not found! Please add it to Streamlit secrets or set it as an environment variable.")

# User Input
user_input = st.text_input("You:", "Type your financial question here...")

# Dynamic Knowledge-Based and LLM Response
def generate_response(user_query):
    knowledge_base = {
        "loans": "Loans can be Personal, Home, Auto, Education, or Business. Eligibility depends on age (21–60), income stability, and credit score. Required documents: ID proof, address proof, income proof, and bank statements.",
        "interest rates": "Interest rates can be fixed or floating. Simple Interest = (P * R * T) / 100. Factors influencing rates include RBI policies, credit score, and market trends.",
        "credit bureaus": "Major Indian credit bureaus: CIBIL, Experian, Equifax, and CRIF High Mark. These agencies track credit history, affecting loan approvals.",
        "credit reports": "Credit reports detail personal info, credit accounts, payment history, and public records. You can request one free report annually from official credit bureaus.",
        "cibil score": "CIBIL Score ranges from 300–900, with 750+ considered good. Factors include payment history (35%), credit utilization (30%), credit history length (15%), credit mix (10%), and new credit inquiries (10%)."
    }

    # Check knowledge base first
    for key, value in knowledge_base.items():
        if key in user_query.lower():
            return value

    # Use OpenAI LLM if not in knowledge base
    prompt = f"""
    You are a professional financial advisor chatbot for WeCredit.
    Answer the user's question with accurate financial information about loans, interest rates, credit bureaus, credit reports, and CIBIL scores.

    User: {user_query}
    Bot:
    """

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=250,
            temperature=0.5
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Handle User Query
if user_input:
    response = generate_response(user_input)
    st.write(f"**WeCredit Bot:** {response}")

# Footer
st.markdown("---")
st.markdown("Created for WeCredit by Amit Kumar Singh")


# ... (Your chatbot logic here) ...

def get_chatbot_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Or your chosen LLM model
        prompt=f"WeCredit Chatbot:\n{user_input}",
        max_tokens=150,
    )
    return response.choices[0].text.strip()


user_input = st.text_input("Ask a question about loans, credit, or interest rates:")

if user_input:
    response = get_chatbot_response(user_input)
    st.write(response)

# ... (Rest of your Streamlit app code) ...
