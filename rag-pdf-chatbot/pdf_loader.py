from pypdf import PdfReader

# pdf_path = "data/AI_Engineer_Roadmap.pdf"

def load_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

# words = load_pdf(pdf_path)

# print(f"words : {words}\n")
# print(f"first 1000 : {words[:1000]}")