# Deepfake Detection
An agent to detect deepfake images.

## The agent should:  

- Use a Vision LLM (like GPT-4o or Claude 3.5 Sonnet) to detect if a photo looks "stock" or has watermarks.  

- Use a text model to check for "scammy" language in the description.  

- Cross-reference the two for "Modality Dissonance" (e.g., text says "Beachfront" but the AI sees "Mountain view" in the photo).  

- Tech Stack: Python, LangChain/LangGraph, OpenAI/Anthropic API, and a vector DB (Pinecone/Milvus).  

## Dataset
> The Kaggle [deepfake and real images](kaggle.com/datasets/manjilkarki/deepfake-and-real-images) dataset will be used for this project. From main page:  
This dataset contains manipulated images and real images. The manipulated images are the faces which are created by various means. The source for this dataset was https://zenodo.org/record/5528418#.YpdlS2hBzDd
this dataset was processed as our will to get maximum outcome out of these images. Each image is a 256 X 256 jpg image of human face either real or fake