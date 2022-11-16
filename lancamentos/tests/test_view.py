from django.test import TestCase
from django.urls import reverse


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.resp = self.client.get(reverse('fluxo_caixa_home'))

    def test_status_code(self):
        """Get /lancamentos/ must return status code 200"""
        self.assertEquals(self.resp.status_code, 200)

    def test_template_used(self):
        """ must to render lancamentos/index.html """
        self.assertTemplateUsed(self.resp, 'lancamento/index.html')

    def test_html(self):
        """Html must contain tags html """
        self.assertContains(self.resp, 'Cadastrar')
        self.assertContains(self.resp, '<table')
        self.assertContains(self.resp, '<th', 6)
        self.assertContains(self.resp, '<tbody')
