class KnowledgeStore:

    def __init__(self):
        self.documents = [
            "Our refund policy allows returns within 30 days.",
            "Employees are allowed 20 days of annual leave.",
            "Support is available Monday to Friday."
        ]

    def get_all_documents(self):
        return self.documents
