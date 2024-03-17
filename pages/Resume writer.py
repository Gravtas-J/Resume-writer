import streamlit as st
import openai
import os


userprofile=os.path.join('Memories', 'user_profile.txt')
r_writer = os.path.join('system prompts', 'resume writer')

def resume_writer():
    # Prepare the data to be sent to the profiling module
    update_data = [{'role': 'system', 'content': r_writer}, {'role': 'user', 'content': st.session_state.get('chat_log', '')}]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0125", messages=update_data, temperature=0, max_tokens=4000)
    User_profile_updated = response['choices'][0]['message']['content']

    # Save the updated data to the user profile file
    with open(userprofile, "w") as file:
        file.write(User_profile_updated)