def explain_result(result, llm):
    prompt = f"""
You are an enterprise AI assistant.
Explain this decision clearly for business users.

Decision:
{result}
"""
    return llm.ask(prompt)
