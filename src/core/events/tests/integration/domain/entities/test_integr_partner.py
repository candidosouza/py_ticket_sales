import unittest

from src.core.events.domain.entities.partner import Partner


class TestIntegrPartner(unittest.TestCase):
    def test_create_partner_valid(self):
        data = {'name': 'Partner Name'}
        partner = Partner(**data)
        self.assertIsInstance(partner, Partner)
        self.assertEqual(partner.name, data['name'])
