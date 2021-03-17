from unittest import TestCase
from post import Post
class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')
        # test that the Test we pass in and post title are the same
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

