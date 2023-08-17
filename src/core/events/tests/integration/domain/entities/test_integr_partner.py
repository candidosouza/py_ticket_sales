import unittest

from src.core.events.domain.entities.partner import Partner


class TestIntegrPartner(unittest.TestCase):
    def test_create_partner_valid(self):
        data = {'name': 'Partner Name'}
        partner = Partner(**data)
        self.assertIsInstance(partner, Partner)
        self.assertEqual(partner.name, data['name'])

    def test_create_event(self):  # sourcery skip: avoid-builtin-shadow
        data = {'name': 'Partner Name'}
        partner = Partner(**data)
        input = {'name': 'Event Name', 'date': '2020-01-01'}
        event = partner.init_event(input)
        self.assertEqual(event.name, input['name'])
        self.assertEqual(event.date, input['date'])
        self.assertEqual(event.partner_id, partner.id)
