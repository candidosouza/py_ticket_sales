from dataclasses import asdict
import unittest
from unittest.mock import Mock, patch

from src.core.events.domain.entities.event_section import EventSection


class TestUnitEventSection(unittest.TestCase):

    def test_create_event_section_valid(self):
        data = {
            'name': 'test',
            'description': 'test',
            'total_spot': 100,
            'price': 100.0,
            'spot': []
        }
        event_section = EventSection(**data)
        self.assertIsInstance(event_section, EventSection)
        self.assertEqual(event_section.name, data['name'])
        self.assertEqual(event_section.description, data['description'])
        self.assertEqual(event_section.total_spot, data['total_spot'])
        self.assertEqual(event_section.price, data['price'])
        self.assertEqual(event_section.is_published, False)
        self.assertEqual(event_section.total_spot_reserved, 0)