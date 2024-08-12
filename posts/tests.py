from django.test import TestCase
from django.contrib.auth.models import User
from .models import Posts

# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abcd1234'
        )
        testuser1.save()

        # create a blog post
        test_post = Posts.objects.create(
            author=testuser1, title='Blog title', body='Body content...'
        )
        test_post.save()

    def test_blog_content(self):
        post = Posts.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content...')