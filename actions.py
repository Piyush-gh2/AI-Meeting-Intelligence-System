def extract_actions(lines):
    actions = []
    for line in lines:
        if "I will" in line:
            actions.append(line.strip())
    return actions