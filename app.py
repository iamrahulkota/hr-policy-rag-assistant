"""Streamlit chat UI for the HR policy assistant. Run with: streamlit run app.py"""

import streamlit as st

from hr_assistant.pipeline import ask, build_hr_assistant

st.set_page_config(page_title="HR Policy Assistant", page_icon="💼", layout="centered")

WELCOME = "Hi! I'm your HR assistant. Ask me anything about company policies."


@st.cache_resource(show_spinner="Building the HR policy assistant...")
def get_agent():
    """Build the RAG agent once and reuse it across reruns and sessions."""
    return build_hr_assistant()


def init_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []


def render_sidebar():
    with st.sidebar:
        st.header("💼 HR Assistant")
        st.caption(
            "Answers are retrieved from the company HR policy document. "
            "If the policy doesn't cover it, the assistant will say so."
        )

        st.divider()
        if st.button("🗑️ Clear conversation", use_container_width=True):
            st.session_state.messages = []
            st.rerun()


def main():
    init_state()
    render_sidebar()

    st.title("HR Policy Assistant")

    try:
        agent = get_agent()
    except Exception as e:
        st.error(f"Could not start the assistant: {e}")
        st.stop()

    # Replay the conversation so far
    with st.chat_message("assistant"):
        st.markdown(WELCOME)
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if question := st.chat_input("Ask a question about HR policy..."):
        history = list(st.session_state.messages)
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Searching HR policy..."):
                try:
                    answer = ask(agent, question, history)
                except Exception as e:
                    answer = f"⚠️ Sorry, something went wrong: {e}"
            st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})


main()
