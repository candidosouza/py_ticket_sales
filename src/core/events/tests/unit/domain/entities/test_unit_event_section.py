from dataclasses import asdict
import unittest
from unittest.mock import Mock, patch

from src.core.events.domain.entities.event_section import EventSection, EventSectionInput


class TestUnitEventSectionInput(unittest.TestCase):
        
    def test_create_event_section_input_valid(self):
        event_section_input = {
            'name': 'Event Name',
            'description': 'Event Description',
            'total_spot': 100,
            'price': 100.00,
            'spot': []
        }

        event_section_input = EventSectionInput(**event_section_input)

        self.assertEqual(event_section_input.name, 'Event Name')
        self.assertEqual(event_section_input.description, 'Event Description')
        self.assertEqual(event_section_input.total_spot, 100)
        self.assertEqual(event_section_input.price, 100.00)


class StubEventSectionInput:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class TestUnitEventSection(unittest.TestCase):

    def test_create_event_section_valid(self):
        data_input = {
            'name': 'test',
            'description': 'test',
            'total_spot': 100,
            'price': 100.0,
            'spot': []
        }
        stub_input = StubEventSectionInput(**data_input)
        event_section = EventSection.create(stub_input)
        self.assertIsInstance(event_section, EventSection)
        self.assertEqual(event_section.name, data_input['name'])
        self.assertEqual(event_section.description, data_input['description'])
        self.assertEqual(event_section.total_spot, data_input['total_spot'])
        self.assertEqual(event_section.price, data_input['price'])
        self.assertEqual(event_section.is_published, False)
        self.assertEqual(event_section.total_spot_reserved, 0)