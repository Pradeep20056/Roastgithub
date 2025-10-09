from pdfminer.high_level import extract_text

def parse_resume(pdf_path: str):
    text = extract_text(pdf_path)
    # crude info extraction
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    preview = "\n".join(lines[:40])
    return preview
