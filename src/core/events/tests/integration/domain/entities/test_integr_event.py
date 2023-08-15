import unittest

from src.core.events.domain.entities.event import EventInput, Event
from src.core.events.domain.entities.event_section import EventSectionInput, EventSection
from src.core.events.domain.entities.event_spot import EventSpot, EventSpotInput


class TestIntegrEvent(unittest.TestCase):

    def test_create_event_valid(self):
        data_event_spot_input = {
            'location': 'location',
            'is_reserved': False,
            'is_published': False
        }
        event_spot_input = EventSpotInput(**data_event_spot_input)
        event_spot = EventSpot.create(event_spot_input)
        data_event_section_input = {
            'name': 'test',
            'description': 'test',
            'total_spot': 100,
            'price': 100.0,
            'spot': [event_spot]
        }
        input = EventSectionInput(**data_event_section_input)
        event_section = EventSection.create(input)

        event_input = {
                'name': 'Event Name',
                'description': 'Event Description',
                'date': '2021-12-12',
                'total_spot': 100,
                'partner_id': 'partner_id',
                'sections': [event_section]
            }
        input = EventInput(**event_input)
        event = Event.create(input)
        self.assertIsInstance(event, Event)
        self.assertEqual(event.name, event_input['name'])
        self.assertEqual(event.description, event_input['description'])
        self.assertEqual(event.date, event_input['date'])
        self.assertEqual(event.total_spot, event_input['total_spot'])
        self.assertEqual(event.partner_id, event_input['partner_id'])
        self.assertEqual(event.sections, event_input['sections'])
        self.assertEqual(event.is_published, False)
        self.assertEqual(event.total_spot_reserved, 0)
