from .ingestor_interface import IngestorInterface
from .quote import QuoteModel

import docx

class DocxIngestor(IngestorInterface):
    """Parse .docx file to create QuoteModel objects"""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path):
        """Read docx file and return list quotes"""
        if not cls.can_ingest(path):
            raise Exception('File extension not compatible')

        quotes = []

        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != '':
                parsed = para.text.split(' - ')
                if len(parsed) > 1:
                    new_quote = QuoteModel(author=parsed[1], body=parsed[0])
                    quotes.append(new_quote)

        return quotes
