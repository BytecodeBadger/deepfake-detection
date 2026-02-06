# Deepfake Detection
An agent to detect deepfake images.

## The agent should:  

- Use a Vision LLM (like GPT-4o or Claude 3.5 Sonnet) to detect if a photo looks "stock" or has watermarks.  

- Use a text model to check for "scammy" language in the description.  

- Cross-reference the two for "Modality Dissonance" (e.g., text says "Beachfront" but the AI sees "Mountain view" in the photo).  

- Tech Stack: Python, LangChain/LangGraph, OpenAI/Anthropic API, and a vector DB (Pinecone/Milvus).  
