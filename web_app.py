import streamlit as st
from modules import read_todo, write_todo

todos = read_todo()
st.title("TODO APP")


def add_todo():
    todo_to_add = st.session_state["input"]
    if todo_to_add != "":
        todos.append(todo_to_add+"\n")
        write_todo(todos)
    
for index, item in enumerate(todos):
    check_box = st.checkbox(item, key=item)
    if check_box:
        todos.pop(index)
        write_todo(todos)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="Type here a todo:", placeholder="Add a todo...",
                on_change=add_todo, key="input")