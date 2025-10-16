from docling.document_converter import DocumentConverter

source = "../../tests/data/pdf/2206.01062.pdf"  # file path
converter = DocumentConverter()
doc = converter.convert(source).document

print(doc.export_to_markdown())
