from docling.document_converter import DocumentConverter

source = "https://www.google.com"  # URL
converter = DocumentConverter()
doc = converter.convert(source).document

print(doc.export_to_markdown())
