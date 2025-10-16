from docling.document_converter import DocumentConverter

source = "./example.md"  # file path
converter = DocumentConverter()
doc = converter.convert(source).document

print(doc.export_to_markdown())
