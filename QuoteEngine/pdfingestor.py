from .ingestor_interface import IngestorInterface
from .quote import QuoteModel

import subprocess
import os
import random

class PDFIngestor(IngestorInterface):
    """Parse .pdf file to create QuoteModel objects"""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path):
        """Read pdf file and return list quotes"""
        if not cls.can_ingest(path):
            raise Exception('File extension not compatible')
        
        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(' - ')
                new_quote = QuoteModel(author=parsed[1], body=parsed[0])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes