import unittest

from src.core.events.domain.entities.event_section import EventSection, EventSectionCommand


class TestIntegrEventSection(unittest.TestCase):

    def test_create_event_section_valid(self):
        data_command = {
            'name': 'test',
            'description': 'test',
            'total_spot': 100,
            'price': 100.0
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
        