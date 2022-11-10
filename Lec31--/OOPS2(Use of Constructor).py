class Book():
    def __init__(self, name, pages_count) -> None:
        self.Name=name
        self.PagesCount=pages_count
        print(f"I finished {name} book, it had {pages_count} pages")


GOT=Book(name="GameOfThrones",pages_count=58)
GOT=Book("HarryPotter",105)


