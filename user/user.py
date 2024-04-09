from dataclasses import dataclass

from document.document import Document





@dataclass
class User:
    __name: str = ''
    __age: int = 0
    __list_of_documents = []

    def set_name(self, name: str):
        self.__name = name

    def display_name(self):
        return self.__name

    def display_age(self):
        return self.__age

    def add_document(self, doc: Document) -> None:
        self.__list_of_documents.append(doc)

    def get_documents_list(self) -> [Document]:
        return self.__list_of_documents

    def display_document(self, doc: Document):
        if doc in self.__list_of_documents:
            return doc.display_content()
        else:
            return "Document Not Found"








