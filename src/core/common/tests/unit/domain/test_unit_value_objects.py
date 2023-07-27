import unittest
from unittest.mock import patch, Mock
from src.core.common.domain.value_objects import Cpf
from src.core.common.domain.exceptions import InvalidCpfException

class TestUnitCpf(unittest.TestCase):
    def test_valid_cpf(self):
        cpf_1 = Cpf("77585141033")
        cpf_2 = Cpf("08839074023")
        cpf_3 = Cpf("95422737032")
        cpf_4 = Cpf("56963632022")
        cpf_5 = Cpf("33704854000")
        cpf_6 = Cpf("03415920054")
        cpf_7 = Cpf("27907158079")
        self.assertEqual(cpf_1.cpf, "77585141033")
        self.assertEqual(cpf_2.cpf, "08839074023")
        self.assertEqual(cpf_3.cpf, "95422737032")
        self.assertEqual(cpf_4.cpf, "56963632022")
        self.assertEqual(cpf_5.cpf, "33704854000")
        self.assertEqual(cpf_6.cpf, "03415920054")
        self.assertEqual(cpf_7.cpf, "27907158079")

        with self.assertRaises(AttributeError):
            cpf_1.cpf = "11111111111"

        valid_cpfs = [
            "069.740.898-13",
            "680.125.488-01",
            "088.390.740-23",
            "775.851.410-33"
        ]

        for cpf in valid_cpfs:
            with self.subTest(cpf=cpf):
                Cpf(cpf)

    def test_invalid_cpf(self):
        message = "CPF inválido"

        with self.assertRaises(InvalidCpfException) as context:
            Cpf("")
        self.assertEqual(str(context.exception), "CPF deve ter 11 dígitos")

        with self.assertRaises(InvalidCpfException) as context:
            Cpf(None)
        self.assertEqual(str(context.exception), 'CPF deve ser uma string')

        with self.assertRaises(InvalidCpfException) as context:
            Cpf("123456789")
        self.assertEqual(str(context.exception), "CPF deve ter 11 dígitos")

        with self.assertRaises(InvalidCpfException) as context:
            Cpf("12345678999")
        self.assertEqual(str(context.exception), message)

        with self.assertRaises(InvalidCpfException) as context:
            Cpf("00000000000")
        self.assertEqual(str(context.exception), message)
        