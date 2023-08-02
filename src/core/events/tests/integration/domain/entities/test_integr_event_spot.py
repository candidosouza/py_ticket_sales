import unittest

from src.core.events.domain.entities.event_spot import EventSpot, EventSpotCommand


class TestIntegrEventSpot(unittest.TestCase):
    def test_create_event_spot(self):
        event_spot_command = {
            'location': 'location',
            'is_reserved': False,
            'is_published': False
        }
        command = EventSpotCommand(**event_spot_command)
        event_spot = EventSpot.create(command)
        self.assertEqual(event_spot.location, 'location')
        self.assertEqual(event_spot.is_reserved, False)
        self.assertEqual(event_spot.is_published, False)
