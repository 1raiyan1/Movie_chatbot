Movie Chatbot
Hey there! Welcome to the Movie Chatbot project. This little bot lets you chat with your favorite movie characters, using real dialogues from movie scripts. If it finds a matching line from the script, it'll reply with that. If not, it’ll use some AI magic to come up with a response.

What This Does
Finds real movie quotes: When you ask a character something, it tries to find a matching line from the movie script.
AI fallback: If it can't find an exact match, it uses AI to generate a response.
Flask-powered API: The chatbot is built on Flask, so you can interact with it via a simple API.
What You’ll Need
Before you dive in, you’ll need a few things set up on your machine:

Python 3.x (duh)
SQLite (it comes with Python)
Flask (to power the API)
Requests (for testing the API)
How to Get It Running
1. Clone the Repo
First things first, clone the project to your local machine:

bash
Copy
Edit
git clone https://github.com/1raiyan1/Movie_chatbot.git
cd Movie_chatbot
2. Install Dependencies
Create a virtual environment and install the necessary packages:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
3. Prepare the Database
Now, you’ll need to parse the movie script into a database. If you have the script (like iron_man_script.txt), place it in the project’s root folder and run this command:

bash
Copy
Edit
python parse_script.py
This will go through the entire script and store the dialogues for each character in a database.

4. Start the Server
Now, it's time to fire up the server:

bash
Copy
Edit
python app.py
Your chatbot will be up and running at http://127.0.0.1:5000.

How to Talk to the Bot
POST /chat
What Does It Do?
You send it the name of a character and what you want to say, and it’ll check if the character has a matching line in the movie script. If it does, it replies with that. If not, it’ll make up a response using some AI.

Example Request
json
Copy
Edit
{
  "character": "Iron Man",
  "user_message": "I am Iron Man"
}
Example Response
If it finds the line in the script:

json
Copy
Edit
{
  "character": "Iron Man",
  "response": "Iron Man says: I am Iron Man"
}
If there’s no match, it’ll try something like:

json
Copy
Edit
{
  "character": "Iron Man",
  "response": "Iron Man says: I am the one who builds the future!"
}
Testing the API
You can test the chatbot using curl or Postman.

Here’s how you’d do it with curl:

bash
Copy
Edit
curl -X POST "http://127.0.0.1:5000/chat" -H "Content-Type: application/json" -d '{"character": "Iron Man", "user_message": "I am Iron Man"}'
What’s Next?
Multi-character chats: Right now, it’s focused on one character at a time. Imagine what it could do with multiple characters!
Improved AI: We can make the AI even better by using more advanced models to handle when there’s no match in the script.
More movie scripts: This is just the start—let’s add more scripts for more characters.
License
Feel free to use and modify this project! It’s open-source under the MIT License. Check out the LICENSE file for more details.

