from sentence_transformers import SentenceTransformer, util
from data import notizen

model = SentenceTransformer("all-MiniLM-L6-v2")

notizen_embeddings = model.encode(notizen)

def suche(anfrage, threshold=0.5):
    if len(anfrage.strip()) < 3:
        return []

    anfrage_embedding = model.encode(anfrage)

    similarities = util.cos_sim(
        anfrage_embedding,
        notizen_embeddings
    )[0]

    ergebnisse = []

    for i, score in enumerate(similarities):
        score = score.item()

        if score >= threshold:
            ergebnisse.append((score, notizen[i]))

    ergebnisse.sort(reverse=True)

    return ergebnisse