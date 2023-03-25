import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(10000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassassa_rahaa_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)


    def test_kateisosto_edullinen_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukas_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(self.kortti.saldo, 9760)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kortti.saldo, 9600)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_edullinen_ei_riittava(self):
        self.kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(self.kortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_maukas_ei_riittava(self):
        self.kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), False)
        self.assertEqual(self.kortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo, 11000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_lataa_rahaa_kortille_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(self.kortti.saldo, 10000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        
