from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.text import slugify


"""
Below app is coming form:
http://kirr.co/9u0caa/ 
in the posts app.
"""
from posts.models import Post
# Create your tests here.


class PostViewTestCase(TestCase):
    def create_post(self, title='This title'):
        return Post.objects.create(title=title)

    def test_list_view(self):
        list_url = reverse("posts:list")
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)


    def test_detail_view(self):
        obj = self.create_post(title='Another New Title Test')
        response = self.client.get(obj.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    
    def test_update_view(self):
        obj = self.create_post(title='Another New Title Test')
        edit_url = reverse("posts:update", kwargs={"slug": obj.slug})
        print(edit_url)
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 404)

    def test_delete_view(self):
        obj = self.create_post(title='Another New Title Test')
        #delete_url = reverse("posts:delete", kwargs={"slug": obj.slug})
        delete_url = obj.get_absolute_url() + "delete/"
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 404)




