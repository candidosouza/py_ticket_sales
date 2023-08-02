import unittest

from src.core.events.domain.entities.event import EventCommand, Event
from src.core.events.domain.entities.event_section import EventSectionCommand, EventSection


class TestIntegrEvent(unittest.TestCase):

    def test_create_event_valid(self):
        data_command = {
            'name': 'test',
            'description': 'test',
            'total_spot': 100,
            'price': 100.0
        }
        command = EventSectionCommand(**data_command)
        event_section = EventSection.create(command)

        event_command = {
                'name': 'Event Name',
                'description': 'Event Description',
                'date': '2021-12-12',
                'total_spot': 100,
                'partner_id': 'partner_id',
                'sections': [event_section]
            }
        command = EventCommand(**event_command)
        event = Event.create(command)
        self.assertIsInstance(event, Event)
        self.assertEqual(event.name, event_command['name'])
        self.assertEqual(event.description, event_command['description'])
        self.assertEqual(event.date, event_command['date'])
        self.assertEqual(event.total_spot, event_command['total_spot'])
        self.assertEqual(event.partner_id, event_command['partner_id'])
        self.assertEqual(event.sections, event_command['sections'])
        self.assertEqual(event.is_published, False)
        self.assertEqual(event.total_spot_reserved, 0)
        

