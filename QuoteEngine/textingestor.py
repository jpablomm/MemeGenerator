from .ingestor_interface import IngestorInterface
from .quote import QuoteModel

class TextIngestor(IngestorInterface):
    """Parse .txt file to create QuoteModel objects"""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path):
        """Read text file and return list quotes"""
        if not cls.can_ingest(path):
            raise Exception('File extension not compatible')

        quotes = []

        with open(path) as infile:
            data = infile.readlines()
            for line in data:
                words = line.strip()
                words = words.split(' - ')
                if len(words) > 1:
                    body = words[0]
                    author = words[1]
                    quote = QuoteModel(author, body)
                    quotes.append(quote)
        return quotes
