from django.test import SimpleTestCase


#checking whether the different urls give successfull http requests
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code():
        response=self.client.get('/')
        self.asserEqual(response.status_code,200)

    def test_about_page_status_code():
        response=self.client.get('about')
        self.asserEqual(response.status_code,200)
