# Performs checklist analysis
import re

def run_analysis(text, checklist):
    results = []
    for item in checklist:
        rule = item.get("rule", "")
        pattern = re.compile(rule, re.IGNORECASE)
        match = pattern.search(text)
        results.append({
            "Item": item.get("item", "Unnamed Item"),
            "Compliant": "Yes" if match else "No",
            "Note": f"Matched: {match.group(0)}" if match else "No match"
        })
    return results
