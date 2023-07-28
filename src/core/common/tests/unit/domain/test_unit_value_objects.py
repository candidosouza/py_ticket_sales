from abc import ABC
from dataclasses import FrozenInstanceError, dataclass, is_dataclass
import unittest
from unittest.mock import patch, Mock
import uuid
from src.core.common.domain.value_objects import Cpf, IdUUID, ValueObject
from src.core.common.domain.exceptions import InvalidCpfException, InvalidUuidException


@dataclass(frozen=True)
class StubOneProp(ValueObject):
    prop: str


@dataclass(frozen=True)
class StubTwoProp(ValueObject):
    prop1: str
    prop2: str


class TestValueObjectUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(ValueObject))

    def test_if_is_a_abc(self):
        self.assertIsInstance(ValueObject(), ABC)

    def test_init_prop(self):
        value_object = StubOneProp(prop='value')
        self.assertEqual(value_object.prop, 'value')

        value1_object = StubTwoProp(prop1='value1', prop2='value2')
        self.assertEqual(value1_object.prop1, 'value1')
        self.assertEqual(value1_object.prop2, 'value2')

    def test_convert_to_string(self):
        value_object = StubOneProp(prop='value')
        self.assertEqual(value_object.prop, str(value_object))

        value1_object = StubTwoProp(prop1='value1', prop2='value2')
        self.assertEqual(
            '{"prop1": "value1", "prop2": "value2"}', str(value1_object))

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = StubOneProp(prop='value')
            value_object.prop = 'fake'


class TestIdUUIDUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(IdUUID))

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = IdUUID()
            value_object.id = 'fake id'

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(
            IdUUID,
            '_IdUUID__validate',
            autospec=True,
            side_effect=IdUUID._IdUUID__validate 
        ) as mock_validate:
            with self.assertRaises(InvalidUuidException) as assert_error:
                IdUUID('fake id')
            mock_validate.assert_called_once()
            self.assertEqual(mock_validate.call_count, 1)
            self.assertEqual(
                assert_error.exception.args[0], 'ID must be a valid UUID')
            
    def test_accept_uui_passed_in_init(self):
        with patch.object(
            IdUUID,
            '_IdUUID__validate',
            autospec=True,
            side_effect=IdUUID._IdUUID__validate
        ) as mock_validate:
            value_object = IdUUID(
                '8177e159-7ef3-4ee8-ac94-35ef1604905c')
            mock_validate.assert_called_once()
            self.assertEqual(
                value_object.id, '8177e159-7ef3-4ee8-ac94-35ef1604905c')

        uuid_value = uuid.uuid4()
        value_object = IdUUID(uuid_value)
        self.assertEqual(value_object.id, str(uuid_value))

    def test_generate_id_when_no_passed_id_in_init(self):
        with patch.object(
            IdUUID,
            '_IdUUID__validate',
            autospec=True,
            side_effect=IdUUID._IdUUID__validate
        ) as mock_validate:
            value_object = IdUUID()
            uuid.UUID(value_object.id)
            mock_validate.assert_called_once()


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
        