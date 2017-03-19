from unittest import TestCase

import bobthebot


class TestJoke(TestCase):
    def test_is_string(self):
        s = bobthebot.joke()
        self.assertTrue(isinstance(s, basestring))