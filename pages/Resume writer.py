import streamlit as st
import openai
import os

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()

# Define paths for the user profile and the directory where the resume will be written
user_profile_path = os.path.join('Memories', 'user_profile.txt')
resume_writer_path = os.path.join('system prompts', 'writer.md')  # Ensure this is a .txt file
writer = open_file (resume_writer_path)
# Check if the user has uploaded a file
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Read the content of the uploaded file
    uploaded_file_content = "<Job listing start>  \n \n" + uploaded_file.getvalue().decode("utf-8") + "<job listing end>"

    # Load the user profile content
    with open(user_profile_path, "r") as file:
        user_profile_content = "<user prifle start>" + file.read() + "<User profile end>"

    # Prepare the data to be sent to the GPT module
    # Including both the content of the uploaded file and the user profile
    prompt_data = [
        {"role": "system", "content": writer},
        {"role": "user", "content": uploaded_file_content},
        {"role": "user", "content": user_profile_content}
    ]

    # Send the data to the GPT model and get the response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=prompt_data,
        temperature=0.5, 
        max_tokens=2048
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].message["content"]

    # Define the output directory and check if it exists
    output_dir = 'GeneratedTexts'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the directory if it does not exist

    # Write the generated text to a new file within the newly ensured directory
    output_file_path = os.path.join(output_dir, 'generated_resume.txt')
    with open(output_file_path, "w") as output_file:
        output_file.write(generated_text)
    
    # Inform the user that the file has been created
    st.success("The resume has been generated and saved successfully.")
