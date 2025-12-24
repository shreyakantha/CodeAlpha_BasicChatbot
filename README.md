# 🤖 Basic Chatbot (Rule-Based)
This project implements a simple rule-based chatbot using Python. The chatbot interacts with users through predefined text inputs such as greetings, common questions, and exit commands, and responds with fixed, appropriate replies.
The chatbot runs in a continuous loop, processes user input from the console, and demonstrates basic conversational flow using conditional logic. It is designed as a beginner-friendly project to practice core Python programming concepts.

## 🎯 Goal
Build a basic rule-based chatbot that accepts user input like greetings and simple questions, responds with predefined messages, and exits gracefully when the user types a termination command.

## ⭐ Features
- Accepts real-time user input from the console
- Responds to predefined inputs such as greetings and common questions
- Handles variations in user input by normalizing text and removing punctuation
- Maintains a simple conversational flow using a follow-up response
- Runs continuously until the user types bye
- Beginner-friendly and easy to extend

## 🧠 Key Concepts Used
- Functions
- if–elif–else conditions
- Loops
- Dictionaries
- String handling
- Console input/output

## 🛠 Tech Stack
**Language :** Python

**Libraries Used :** string (for punctuation handling)

## 📂 Project Structure
```Bash
CodeAlpha_BasicChatbot/
│
├── BasicChatbot.py     # Main Python chatbot script
├── README.md           # Project documentation
```
## 📥 Installation
Clone the repository using Git :
```Bash
    git clone https://github.com/shreyakantha/CodeAlpha_BasicChatbot
cd CodeAlpha_BasicChatbot
```
    
## 🖥 Run Locally
Navigate to the location of your file :
```bash
  cd CodeAlpha_BasicChatbot
```
Run the script :
```bash
 python BasicChatbot.py
```

## 🎥 Demo
*A short demo video showing the chatbot interaction in the console. The demo covers user greetings, conversational responses, follow-up replies, and graceful termination using the exit command.*

[ ▶ click here to view the demo video of the basic chatbot ](https://github.com/shreyakantha/CodeAlpha_BasicChatbot/releases/tag/v1.0)

## 📝  Usage/Example
Below is a sample interaction with the chatbot :
```bash
Bot: Hello! I'm a simple chatbot. Type 'bye' to exit.
You: Hello
Bot: Hi!
You: How are you?
Bot: I'm fine, thanks! How are you?
You: I am good
Bot: Glad to hear that!
You: Bye
Bot: Goodbye
```

## 🚀 Deployment
This is a console-based Python script and does not require deployment.
It can be executed on any system with Python installed.

## ⚙ Optimizations
- Uses input normalization (lowercasing and punctuation removal) for better matching
- Dictionary-based responses for cleaner and scalable logic
- Simple state tracking to support follow-up conversation

## 📚 Lessons Learned
- Designing rule-based conversational logic
- Handling user input variations
- Structuring interactive Python scripts
- Improving readability and maintainability using dictionaries

## 🔮 Future Improvements
- Add partial input matching for more natural conversation
- Expand response coverage for more questions
- Add basic conversation history
- Convert the chatbot into a GUI or web-based interface

## 📄 Documentation
The code is structured for clarity and readability. Each logical block is easy to understand, making the project suitable for beginners learning Python control flow and user interaction.

## 👤 Author
- [@shreyakantha](https://github.com/shreyakantha) 

## 🙌 Acknowledgements
- CodeAlpha Internship Program for providing the task
- Python official documentation
- Online Python learning resources for beginner-friendly guidance

## 📜 License
This project is open for educational and personal use.
Feel free to modify, improve, and expand it as needed.

## 💬 Feedback
If you have any feedback or suggestions, feel free to reach out at 📧 shreyakantha348@gmail.com

## ❓ FAQ
#### Q1. Is this chatbot AI-based?
**Answer.** No. It is a simple rule-based chatbot using predefined logic.
#### Q2. Can it understand free-form sentences?
**Answer.** No. It responds only to predefined inputs.
#### Q3. How does the chatbot exit?
**Answer.** By typing 'bye'.

## 🧩 Appendix
This project was completed as ***The fourth task Basic Chatbot*** under the **CodeAlpha Python Programming Internship**, with a focus on strengthening core Python fundamentals and rule-based conversational logic.

## 📌 Related Projects
*The following projects were completed as part of the same **CodeAlpha internship** program and focus on strengthening core Python programming concepts.*
- 🔗 [Hangman Game – Python fundamentals and control flow](https://github.com/shreyakantha/CodeAlpha_HangmanGame)
- 🔗 [Stock Portfolio Tracker – Data processing using Python](https://github.com/shreyakantha/CodeAlpha_StockPortfolioTracker)
- 🔗 [Email Extraction Automation – File handling and regular expressions in Python](https://github.com/shreyakantha/CodeAlpha_EmailExtractor)