
class QuoteModel:
    """Represents a quote."""
    def __init__(self, author, body):
        self.author = author
        self.body = body

    def __repr__(self):
        return f'{self.body} - {self.author}'

    def __str__(self):
        return f'{self.body} - {self.author}'
