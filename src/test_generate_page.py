import unittest

from generate_page import (
    extract_title,
)

class TestGeneratePage(unittest.TestCase):

    def test_extract_title(self):
        md = "# Hello! "
        title = extract_title(md)
        self.assertEqual(title, "Hello!")