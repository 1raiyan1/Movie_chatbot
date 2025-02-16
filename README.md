Movie Chatbot

Overview

Movie Chatbot is an AI-powered conversational agent that helps users find movie recommendations, details, and insights through a chat-based interface. It leverages WebSockets for real-time communication and a database for storing chat history.

Features

Real-time WebSocket Communication: Provides seamless interaction between users and the chatbot.

Movie Search & Recommendations: Users can ask for movie suggestions based on genres, actors, or mood.

Database Integration: Stores chat history for improved user experience.

FastAPI Backend: The backend is built using FastAPI for high-performance responses.

Deployment-Ready: Can be deployed on cloud platforms like AWS, Railway, or any other hosting provider.

Installation

Prerequisites

Python 3.10+

Git

Virtual Environment (optional but recommended)

Setup

Clone the repository:

git clone https://github.com/1raiyan1/Movie_chatbot.git

Navigate to the project directory:

cd Movie_chatbot

Install dependencies:

pip install -r requirements.txt

Run the server:

python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Usage

Open test.html in a browser to interact with the chatbot.

Send messages, and the bot will respond with movie recommendations and details.

Deployment

To deploy on AWS or any cloud platform:

Set up a virtual machine or container service.

Install dependencies as mentioned above.

Run the server and configure the domain for public access.

Contribution

Feel free to contribute by opening issues or pull requests!

License

This project is open-source under the MIT License.
