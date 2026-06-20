from pdf_loader import PdfReader
from chunker import create_chunks

pdf_path = "data/AI_Engineer_Roadmap.pdf"


pdf_to_words = PdfReader(pdf_path)

chunks = create_chunks(pdf_to_words)

print(f"chunks : {chunks}")