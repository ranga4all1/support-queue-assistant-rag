import streamlit as st
import uuid
from rag import rag  # Assuming you have this function

# import db  # Assuming this is your database module

# Streamlit UI
st.title("Support Queue Assistant")

# Use a form to capture "Enter" key submission
with st.form(key="question_form", clear_on_submit=True):
    user_question = st.text_input("Enter your question", key="question_input")
    submit_button = st.form_submit_button(label="Submit Question")

if submit_button:
    if user_question:
        # Generate a conversation ID
        conversation_id = str(uuid.uuid4())

        # Get the answer from the rag function
        answer_data = rag(user_question)
        answer = answer_data["answer"]

        # Display the question and answer in the Streamlit UI
        st.write(f"**Question**: {user_question}")
        st.write(f"**Answer**: {answer}")

        # Save the conversation to the database
        # db.save_conversation(
        #     conversation_id=conversation_id,
        #     question=user_question,
        #     answer_data=answer_data,
        # )

        # Store the conversation ID for feedback
        st.session_state.conversation_id = conversation_id
    else:
        st.write("Please enter a valid question.")

# Feedback section
if "conversation_id" in st.session_state:
    st.subheader("Provide Feedback")
    feedback = st.radio("Was the answer helpful?", ("Yes", "No"))

    if st.button("Submit Feedback"):
        feedback_value = 1 if feedback == "Yes" else -1

        # Save the feedback to the database
        db.save_feedback(
            conversation_id=st.session_state.conversation_id,
            feedback=feedback_value,
        )

        st.write(
            f"Feedback submitted for conversation {st.session_state.conversation_id}"
        )
