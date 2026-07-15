from loader import load_pdf

documents = load_pdf("data/example.pdf")

print(f"Pages: {len(documents)}")

print(documents[0].page_content[:300])