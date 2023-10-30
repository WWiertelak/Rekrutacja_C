from django.test import TestCase
from pesel import utils as pesel_utils


class TestPeselFunctions(TestCase):

    def test_is_valid_pesel(self):
        self.assertTrue(pesel_utils.is_valid_pesel("95062609131"))
        self.assertFalse(pesel_utils.is_valid_pesel("95062609139"))
        self.assertFalse(pesel_utils.is_valid_pesel("2270803628"))
        self.assertFalse(pesel_utils.is_valid_pesel("022708036288"))
        self.assertFalse(pesel_utils.is_valid_pesel("02270803a28"))

    def test_extract_birth_date(self):
        self.assertEqual(pesel_utils.extract_birth_date("02270803628"), "2002-07-08")
        self.assertEqual(pesel_utils.extract_birth_date("95062609131"), "1995-06-26")
        self.assertEqual(pesel_utils.extract_birth_date("82870803628"), "1882-07-08")

    def test_extract_gender(self):
        self.assertEqual(pesel_utils.extract_gender("02270803618"), "Mężczyzna")
        self.assertEqual(pesel_utils.extract_gender("02270803620"), "Kobieta")
