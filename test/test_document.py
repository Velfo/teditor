import unittest

from document.document import Document


class TestDocument(unittest.TestCase):

    def setUp(self):
        self.doc = Document(title='title', content='content')

    def tearDown(self):
        pass

    def test_document_init(self):
        self.assertEqual(self.doc.display_title(), 'title')
