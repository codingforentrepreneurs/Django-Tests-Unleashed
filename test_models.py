from django.test import TestCase
from django.utils.text import slugify


from .models import Post # from http://kirr.co/9u0caa/ the posts app.


class PostModelTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title='A new title', slug='some-prob-unique-slug-by-this-test-abc-123')

    def create_post(self, title='This title'):
        return Post.objects.create(title=title)

    def test_post_title(self):
        obj = Post.objects.get(slug='some-prob-unique-slug-by-this-test-abc-123')
        self.assertEqual(obj.title, 'A new title')
        self.assertTrue(obj.content == "") # maybe i want to change 
        #self.assertTrue(100 == 40+2000)

    def test_post_slug(self):
        # generate slug
        title1 = 'another title abc'
        title2 = 'another title abc'
        title3 = 'another title abc'
        slug1 = slugify(title1)
        slug2 = slugify(title2)
        slug3 = slugify(title3)
        obj1 = self.create_post(title=title1)
        obj2 = self.create_post(title=title2)
        obj3 = self.create_post(title=title2)
        self.assertEqual(obj1.slug, slug1)
        self.assertNotEqual(obj2.slug, slug2)
        self.assertNotEqual(obj3.slug, slug3)

    def test_post_qs(self):
        title1 = 'another title abc'
        obj1 = self.create_post(title=title1)
        obj2 = self.create_post(title=title1)
        obj3 = self.create_post(title=title1)
        qs = Post.objects.filter(title=title1)
        self.assertEqual(qs.count(), 3)
        qs2 = Post.objects.filter(slug=obj1.slug)
        self.assertEqual(qs2.count(), 1)





