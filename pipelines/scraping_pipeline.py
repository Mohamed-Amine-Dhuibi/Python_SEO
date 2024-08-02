class MyPipeline:
    def __init__(self):
        self.items = []
        pass

    def process_item(self, item, spider):
        self.items.append(item)
        pass
