🤖 Mini Tool-Using AI Agent

A beginner-to-intermediate Agentic AI project built with Python, Ollama, and Qwen3:4B.

This project demonstrates how an LLM can decide when to use external tools, execute those tools through Python, observe their results, and continue reasoning until it can provide a final response.

🚀 Project Overview

Unlike a basic chatbot that only generates text, this project gives the LLM access to real Python functions and an external weather API.

The agent can:

* Perform mathematical calculations
* Retrieve current weather information for a city
* Decide which tool to use based on the user’s request
* Execute multiple tool calls when required
* Pass tool results back to the LLM
* Continue the agent loop until a final answer can be generated
* Maintain conversation history during the session

🧠 Agent Workflow

User Request
     │
     ▼
   Qwen3:4B
     │
     ▼
Does the request require a tool?
     │
 ┌───┴────┐
 │        │
Yes       No
 │        │
 ▼        ▼
Tool    Final
Call    Answer
 │
 ▼
Python executes tool
 │
 ▼
Tool Result
 │
 ▼
Back to LLM
 │
 ▼
Another Tool / Final Answer

🛠️ Available Tools

add(a, b)

Adds two numbers.

Example:

User: What is 25 + 15?
Agent: 40

multiply(a, b)

Multiplies two numbers.

Example:

User: What is 25 × 8?
Agent: 200

get_weather(city)

Retrieves current weather information using the Open-Meteo API.

The tool converts a city name into geographic coordinates and then retrieves current weather data.

Example:

User: What's the weather in Mumbai?
Agent: The current temperature in Mumbai is ...

🔄 Multi-Tool Example

The agent can handle requests that require more than one action.

Example:

User:
What's the weather in Mumbai and what is 25 multiplied by 8?
Agent:
→ Calls get_weather("Mumbai")
→ Calls multiply(25, 8)
→ Receives both tool results
→ Generates the final response

This demonstrates the basic observe → act → observe → act → respond pattern used in tool-using agents.

🧰 Tech Stack

* Python
* Ollama
* Qwen3:4B
* Open-Meteo API
* Requests

📁 Project Structure

Mini-Agent/
│
├── agent.py
├── README.md
└── requirements.txt

⚙️ Installation

1. Clone the repository

git clone https://github.com/anmolahlawat/Mini-Agent.git
cd Mini-Agent

2. Install Python dependencies

pip install -r requirements.txt

3. Install Ollama

Install Ollama and make sure it is running on your machine.

Then download the Qwen model:

ollama pull qwen3:4b

4. Run the agent

python agent.py

Type:

exit

to stop the agent.

📦 Requirements

Example requirements.txt:

ollama
requests

🎯 What I Learned

This project helped me understand the fundamental architecture behind tool-using AI agents:

1. How an LLM decides whether a tool is required
2. How tool calls are represented
3. How Python functions can be connected to an LLM
4. How tool arguments are passed from the model to Python
5. How tool results are returned to the model
6. How an iterative agent loop works
7. How multiple tools can be combined in a single workflow
8. Why conversation/message history is important for agent behavior

🔮 Future Improvements

This project is the foundation for more advanced Agentic AI systems.

Planned improvements include:

* Better error handling
* More tools
* Persistent memory
* RAG integration
* API-based tools
* More complex multi-step workflows
* Improved tool selection
* Agent + RAG architecture
* Interactive chat interface
* More advanced autonomous agent workflows

👨‍💻 Author

Anmol Ahlawat

B.Tech — Artificial Intelligence & Machine Learning

GitHub: https://github.com/anmolahlawat

⸻

⭐ This project is part of my ongoing journey from Machine Learning → Deep Learning → Generative AI → Agentic AI.