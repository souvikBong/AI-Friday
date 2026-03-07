class PromptBuilder:

    def build_prompt(self, query, documents):

        context = "\n".join(documents)

        prompt = f"""
Use the following knowledge to answer the question.

Knowledge:
{context}

Question:
{query}

Answer:
"""

        return prompt
