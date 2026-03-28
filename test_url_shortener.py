import unittest
from main import app, db, URL

class URLShortenerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_url(self):
        response = self.app.post('/urls', json={'original_url': 'https://www.google.com'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('short_url', response.get_json())

    def test_create_url_invalid(self):
        response = self.app.post('/urls', json={'original_url': 'not_a_url'})
        self.assertEqual(response.status_code, 400)

    def test_list_urls(self):
        self.app.post('/urls', json={'original_url': 'https://www.google.com'})
        response = self.app.get('/urls')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_get_url(self):
        post_resp = self.app.post('/urls', json={'original_url': 'https://www.google.com'})
        short_url = post_resp.get_json()['short_url']
        get_resp = self.app.get(f'/urls/{short_url}')
        self.assertEqual(get_resp.status_code, 200)
        self.assertEqual(get_resp.get_json()['original_url'], 'https://www.google.com')

    def test_update_url(self):
        post_resp = self.app.post('/urls', json={'original_url': 'https://www.google.com'})
        short_url = post_resp.get_json()['short_url']
        put_resp = self.app.put(f'/urls/{short_url}', json={'original_url': 'https://www.example.com'})
        self.assertEqual(put_resp.status_code, 200)
        self.assertEqual(put_resp.get_json()['original_url'], 'https://www.example.com')

    def test_delete_url(self):
        post_resp = self.app.post('/urls', json={'original_url': 'https://www.google.com'})
        short_url = post_resp.get_json()['short_url']
        del_resp = self.app.delete(f'/urls/{short_url}')
        self.assertEqual(del_resp.status_code, 204)
        get_resp = self.app.get(f'/urls/{short_url}')
        self.assertEqual(get_resp.status_code, 404)

    def test_redirect(self):
        post_resp = self.app.post('/urls', json={'original_url': 'https://www.google.com'})
        short_url = post_resp.get_json()['short_url']
        resp = self.app.get(f'/{short_url}', follow_redirects=False)
        self.assertEqual(resp.status_code, 302)
        self.assertIn('https://www.google.com', resp.headers['Location'])

if __name__ == '__main__':
    unittest.main()

