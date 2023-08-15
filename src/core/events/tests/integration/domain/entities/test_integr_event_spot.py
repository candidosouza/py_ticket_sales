import unittest

from src.core.events.domain.entities.event_spot import EventSpot, EventSpotInput


class TestIntegrEventSpot(unittest.TestCase):
    def test_create_event_spot(self):
        event_spot_input = {
            'location': 'location',
            'is_reserved': False,
            'is_published': False
        }
        input = EventSpotInput(**event_spot_input)
        event_spot = EventSpot.create(input)
        self.assertEqual(event_spot.location, 'location')
        self.assertEqual(event_spot.is_reserved, False)
        self.assertEqual(event_spot.is_published, False)
