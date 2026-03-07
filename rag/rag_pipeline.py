class RAGPipeline:

    def __init__(self, retriever, prompt_builder, llm_client):
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.llm_client = llm_client

    def run(self, query):

        docs = self.retriever.retrieve(query)

        prompt = self.prompt_builder.build_prompt(query, docs)

        response = self.llm_client.generate(prompt)

        return response
