import unittest

from src.core.events.domain.entities.event_spot import EventSpot


class TestIntegrEventSpot(unittest.TestCase):
    def test_create_event_spot(self):
        data = {
            'location': 'location',
            'is_reserved': False,
            'is_published': False
        }
        event_spot = EventSpot(**data)
        self.assertEqual(event_spot.location, 'location')
        self.assertEqual(event_spot.is_reserved, False)
        self.assertEqual(event_spot.is_published, False)
