def extract_decisions(lines):
    decisions = []
    for line in lines:
        if "should" in line or "let's" in line.lower():
            decisions.append(line.strip())
    return decisions