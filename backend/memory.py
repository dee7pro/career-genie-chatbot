class ConversationMemory:
    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append({"role": role, "content": message})

    def get_all(self):
        return self.history

    def clear(self):
        self.history = []