def generate_summary(lines):
    summary = " ".join([line.strip() for line in lines[:3]])
    return summary