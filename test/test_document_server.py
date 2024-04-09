import unittest

from document.document import Document
from document_server.document_server import DocumentServer
from user.user import User


class TestDocumentServer(unittest.TestCase):

    def setUp(self):
        self.document_name = "document1"
        self.document_content = "This is the initial content of the document1.\nThis will be modified."
        self.document_server = DocumentServer()
        self.document = Document(name=self.document_name, content=self.document_content)
        self.user = User()
        self.list_of_users = [self.user]


    def tearDown(self):
        pass

    def test_document_server_can_serve(self):
        assertion_text = "serving document1"
        serve_output = self.document_server.serve(self.document, self.list_of_users)
        self.assertEqual(assertion_text, serve_output)

    def test_document_server_edit_doc_add_text(self):
        # initial state of the content of document1 should not have the added_text
        added_text = "This is the added text."
        self.assertNotIn(added_text, self.document.display_content())
        # now edit the document by adding text to it
        self.document_server.add_text(doc=self.document, user=self.user, added_text=added_text)
        self.assertIn(added_text, self.document.display_content())

    def test_document_server_edit_doc_delete_text(self):
        # initial state of the content of document1 should contain the text_to_remove
        text_to_remove = "initial content of the"
        self.assertIn(text_to_remove, self.document.display_content())
        # now edit the document by removing the text_to_remove string from it
        self.document_server.delete_text(doc=self.document, user=self.user, text_to_remove=text_to_remove)
        self.assertNotIn(text_to_remove, self.document.display_content())



