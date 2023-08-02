from dataclasses import asdict
import unittest
from unittest.mock import Mock, patch

from src.core.events.domain.entities.event_section import EventSection, EventSectionCommand


class TestUnitEventSectionCommand(unittest.TestCase):
        
    def test_create_event_section_command_valid(self):
        event_section_command = {
            'name': 'Event Name',
            'description': 'Event Description',
            'total_spot': 100,
            'price': 100.00,
            'spot': []
        }

        event_section_command = EventSectionCommand(**event_section_command)

        self.assertEqual(event_section_command.name, 'Event Name')
        self.assertEqual(event_section_command.description, 'Event Description')
        self.assertEqual(event_section_command.total_spot, 100)
        self.assertEqual(event_section_command.price, 100.00)


class StubEventSectionCommand:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class TestUnitEventSection(unittest.TestCase):

    def test_create_event_section_valid(self):
        data_command = {
            'name': 'test',
            'description': 'test',
            'total_spot': 100,
            'price': 100.0,
            'spot': []
        }
        stub_command = StubEventSectionCommand(**data_command)
        event_section = EventSection.create(stub_command)
        self.assertIsInstance(event_section, EventSection)
        self.assertEqual(event_section.name, data_command['name'])
        self.assertEqual(event_section.description, data_command['description'])
        self.assertEqual(event_section.total_spot, data_command['total_spot'])
        self.assertEqual(event_section.price, data_command['price'])
        self.assertEqual(event_section.is_published, False)
        self.assertEqual(event_section.total_spot_reserved, 0)