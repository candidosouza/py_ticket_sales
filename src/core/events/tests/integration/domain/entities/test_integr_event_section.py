import unittest

from src.core.events.domain.entities.event_section import EventSection, EventSectionCommand
from src.core.events.domain.entities.event_spot import EventSpot, EventSpotCommand


class TestIntegrEventSection(unittest.TestCase):

    def test_create_event_section(self):
        data_event_spot_command = {
            'location': 'location',
            'is_reserved': False,
            'is_published': False
        }
        event_spot_command = EventSpotCommand(**data_event_spot_command)
        event_spot = EventSpot.create(event_spot_command)
        data_command = {
            'name': 'test',
            'description': 'test',
            'total_spot': 100,
            'price': 100.0,
            'spot': [event_spot]
        }
        command = EventSectionCommand(**data_command)
        event_section = EventSection.create(command)
        self.assertIsInstance(event_section, EventSection)
        self.assertEqual(event_section.name, data_command['name'])
        self.assertEqual(event_section.description, data_command['description'])
        self.assertEqual(event_section.total_spot, data_command['total_spot'])
        self.assertEqual(event_section.price, data_command['price'])
        self.assertEqual(event_section.is_published, False)
        self.assertEqual(event_section.total_spot_reserved, 0)
        self.assertEqual(event_section.spot, data_command['spot'])
        