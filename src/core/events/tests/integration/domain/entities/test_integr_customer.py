import unittest

from src.core.events.domain.entities.customer import Customer
from src.core.common.domain.value_objects import Cpf


class TestIntegrCustomer(unittest.TestCase):
    def test_create_customer(self):
        data = {
            "name": "Jhon Doe",
            "cpf": Cpf("070.300.380-10")
        }
        customer = Customer(**data)
        self.assertEqual(customer.name, "Jhon Doe")
        self.assertEqual(customer.cpf.cpf, "070.300.380-10")

    def test_change_customer_name(self):
        data = {
            "name": "Jhon Doe",
            "cpf": Cpf("795.724.670-26")
        }
        customer = Customer(**data)
        customer.change_name("Jhon Doe Souza")
        self.assertEqual(customer.name, "Jhon Doe Souza")
        self.assertEqual(customer.cpf.cpf, "795.724.670-26")

    def test_change_customer_name_with_invalid_name(self):
        data = {
            "name": "Jhon Doe",
            "cpf": Cpf("795.724.670-26")
        }
        customer = Customer(**data)

        with self.assertRaises(ValueError) as context:
            customer.change_name("")
        self.assertTrue("Nome Inválido" in str(context.exception))
