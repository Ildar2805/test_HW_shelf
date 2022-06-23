import unittest
from parameterized import parameterized
from main import show_document_info, get_doc_shelf, get_doc_owner_name, get_all_doc_owners_names, \
remove_doc_from_shelf, directories, append_doc_to_shelf, documents, delete_doc


class TestFunction(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('11-2'), 'Геннадий Покемонов')

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"})

    def test_remove_doc_from_shelf(self):
        result = remove_doc_from_shelf('10006')
        self.assertNotIn('10006', directories['2'])

    def test_append_doc_to_shelf(self):
        result = append_doc_to_shelf('9213', '3')
        self.assertIn('9213', directories['3'])

    def test_delete_doc(self):
        result = delete_doc('2207 876234')
        self.assertEqual(len(documents), 2)
        self.assertNotIn('2207 876234', directories['1'])

    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf('10006'), '2')

    def test_show_document_info(self):
        self.assertEqual(
            show_document_info({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}),
            'passport "2207 876234" "Василий Гупкин"'
        )



