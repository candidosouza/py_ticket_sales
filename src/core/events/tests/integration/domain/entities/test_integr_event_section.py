import unittest

from src.core.events.domain.entities.event_section import EventSection
from src.core.events.domain.entities.event_spot import EventSpot


class TestIntegrEventSection(unittest.TestCase):
    def test_create_event_section(self):
        data_spot = {
            'location': 'location',
            'is_reserved': False,
            'is_published': False,
        }
        event_spot = EventSpot(**data_spot)
        data = {
            'name': 'test',
            'description': 'test',
            'total_spot': 100,
            'price': 100.0,
            'spot': [event_spot],
        }
        event_section = EventSection(**data)
        self.assertIsInstance(event_section, EventSection)
        self.assertEqual(event_section.name, data['name'])
        self.assertEqual(event_section.description, data['description'])
        self.assertEqual(event_section.total_spot, data['total_spot'])
        self.assertEqual(event_section.price, data['price'])
        self.assertEqual(event_section.is_published, False)
        self.assertEqual(event_section.total_spot_reserved, 0)
        self.assertEqual(event_section.spot, data['spot'])
