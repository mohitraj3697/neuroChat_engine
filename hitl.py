from typing import Annotated, TypedDict
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, BaseMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command
import os
from dotenv import load_dotenv


load_dotenv()



groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5,
    groq_api_key=groq_api_key
)


#state

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

#node
def chat_node(state: ChatState):

    #hitl
    decision = interrupt({
        "type": "approval",
        "reason": "Model is about to answer a user question.",
        "question": state["messages"][-1].content,
        "instruction": "Approve this question? yes/no"
    })

    #not approved
    if decision["approved"] == 'no':
        return {"messages": [AIMessage(content="Not approved.")]}

     #approved
    else:
        response = llm.invoke(state["messages"])
        return {"messages": [response]}

#graph
builder = StateGraph(ChatState)

builder.add_node("chat", chat_node)
builder.add_edge(START, "chat")
builder.add_edge("chat", END)


checkpointer = MemorySaver()

app = builder.compile(checkpointer=checkpointer)


#tread config
config = {"configurable": {"thread_id": "1234"}}


initial_input = {
    "messages": [
        ("user", "Explain the theory of relativity in simple terms?")
    ]
}

result = app.invoke(initial_input, config=config)


message = result['__interrupt__'][0].value
print("\nBackend message:", message)


user_input = input("\nApprove this question? (y/n): ")


final_result = app.invoke(
    Command(resume={"approved": user_input}),
    config=config,
)

#o/p
print("\nFinal Answer:\n")
print(final_result["messages"][-1].content)