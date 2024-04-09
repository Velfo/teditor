import unittest

from user.user import User
from document.document import Document


class TestUser(unittest.TestCase):

    def setUp(self):
        self.u1 = User('John')
        self.u2 = User('Jack')
        pass

    def tearDown(self):
        pass

    def test_user_init(self):
        self.assertEqual(self.u1.display_name(), 'John')
        self.assertEqual(self.u2.display_name(), 'Jack')

    def test_user_add_document(self):
        doc = Document(name="random1", content="random content for the ramdom1")
        self.u1.add_document(doc)
        assert doc in self.u1.get_documents_list()

