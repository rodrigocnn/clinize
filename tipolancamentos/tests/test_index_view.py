from django.test import TestCase


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.resp = self.client.get('/tipo-lancamentos/')
        self.tag_create = '<a href="/tipo-lancamentos/create" class="btn btn-info btn-fill pull-right mb-3">Cadastrar</a>'

    def test_status_code(self):
        """Get /tipo-lancamentos/ must return status code 200"""
        self.assertEquals(self.resp.status_code, 200)

    def test_template_used(self):
        """ must to render tipolancamentos/index.html """
        self.assertTemplateUsed(self.resp, 'tipolancamentos/index.html')

    def test_html(self):
        """Html must contain tags html """
        self.assertContains(self.resp, self.tag_create)
        self.assertContains(self.resp, '<table')
        self.assertContains(self.resp, '<th', 4)
        self.assertContains(self.resp, '<tbody')
