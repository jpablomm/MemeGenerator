from .ingestor_interface import IngestorInterface
from .textingestor import TextIngestor
from .csvingestor import CSVIngestor
from .docxingestor import DocxIngestor
from .pdfingestor import PDFIngestor
from .quote import QuoteModel

class Ingestor(IngestorInterface):
    ingestors = [TextIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
