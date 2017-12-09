

class Status:
    def __init__(self, json: str):
        self.json = json

    def build(self):
        pass

    def _parse_json(self):
        pass

    class Parser:
        def __call__(self, data):
            # TODO: Implement status parser (need data sample)
            return str(data)
