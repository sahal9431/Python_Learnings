import streamlit as st
from D_01.to_do import functions

todos = functions.get_todos()
st.set_page_config(page_icon="✅", layout="wide")
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
todos = functions.get_todos()
st.title("To-Do List Web App")
st.subheader("Manage your tasks easily")
st.write("This is a simple to-do list application built with Streamlit.")
st.text_input(label="Add a new to-do:", 
              placeholder="Enter a new task here...", 
              key="new_todo", 
              on_change=add_todo)
for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
