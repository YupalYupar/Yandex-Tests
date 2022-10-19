import unittest
from unittest.mock import patch
from main import check_document_existance, get_doc_owner_name, delete_doc, add_new_doc


class UnitestHomework(unittest.TestCase):
    def test_check_document_existance(self):
        self.assertEqual(check_document_existance("10006"), True)
        self.assertEqual(check_document_existance("1111"), False)

    @patch('builtins.input')
    def test_get_doc_owner_name(self, doc_num_input):
        doc_num_input.side_effect = ["2207 876234"]
        self.assertEqual(get_doc_owner_name(), "Василий Гупкин")

    @patch('builtins.input')
    def test_delete_doc(self, num_input):
        num_input.side_effect = ['11-2']
        self.assertEqual(delete_doc(), ('11-2', True))

    @patch('builtins.input')
    def test_add_new_doc(self, doc_input):
        doc_input.side_effect = ['10006', 'insurance', 'Аристарх Павлов', '2']
        self.assertEqual(add_new_doc(), '2')
