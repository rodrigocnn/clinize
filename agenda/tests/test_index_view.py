from django.test import TestCase


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.resp = self.client.get('/agenda')
        self.tag_create = '<a href="/tipo-lancamentos/create" class="btn btn-info btn-fill pull-right mb-3">Cadastrar</a>'

    def test_status_code(self):
        """Get /agenda/ must return status code 200"""
        self.assertEquals(self.resp.status_code, 200)
