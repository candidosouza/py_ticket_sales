from dataclasses import asdict
import unittest
from unittest.mock import Mock, patch

from src.core.events.domain.entities.customer import Customer


class TestUnitCustomer(unittest.TestCase):

    def test_create_customer_valid(self):
        customer_input = {
            'cpf': '896.486.520-07',
            'name': 'John Doe'
        }

        cpf_mock = Mock()
        cpf_mock.cpf = '896.486.520-07'

        with patch('src.core.common.domain.value_objects.Cpf', return_value=cpf_mock):
            customer = Customer.create(customer_input)

        self.assertEqual(customer.cpf.cpf, '896.486.520-07')
        self.assertEqual(customer.name, 'John Doe')


    def test_change_customer_name(self):
        customer_input = {
            'cpf': '795.724.670-26',
            'name': 'John Doe'
        }

        cpf_mock = Mock()
        cpf_mock.cpf = '795.724.670-26'

        with patch('src.core.common.domain.value_objects.Cpf', return_value=cpf_mock):
            customer = Customer.create(customer_input)

        customer.change_name("Jhon Doe Souza")
        self.assertEqual(customer.name, "Jhon Doe Souza")
        self.assertEqual(customer.cpf.cpf, "795.724.670-26")

    def test_change_customer_name_with_invalid_name(self):
        customer_input = {
            'cpf': '195.841.570-78',
            'name': 'John Doe'
        }

        cpf_mock = Mock()
        cpf_mock.cpf = '195.841.570-78'

        with patch('src.core.common.domain.value_objects.Cpf', return_value=cpf_mock):
            customer = Customer.create(customer_input)

        message = "Nome Inválido"

        with self.assertRaises(ValueError) as context:
            customer.change_name("")
        self.assertTrue(message in str(context.exception))

        with self.assertRaises(ValueError) as context:
            customer.change_name(1)
        self.assertTrue(message in str(context.exception))

        with self.assertRaises(ValueError) as context:
            customer.change_name(None)
        self.assertTrue(message in str(context.exception))
