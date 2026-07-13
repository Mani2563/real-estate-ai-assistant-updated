from typing import List, Dict


class ConversationMemory:
    """
    Maintains conversation history.
    """

    def __init__(self):

        self.messages: List[Dict[str, str]] = []

    def add_user_message(self, message: str):

        self.messages.append(
            {
                "role": "user",
                "content": message
            }
        )

    def add_ai_message(self, message: str):

        self.messages.append(
            {
                "role": "assistant",
                "content": message
            }
        )

    def get_history(self):

        history = ""

        for message in self.messages:

            history += (
                f"{message['role'].capitalize()}: "
                f"{message['content']}\n"
            )

        return history

    def clear(self):

        self.messages.clear()