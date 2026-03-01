import sqlite3

class RAGEngine:
    def __init__(self, db_path="db/knowledge.db"):
        self.conn = sqlite3.connect(db_path)

    def ask(self, query, llm):
        return llm.ask(f"Answer based on database: {query}")
