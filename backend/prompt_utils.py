def format_prompt(question: str) -> str:
    return (
        "You are a travel documentation assistant. Answer the following question in a helpful, organized format.\n"
        f"Question: \"{question}\""
    ) 