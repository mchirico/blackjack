# -*- coding: utf-8 -*-

from .context import dealer
from dealer.util.cardgen import Junk

from unittest import TestCase


class AdvancedTestSuite(TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(dealer.hmm())

    def test_junk(self):
        j = Junk()
        self.assertEqual("we stuff", j.stuff())
