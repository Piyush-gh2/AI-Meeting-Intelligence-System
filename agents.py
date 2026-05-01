from src.parser import load_meeting
from src.summary import generate_summary
from src.actions import extract_actions
from src.decisions import extract_decisions

def analyze_meeting():
    lines = load_meeting()
    
    summary = generate_summary(lines)
    actions = extract_actions(lines)
    decisions = extract_decisions(lines)
    
    return summary, actions, decisions