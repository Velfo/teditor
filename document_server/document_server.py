from user.user import User
from document.document import Document
import logging
import datetime


class DocumentServer:
    def __init__(self):
        self.num_docs = 0
        self.num_users = 0
        self.list_of_docs = []
        self.list_of_users = []
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

    def serve(self, doc: Document, users: [User]) -> str:
        self.list_of_docs.append(doc)
        doc_name = doc.display_name()
        for user in users:
            user.add_document(doc)
        return "serving "+doc_name

    def add_text(self, added_text: str, doc: Document, user: User, position: int = 0) -> None:
        self.log_entry(user=user, doc=doc, action=self.add_text.__name__)
        new_content = doc.display_content()[:position] + added_text + doc.display_content()[position:]
        doc.set_content(new_content)

    def delete_text(self, text_to_remove: str, doc: Document, user: User, position: int = 0) -> None:
        self.log_entry(user=user, doc=doc, action=self.delete_text.__name__)
        doc_content = doc.display_content()
        if text_to_remove in doc_content:
            new_content = doc.display_content().replace(text_to_remove, '')
            doc.set_content(new_content)
        else:
            print(f'The text \'{text_to_remove}\' not found in document {doc.display_name()}')

    def log_entry(self, user: User, doc: Document, action:str) -> None:
        log_entry = ('Action performed ' + action + '. The document named ' + doc.display_name() + ' is edited by user '
                     ' called ' + user.display_name() + ' on ' + str(datetime.datetime.now()))
        self.logger.info(log_entry)











