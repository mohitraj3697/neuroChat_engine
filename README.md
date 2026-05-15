# NeuroChat Engine

NeuroChat Engine is a modular AI chatbot system built to explore how real-world LLM applications are designed. It focuses on building a system that can handle context, memory, tools, and structured conversations rather than just simple question–answer interactions.

The goal of this project is to move beyond basic chatbot implementations and create something closer to a production-style intelligent system.

---

## Overview

Most chatbot projects are limited to single-turn or short conversations. This system is designed to support:

* Persistent conversations
* Multiple chat threads per user
* Streaming responses for better user experience
* Context-aware replies using memory
* External knowledge integration using RAG
* Tool usage via MCP client
* Human-in-the-loop control for sensitive actions

---

## Features

### Threaded Conversations

Supports multiple conversations per user, where each thread maintains its own context and message history.

### Persistence (SQLite)

All chats, threads, and memory are stored using SQLite, allowing the system to recover and continue conversations at any time.

### Streaming Responses

Responses are generated and returned incrementally to simulate real-time interaction.

### Resume Chat

Previous conversations are loaded from storage and used as context, allowing seamless continuation.

### Memory System

Includes both short-term and long-term memory:

* Short-term memory keeps recent interactions
* Long-term memory stores summarized context

### Retrieval-Augmented Generation (RAG)

Allows the chatbot to use external documents:

* Documents are embedded and stored in a vector database
* Relevant content is retrieved during queries

### Tool Calling (MCP Client)

Supports integration with external tools and services through a structured tool-calling mechanism.

### Human-in-the-Loop (HITL)

Enables manual intervention or approval for certain actions to improve safety and control.

---

## Architecture (High-Level)

User input is processed through a structured pipeline:

* The system identifies the active thread
* Loads previous messages and memory from the database
* Retrieves additional context using RAG if required
* Routes tool calls when needed
* Sends everything to the LLM for response generation
* Streams the response back to the user
* Stores the updated conversation

---

## Tech Stack

* Python
* FastAPI (optional API layer)
* SQLite
* FAISS or Chroma (vector storage)
* OpenAI, Ollama, or Groq (LLM providers)
* MCP (Model Context Protocol for tools)

---


## Setup

Clone the repository:

```bash
git clone https://github.com/mohitraj3697/neurochat_engine.git
cd neurochat_engine
```

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   
```

Install dependencies:



Create a `.env` file:

---

## Roadmap

* Web interface (React / Next.js)
* WebSocket-based streaming
* Authentication system
* Improved memory handling
* Extensible tool/plugin system

---


