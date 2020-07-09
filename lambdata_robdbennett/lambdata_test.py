#!/usr/bin/env python
"""Tests for lambdata modules."""

import unittest
# unittest supports a type of tests called unit tests.
# A unit is the smallest piece of code we can test. Typically a function or method.
# other types of tests (not needed yet):
# Integration- testing multiple pieces working together
# end to end- testing a full flow/ use space.
# There are also manual/non-code tests, like user acceptance testing (someone playing with it)
from random import randint
import classes
import __example_module__
import test

class ExampleModuleTests(unittest.TestCase):
    """A test for the simple increment function and colors list."""
    def test_increment(self):
        x1 = 7
        y1 = __example_module__.increment(x1)
        x2 = -10
        y2 = __example_module__.increment(x2)
        self.assertEqual(y1, 8)
        self.assertEqual(y2, -9)

    def test_colors(self):
        self.assertIn('Black', __example_module__.COLORS)
        self.assertNotIn('Magenta', __example_module__.COLORS)

class SocialMediaUserTests(unittest.TestCase):
    """Making sure our example classes work as expected"""
    def test_social_media_name(self):
        """Testing that classes work"""
        user1 = test.SocialMediaUser('Rob')
        user2 = test.SocialMediaUser('Jane')
        self.assertEqual(user1.name, 'Rob')
        self.assertEqual(user2.name, 'Jane')
    
    def test_default_upvotes(self):
        """Testing that upvotes tabulate"""
        user1 = test.SocialMediaUser('Rob')
        self.assertEqual(user1.upvotes, 0)
    
    def test_unpopular(self):
        """Testing that unpopular reports correctly."""
        user1 = test.SocialMediaUser('Rob')
        for _ in range(randint(1, 100)):
            user1.receive_upvote()
        self.assertEqual(user1.is_popular(), False)
    
    def test_popular(self):
        """Testing that popular reports correctly."""
        user1 = test.SocialMediaUser('Rob')
        for _ in range(randint(101, 1000)):
            user1.receive_upvote()
        self.assertEqual(user1.is_popular(), True)

class GamerNerdTests(unittest.TestCase):
    """This should test the different objects of gamers and their inheritance"""
    def test_base_gamer(self):
        user1 = classes.Gamer('Rob', 39)
        self.assertEqual(user1.beard, None)
        self.assertEqual(user1.position, 0)
    
    def test_larper(self):
        """Tests base attributes of Larper"""
        user1 = classes.Larper('Rob', 39)
        self.assertEqual(user1.beard, True)

    def test_tabletop(self):
        """Tests base attributes of Tabletop"""
        user1 = classes.Tabletop('Rob', 39)
        self.assertEqual(user1.snobbery, True)
        self.assertEqual(user1.age, 39)
    
    def test_parlor(self):
        """Testing that hobbies add correctly to a Parlor object."""
        user1 = classes.Parlor('Rob', 39)
        user1.hobby = 'videogames'
        self.assertEqual(user1.hobby, 'videogames')
        self.assertEqual(user1.games_played, 'indoor')
    


if __name__ == '__main__':
    unittest.main()
