from dataclasses import dataclass
import datetime


@dataclass
class Document:
    """Class for describing a document."""
    name: str = ""
    title: str = ""
    content: str = ""
    author: str = ""
    date: str = ""

    def display_title(self):
        return self.title

    def display_author(self):
        return self.author

    def display_content(self):
        return self.content

    def set_content(self, new_content: str) -> bool:
        try:
            self.content = new_content
            return True
        except ValueError:
            print("Wrong value of added text")
            return False

    def display_name(self):
        return self.name



def main():
    d = Document(name="Test Document", title="Test Title", content="Test Content")
    print(d.display_title())


if __name__ == "__main__":
    main()





