import unittest

from src.core.events.domain.entities.event import Event
from src.core.events.domain.entities.event_section import EventSection
from src.core.events.domain.entities.event_spot import EventSpot


class TestIntegrEvent(unittest.TestCase):

    def test_create_event_valid(self):
        data_spot = {
            'location': 'location',
            'is_reserved': False,
            'is_published': False
        }
        event_spot = EventSpot(**data_spot)
        data_section = {
            'name': 'test',
            'description': 'test',
            'total_spot': 100,
            'price': 100.0,
            'spot': [event_spot]
        }
        event_section = EventSection(**data_section)
        data = {
                'name': 'Event Name',
                'description': 'Event Description',
                'date': '2021-12-12',
                'total_spot': 100,
                'partner_id': 'partner_id',
                'sections': event_section
            }
        event = Event(**data)
        self.assertIsInstance(event, Event)
        self.assertEqual(event.name, data['name'])
        self.assertEqual(event.description, data['description'])
        self.assertEqual(event.date, data['date'])
        self.assertEqual(event.total_spot, data['total_spot'])
        self.assertEqual(event.partner_id, data['partner_id'])
        self.assertEqual(event.sections, data['sections'])
        self.assertEqual(event.is_published, False)
        self.assertEqual(event.total_spot_reserved, 0)

    def test_create_event_without_sections(self):
        data = {
            'name': 'Event Name',
            'description': 'Event Description',
            'date': '2021-12-12',
            'total_spot': 100,
            'partner_id': 'partner_id',
            'sections': []
        }
        event = Event(**data)
        self.assertIsInstance(event, Event)
        self.assertEqual(event.name, data['name'])
        self.assertEqual(event.description, data['description'])
        self.assertEqual(event.date, data['date'])
        self.assertEqual(event.total_spot, data['total_spot'])
        self.assertEqual(event.partner_id, data['partner_id'])
        self.assertEqual(event.sections, data['sections'])
        self.assertEqual(event.is_published, False)
        self.assertEqual(event.total_spot_reserved, 0)

    def test_add_section_and_create_spots(self):
        data_section = {
            'name': 'test',
            'description': 'test',
            'total_spot': 100,
            'price': 100.0
        }
        event_section = EventSection(**data_section)
        data = {
            'name': 'Event Name',
            'description': 'Event Description',
            'date': '2021-12-12',
            'partner_id': 'partner_id',
        }
        event = Event(**data)
        event.add_section(event_section)
        
        self.assertEqual(len(event.sections), 1)
        self.assertEqual(event.total_spot, 100)
        self.assertEqual(len(event.sections[0].spot), 100)
        self.assertEqual(len(event_section.spot), 100)
