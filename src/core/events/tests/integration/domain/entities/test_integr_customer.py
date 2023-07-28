import unittest

from src.core.events.domain.entities.customer import Customer, CustomerCommand


class TestIntegrCustomer(unittest.TestCase):
    def test_create_customer(self):
        command = {
            "name": "Jhon Doe",
            "cpf": "070.300.380-10"
        }
        customer_input = CustomerCommand(**command)
        customer = Customer.create(customer_input)
        self.assertEqual(customer.name, "Jhon Doe")
        self.assertEqual(customer.cpf.cpf, "070.300.380-10")

    def test_change_customer_name(self):
        command = {
            "name": "Jhon Doe",
            "cpf": "795.724.670-26"
        }
        customer_input = CustomerCommand(**command)
        customer = Customer.create(customer_input)
        customer.change_name("Jhon Doe Souza")
        self.assertEqual(customer.name, "Jhon Doe Souza")
        self.assertEqual(customer.cpf.cpf, "795.724.670-26")

    def test_change_customer_name_with_invalid_name(self):
        command = {
            "name": "Jhon Doe",
            "cpf": "795.724.670-26"
        }
        customer_input = CustomerCommand(**command)
        customer = Customer.create(customer_input)

        with self.assertRaises(ValueError) as context:
            customer.change_name("")
        self.assertTrue("Nome Inválido" in str(context.exception))
