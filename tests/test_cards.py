# -*- coding: utf-8 -*-

from .context import dealer
from dealer.util.cardgen import Junk
from dealer.util.cardgen import Cards

from unittest import TestCase


class CardsTestSuite(TestCase):
    """Advanced test cases."""

    def test_raddom(self):
        suit_expected = {'H': 13, 'C': 13, 'S': 13, 'D': 13}
        face_expected = {'4': 4, '5': 4, '6': 4, 'A': 4, '9': 4, '7': 4,
                         'T': 4,
                         'K': 4, 'J': 4, 'Q': 4, '8': 4, '3': 4, '2': 4}

        cards = Cards()
        deck = [cards.dealCard() for _ in range(52)]
        suit = {}
        face = {}
        for c in deck:
            suit[c[1]] = suit.get(c[1], 0) + 1
            face[c[0]] = face.get(c[0], 0) + 1

        shared_items = {k: suit[k] for k in suit_expected
                        if k in suit and suit[k] == suit_expected[k]}

        self.assertEqual(4, len(shared_items))

        shared_items = {k: face[k] for k in face_expected
                        if k in face and face[k] == face_expected[k]}
        self.assertEqual(13, len(shared_items))

    def test_junk(self):
        j = Junk()
        self.assertEqual("we stuff", j.stuff())
