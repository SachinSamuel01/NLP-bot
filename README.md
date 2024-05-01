# Natural Language Conversational Bot Platform

## Introduction
The Natural Language Conversational Bot Platform is a web-based interface that allows users to create custom AI-powered chatbots. This platform is versatile, supporting a wide range of fields and integrating large language models (LLM) for enhanced conversational capabilities. Users can create personalized bots, upload relevant files for RAG, and interact through both text and voice.

[![Watch the video](https://img.youtube.com/vi/jfcI9Kcjh2U/0.jpg)](https://youtu.be/jfcI9Kcjh2U)


## Features
- **Custom Chatbots:** Users can create bots tailored to their specific needs.
- **Prompt Customization:** Allows detailed instructions to fine-tune the bot for better accuracy and how the bot should interact.
- **Voice Interaction:** Supports both voice and text interactions ( using whisper and pyttsx3 ).
- **Retrieval Augmented Generation (RAG):** Users can upload files ( currently supports txt files ) to ask specific questions or queries related to it.

## Technologies
- **Python**: Main programming language.
- **Langchain**: Interfaces between the LLM and the Python project.
- **ChromaDB**: Manages vector data storage.
- **Streamlit**: For creating the web interface.
- **Whisper**: Speech-to-text model by OpenAI.
- **PyTTSx3**: Library for text-to-speech functionality.

## Getting Started

### Installation
Clone the repository and install the dependencies:
```bash
git clone <repository-url>
cd <repository-folder>
pip install -r requirements.txt
streamlit run ./main.py
```

## Project Structure
```bash
/my-project
|-- /assets             # Lottie animation files
|-- /content            # Data files for testing and example usage
|-- /lib                # Core libraries and modules
|-- /recordings         # Audio recordings
|-- /sections           # Different sections of the application
|-- /vector_database    # Storage for vector data
|-- main.py             # Main application entry point
```

### Detailed Breakdown
- assets:
  - idle.json: Animation for idle state.
  - recording.json: Animation for recording state.
  - response.json: Animation for response state.
- content:
  - autism.txt, data.txt, unsupervised_learning.txt: Example textual data for bot training and testing.
- lib:
  - Python modules for audio recording, Whisper integration, LLM management, and response handling.
- sections:
  - Modular Python scripts defining different user interface sections.

## Detailed Conversation Flow

The conversation flow of this NLP conversational bot is designed to provide a seamless interaction between the user and the AI, incorporating both text and voice inputs. Here's a step-by-step breakdown of the entire process:

### 1. **Setup**
- **Bot Configuration**: Upon accessing the platform, the user is prompted to configure the bot. This involves setting the bot's name, choosing a voice (Male or Female), and writing an initial prompt that guides the bot's behavior.
- **File Upload**: Users can upload text files (.txt format) that the bot uses to fine-tune its responses. This is particularly useful for tailoring the bot's knowledge to specific domains or topics.

### 2. **Idle State**
- **User Interface Prompt**: In this state, the bot displays a message encouraging the user to start the conversation. The message typically instructs the user to press an "Ask Question" button to begin recording their query.
- **Animations**: The platform displays an idle animation (configured in `assets/idle.json`) to indicate that the bot is waiting for input.

### 3. **Recording State**
- **Voice Recording**: Once the user initiates a conversation, the bot begins recording audio through the user's microphone. This state is visually supported by a recording animation (configured in `assets/recording.json`).
- **Silence Detection**: Recording continues until a silence of at least 3 seconds is detected, ensuring that the user has finished speaking.
- **Implementation**: The recording functionality is handled by `lib/audio_recorder.py`, which uses the PyAudio library to capture audio in real-time.

### 4. **Processing State**
- **Speech to Text**: The recorded audio is processed using OpenAI’s Whisper model to convert speech to text. This step is crucial for understanding the user's query.
- **Query Processing**: The transcribed text is then sent to the bot's language model to generate a relevant response. During this phase, the platform might also use the uploaded textual data to enhance the response accuracy.
- **Visual Feedback**: A processing animation (configured in `assets/response.json`) is shown to indicate that the bot is thinking and formulating a response.

### 5. **Response State**
- **Text to Speech**: Once the bot has formulated a response, the text is converted back into speech using the PyTTSx3 library. This allows the bot to communicate verbally with the user.
- **Voice Customization**: The response is voiced in the selected gender voice, providing a personalized touch.
- **Display and Voice**: The text response is also displayed on the screen for the user to read along while listening.

### 6. **Loop Back to Idle**
- After responding, the bot returns to the Idle State, ready to answer more questions or continue the conversation. This loop allows for sustained interaction until the user decides to end the session.

## Contributing
This is a work in progress and in the comming weeks I would be making a deployable version of the bot, move to open-source llms, and make the user experience more streamlined. Contributions to enhance or expand the platform are welcome. Please fork the repository and submit a pull request with your changes.
