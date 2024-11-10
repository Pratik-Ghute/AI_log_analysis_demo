from huggingface_hub import InferenceClient
from tokenization import count_tokens
from config import HUGGINGFACE_TOKEN, MAX_TOKEN_LIMIT, MAX_OUTPUT_TOKENS, INSTRUCTION_TEMPLATE

client = InferenceClient(model="meta-llama/Meta-Llama-3-8B-Instruct", token=HUGGINGFACE_TOKEN)

def analyze_logs(log_text: str):
    # Count the tokens and check if it's within the token limit
    log_tokens = count_tokens(log_text)
    print(f"Log token count: {log_tokens}")

    max_input_tokens = MAX_TOKEN_LIMIT - MAX_OUTPUT_TOKENS

    # Split the log if it's too large
    chunks = []
    if log_tokens > max_input_tokens:
        # Split the log into smaller chunks based on the token limit
        while len(log_text) > 0:
            chunk = log_text[:max_input_tokens]
            chunks.append(chunk)
            log_text = log_text[len(chunk):]
    else:
        chunks.append(log_text)

    # Process each chunk separately and collect the responses
    responses = []

    for chunk in chunks:
        prompt = INSTRUCTION_TEMPLATE.format(log_entry=chunk)
        
        # Call the Hugging Face model with the constructed prompt
        response = client.chat_completion(
            [{"role": "user", "content": prompt}],
            max_tokens=MAX_OUTPUT_TOKENS  # Adjust as needed
        )
        
        # Collect the response
        responses.append(response["choices"][0]["message"]["content"])

    # Combine all responses
    final_response = "\n\n".join(responses)
    return final_response
