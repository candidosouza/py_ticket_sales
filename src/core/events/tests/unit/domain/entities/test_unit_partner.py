import unittest

from src.core.events.domain.entities.partner import Partner


class TestUnitPartner(unittest.TestCase):

    def test_create_partner_valid(self):
        data = {
            "name": "Partner 1",
        }
        partner = Partner(**data)
        self.assertEqual(partner.name, data["name"])