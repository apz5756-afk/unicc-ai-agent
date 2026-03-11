import streamlit as st

from agent import SYSTEM_PROMPT, create_client, get_reply, load_config


st.set_page_config(page_title="AIna AI Agent", page_icon="AI", layout="centered")

st.title("AIna AI Agent")
st.caption("A simple web-based AI assistant powered by OpenAI.")

try:
    _, model = load_config()
    client = create_client()
except SystemExit as exc:
    st.error(str(exc))
    st.stop()

if "history" not in st.session_state:
    st.session_state.history = [{"role": "system", "content": SYSTEM_PROMPT}]

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask AIna something")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = get_reply(client, model, st.session_state.history, prompt)
        st.markdown(answer)

    st.session_state.history.append({"role": "user", "content": prompt})
    st.session_state.history.append({"role": "assistant", "content": answer})
    st.session_state.messages.append({"role": "assistant", "content": answer})

if st.button("Clear chat"):
    st.session_state.history = [{"role": "system", "content": SYSTEM_PROMPT}]
    st.session_state.messages = []
    st.rerun()
