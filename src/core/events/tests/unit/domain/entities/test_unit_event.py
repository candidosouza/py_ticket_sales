from dataclasses import asdict
import unittest
from unittest.mock import Mock, patch

from src.core.events.domain.entities.event import Event, EventCommand


class TestUnitEventCommand(unittest.TestCase):
    
        def test_create_event_command_valid(self):
            event_sections = Mock()
            event_sections.name = 'Event Name'
            event_sections.description = 'Event Description'
            event_sections.is_published = False
            event_sections.total_spot = 100
            event_sections.total_spot_reserved = 0
            event_sections.price = 100.00
    
            event_command = {
                'name': 'Event Name',
                'description': 'Event Description',
                'date': '2021-12-12',
                'total_spot': 100,
                'partner_id': 'partner_id',
                'sections': [event_sections]
            }
    
            event_command = EventCommand(**event_command)
    
            self.assertEqual(event_command.name, 'Event Name')
            self.assertEqual(event_command.description, 'Event Description')
            self.assertEqual(event_command.date, '2021-12-12')
            self.assertEqual(event_command.total_spot, 100)
            self.assertEqual(event_command.partner_id, 'partner_id')


class StubEventCommand:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class TestUnitEvent(unittest.TestCase):

    def test_create_event_valid(self):
        event_sections = Mock()
        event_sections.name = 'Event Name'
        event_sections.description = 'Event Description'
        event_sections.is_published = False
        event_sections.total_spot = 100
        event_sections.total_spot_reserved = 0
        event_sections.price = 100.00

        event_command = {
            'name': 'Event Name',
            'description': 'Event Description',
            'date': '2021-12-12',
            'total_spot': 100,
            'partner_id': 'partner_id',
            'sections': [event_sections]
        }
        stub_event_command = StubEventCommand(**event_command)
        event = Event.create(stub_event_command)

        self.assertEqual(event.name, 'Event Name')
        self.assertEqual(event.description, 'Event Description')
        self.assertEqual(event.date, '2021-12-12')
        self.assertEqual(event.total_spot, 100)
        self.assertEqual(event.partner_id, 'partner_id')