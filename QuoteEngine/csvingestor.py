from .ingestor_interface import IngestorInterface
from .quote import QuoteModel

import pandas

class CSVIngestor(IngestorInterface):
    """Parse .csv file to create QuoteModel objects"""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path):
        """Read csv file and return list quotes"""
        
        if not cls.can_ingest(path):
            raise Exception('File extension not compatible')

        quotes = []

        dframe = pandas.read_csv(path, header=0)

        for index, row in dframe.iterrows():
            new_quote = QuoteModel(author=row['author'], body=row['body'])
            quotes.append(new_quote)

        return quotes
