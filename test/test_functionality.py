import unittest
from document.document import Document
from document_server.document_server import DocumentServer
from user.user import User


class TestFunctionality(unittest.TestCase):

    def setUp(self):
        self.document_server = DocumentServer()
        self.user1 = User()
        self.user2 = User()
        self.user3 = User()
        self.list_of_users = [self.user1, self.user2, self.user3]
        pass

    def tearDown(self):
        pass

    def test_one_plus_one_is_two(self):
        self.assertEqual(1, 1)

    def test_multiple_users_can_edit_at_the_same_time(self):
        document1 = Document()
        text_from_user1 = "text from user1"
        text_after_user3_edits = "user1"
        self.document_server.serve(document1, self.list_of_users)
        # user1 edits the document (adds some text)
        self.document_server.add_text(doc=document1, user=self.user1, added_text=text_from_user1,)
        # assert user2 can see user1's edits
        self.assertIn(self.user2.display_document(document1), text_from_user1)
        # user3 edits the document (removes the text_to_remove)
        text_to_remove = "text from "
        self.document_server.delete_text(doc=document1, user=self.user3, text_to_remove=text_to_remove)
        # asser user2 sees the newly edited document
        self.assertEqual(self.user2.display_document(document1), text_after_user3_edits)

    def test_document_maintains_consistency_after_edits(self):
        document2 = Document()
        text_from_user1 = "This is initial text from user1 in document2"
        text_removed_by_user2 = " initial text from"
        text_left_in_document2_after_removing_strings = "This is user1 in document2"
        self.document_server.serve(document2, self.list_of_users)
        # user1 edits the document (adds some text)
        self.document_server.add_text(doc=document2, user=self.user1, added_text=text_from_user1)
        # assert user2 can see user1's edits
        self.assertIn(self.user2.display_document(document2), text_from_user1)
        # assert user3 can also see the same text added by user1
        self.assertIn(self.user3.display_document(document2), text_from_user1)

        # now user2 edits the document (removes some text from the document2)
        self.document_server.delete_text(doc=document2, user=self.user2, text_to_remove=text_removed_by_user2)
        # assert user3 sees the right state of the newly edited document2
        self.assertEqual(self.user3.display_document(document2), text_left_in_document2_after_removing_strings)
        # assert user1 also sees the right state of the newly edited document2
        self.assertEqual(self.user1.display_document(document2), text_left_in_document2_after_removing_strings)
