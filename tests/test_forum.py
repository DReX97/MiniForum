import tempfile
import unittest
from pathlib import Path

import app as miniforum

class ForumTests(unittest.TestCase):

    def setUp(self):
        #use a separate temp db for each test
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_database = miniforum.DATABASE
        miniforum.DATABASE = str(Path(self.temp_dir.name) / "test_forum.db")
        miniforum.setup_database()
        self.client = miniforum.app.test_client()

    def tearDown(self):
        #retore the normal db after each test
        miniforum.DATABASE = self.original_database
        self.temp_dir.cleanup()

    def test_homepage_displays_threads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Best co-op games to play', response.data)

    def test_search_finds_rpg(self):
        response = self.client.get('/?search=RPG')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Any good RPGs recommendations?', response.data)
        self.assertNotIn(b'Best co-op games to play', response.data)

    def test_search_no_matches(self):
        response = self.client.get('/?search=Nonexistent')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Best co-op games to play', response.data)
        self.assertNotIn(b'Any good RPGs recommendations?', response.data)

if __name__ == '__main__':
    unittest.main()    