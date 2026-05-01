def load_meeting():
    with open("meetings.txt") as f:
        return f.readlines()