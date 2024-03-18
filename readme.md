## Introduction

This project consists of two main components: a Chatbot and a Resume Writer, both designed to leverage the power of OpenAI's GPT models. The Chatbot facilitates interactive conversations, while the Resume Writer generates custom resumes based on user inputs and job listings. This document provides an overview of the project, including its structure, functionalities, and setup instructions.

## Structure

The project is divided into two primary sections:

1. **Chatbot**: This section employs Streamlit for UI interactions and OpenAI's GPT model to generate responses. It includes functionalities for simulating real-time message exchanges, updating user profiles, and maintaining a chat log.

2. **Resume Writer**: This component also uses Streamlit for file uploads and interactions. It utilizes OpenAI's GPT model to create personalized resumes based on the user's profile and uploaded job listings.

## Features

### Chatbot

- Real-time messaging simulation with delay.
- Persistent chat logs.
- User profile updates based on chat interactions.

### Resume Writer

- File upload for job listings.
- Custom resume generation based on user profile and job listing.
- Generated resumes are saved for user access.

## Installation

1. **Environment Setup**: Ensure Python is installed on your system.

2. **Dependencies Installation**: Install required packages using the following command:

   ```
   pip install streamlit openai python-dotenv
   ```

3. **API Key Configuration**: Sign up for OpenAI and obtain an API key. Create a `.env` file in your project directory and add your API key as follows:

   ```
   OPENAI_API_KEY='Your_OpenAI_API_Key_Here'
   ```


## Usage

- **Chatbot**:
  
  Launch the application with Streamlit using:

  ```
  streamlit run your_script_name.py
  ```

  Interact with the Chatbot via the Streamlit interface.

- **Resume Writer**:

  After launching the application, use the file uploader to provide a job listing. The system will generate a customized resume based on the provided information and your profile.

## Contributing

Contributions to this project are welcome. Please ensure to follow the project's coding standards and submit pull requests for any new features or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
