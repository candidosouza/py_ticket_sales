import unittest

from src.core.events.domain.entities.event_section import EventSection, EventSectionInput
from src.core.events.domain.entities.event_spot import EventSpot, EventSpotInput


class TestIntegrEventSection(unittest.TestCase):

    def test_create_event_section(self):
        data_event_spot_input = {
            'location': 'location',
            'is_reserved': False,
            'is_published': False
        }
        event_spot_input = EventSpotInput(**data_event_spot_input)
        event_spot = EventSpot.create(event_spot_input)
        data_input = {
            'name': 'test',
            'description': 'test',
            'total_spot': 100,
            'price': 100.0,
            'spot': [event_spot]
        }
        input = EventSectionInput(**data_input)
        event_section = EventSection.create(input)
        self.assertIsInstance(event_section, EventSection)
        self.assertEqual(event_section.name, data_input['name'])
        self.assertEqual(event_section.description, data_input['description'])
        self.assertEqual(event_section.total_spot, data_input['total_spot'])
        self.assertEqual(event_section.price, data_input['price'])
        self.assertEqual(event_section.is_published, False)
        self.assertEqual(event_section.total_spot_reserved, 0)
        self.assertEqual(event_section.spot, data_input['spot'])
        