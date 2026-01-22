
from langgraph.graph import StateGraph
from typing import Dict

def log_interaction_tool(data):
    return f"Interaction logged for {data['doctor']}"

def edit_interaction_tool(data):
    return f"Interaction edited for {data['doctor']}"

def summarize_tool(data):
    return "Summary created"

def classify_tool(data):
    return "Interaction classified"

def followup_tool(data):
    return "Follow-up suggested"

tools = {
    "log": log_interaction_tool,
    "edit": edit_interaction_tool,
    "summarize": summarize_tool,
    "classify": classify_tool,
    "followup": followup_tool
}
