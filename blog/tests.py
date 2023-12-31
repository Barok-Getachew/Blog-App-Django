from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import blog


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@gmail.com',
            password = 'secret',
        )
        self.blog = blog.objects.create(
            title =  'A good title',
            body = 'Nice body content',
            author = self.user,

        )

    def test_string_representation(self):

        blog = blog(title = 'A sample title')
        self.assertEqual(str(blog),blog.title)
    def test_blog_content(self):
        self.assertEqual(f'{self.blog.title}', 'A good title')
        self.assertEqual(f'{self.blog.author}', 'testuser')
        self.assertEqual(f'{self.blog.body}', 'Nice body content')    
    def test_blog_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Nice body content')
        self.assertTemplateNotUsed(response,'home.html')
    def test_blog_detail_view(self):
        response= self.client.get('/blog/1')
        no_response = self.client.get('/blog/100000')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'A good title')
        self.assertTemplateUsed(response,'detail.html')
    def test_blog_update(self):
        response =self.client.post(reverse('edit.html',args='1')),{
            'title': 'Updated title',
            'body': 'Updated text',
        }
        self.assertEqual(response.status_code,302)
    def test_post_delete_view(self): # new
            response = self.client.get(reverse('post_delete', args='1'))
            self.assertEqual(response.status_code, 200)
    def test_post_create_view(self): 
        response = self.client.post(reverse('post_new'), {
        'title': 'New title',
        'body': 'New text',
        'author': self.user,})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

