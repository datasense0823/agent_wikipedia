import streamlit as st
from agents import lookup  # Replace 'your_module' with the actual module name

# Set Streamlit app title and layout
st.set_page_config(page_title="QueryMaster 360°", page_icon="🧠", layout="wide")

# Fancy App Header
st.markdown(
    """
    <div style="background-color: #4CAF50; padding: 20px; border-radius: 10px; text-align: center;">
        <h1 style="color: white;">🧠 QueryMaster 360°</h1>
        <h4 style="color: white;">🌟 Your AI-powered assistant to solve data-driven questions 🌟</h4>
    </div>
    """,
    unsafe_allow_html=True,
)

# Question Input Section
st.markdown("### 🔍 **What’s Your Question?**")
user_question = st.text_input(
    "Ask your query below 👇",
    placeholder="E.g., What is the population of Canada? Multiply by 2.",
)

# Button to Submit
if st.button("Get Answer 💡"):
    if user_question.strip():
        with st.spinner("Thinking... 🤔"):
            try:
                # Call your lookup function
                agent_response = lookup(user_question)

                # Extract the final answer
                final_answer = agent_response.get("output", "No final answer available.")

                # Display Final Answer
                st.markdown(
                    f"""
                    <div style="background-color: #FFD700; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px;">
                        <h2 style="color: black;">✨ Final Answer ✨</h2>
                        <p style="font-size: 18px; color: #333;">{final_answer}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            except Exception as e:
                st.error(f"❌ Oops! Something went wrong: {e}")
    else:
        st.warning("⚠️ Please enter a question to get started!")

# Footer with Branding
st.markdown(
    """
    <hr>
    <div style="text-align: center; color: gray; margin-top: 20px;">
        <p>✨ Built with ❤️ by Data Sense | Powered by  OpenAI ✨</p>
        <p style="font-size: 12px;">🚀 Empowering smarter data-driven decisions</p>
    </div>
    """,
    unsafe_allow_html=True,
)
