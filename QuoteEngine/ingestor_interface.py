from abc import ABC, abstractmethod

class IngestorInterface(ABC):
    """Abstract Base Class of parsers."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Confirm if file type is allowed"""
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(self, path):
        """Create quotes."""
        pass
