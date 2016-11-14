from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from django.utils.text import slugify


"""
Below app is coming form:
http://kirr.co/9u0caa/ 
in the posts app.
"""
from posts.models import Post
from posts.views import post_update, post_create
# Create your tests here.

User = get_user_model()

class PostViewAdvanceTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
                    username='abc123test123',
                    email = 'abc123test123@gmail.com',
                    password = 'pwtest123#$$$',
                    is_staff=True,
                    is_superuser=True,
                )

    def create_post(self, title='This title'):
        return Post.objects.create(title=title)

    def test_user_auth(self):
        obj = self.create_post(title='Another New Title Test')
        edit_url = reverse("posts:update", kwargs={"slug": obj.slug})
        request = self.factory.get(edit_url)
        request.user = self.user
        response = post_update(request, slug=obj.slug)
        self.assertEqual(response.status_code, 200)
        #print(request.user.is_authenticated())

    def test_user_post(self):
        obj = self.create_post(title='Another New Title Test')
        request = self.factory.post("/posts/create/")
        request.user = self.user
        response = post_create(request)
        self.assertEqual(response.status_code, 200)
        #print(request.user.is_authenticated())

    def test_empty_page(self):
        page = '/asdfads/asdfasd/fasdfasdfasd/'
        request = self.factory.get(page)
        request.user = self.user
        response = post_create(request)
        self.assertEqual(response.status_code, 200)

    def test_unauth_user(self):
        obj = self.create_post(title='Another New Title Test')
        edit_url = reverse("posts:update", kwargs={"slug": obj.slug})
        request = self.factory.get(edit_url)
        request.user = AnonymousUser()
        response = post_update(request, slug=obj.slug)
        '''
        Using Class Based views instead of FBVs
        response = PostUpdateView.as_view()(request)
        '''
        self.assertEqual(response.status_code, 404)
    




