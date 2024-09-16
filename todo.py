import streamlit as st

# Initialize session state to hold the to-do list
if 'todos' not in st.session_state:
    st.session_state.todos = []

# Title for the to-do list app
st.title("To-Do List App")

# Input field to add new task
new_task = st.text_input("Enter a task:")

# Add task to the list
if st.button("Add Task"):
    if new_task:  # Ensure the task is not empty
        st.session_state.todos.append(new_task)
    else:
        st.warning("Please enter a task.")

# Display the tasks
if st.session_state.todos:
    st.subheader("Your To-Do List:")
    for i, task in enumerate(st.session_state.todos):
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.write(f"{i+1}. {task}")
        with col2:
            # Add a "Delete" button next to each task
            if st.button("Delete", key=f"del_{i}"):
                st.session_state.todos.pop(i)
                st.experimental_rerun()

# Clear all tasks
if st.button("Clear All"):
    st.session_state.todos.clear()
