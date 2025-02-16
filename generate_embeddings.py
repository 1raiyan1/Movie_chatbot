from transformers import AutoTokenizer, AutoModel
import torch
import faiss
import numpy as np

model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def generate_embeddings(dialogue):
    inputs = tokenizer(dialogue, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze()
    return embeddings

def build_faiss_index(dialogues):
    dimension = 384
    index = faiss.IndexFlatL2(dimension)
    embeddings_list = []

    for dialogue in dialogues:
        embedding = generate_embeddings(dialogue).numpy()
        embeddings_list.append(embedding)

    embeddings_array = np.vstack(embeddings_list)
    index.add(embeddings_array)

    faiss.write_index(index, "movie_script.index")

# Replace with actual dialogues from the movie script
dialogues = ["I am Iron Man.", "The truth is, I am Iron Man."]
build_faiss_index(dialogues)
