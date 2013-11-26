#!/usr/bin/env python

"""
Test case for linkedlist.py module.
"""

import unittest
from pyowm.commons.frontlinkedlist import FrontLinkedList

class TestLinkedList(unittest.TestCase):
    
    def test_add(self):
        instance = FrontLinkedList()
        self.assertEquals(0, instance.size())
        instance.add("test1")
        self.assertEquals(1, instance.size())
        instance.add("test2")
        self.assertEquals(2, instance.size())

    def test_remove(self):
        instance = FrontLinkedList()
        for i in range(1,6):
            instance.add(i)
        self.assertEquals(5, instance.size())
        instance.remove(3)
        self.assertEquals(4, instance.size())
        for item in instance:
            self.assertNotEquals(3, item.data())
            
    def test_remove_deletes_the_first_occurrence_from_the_front(self):
        instance = FrontLinkedList()
        instance.add("4")
        instance.add("3")
        instance.add("2")
        instance.add("1")
        instance.add("4")
        instance.add("0")
        instance.remove("4")
        counter = 0
        next_item = None
        for item in instance:
            if item.data() == "4":
                counter += 1
                next_item = item.next()
        self.assertEquals(1, counter)
        self.assertFalse(next_item)
        
    def test_contains(self):
        instance = FrontLinkedList()
        instance.add(12)
        instance.add(3)
        instance.add(456)
        self.assertTrue(instance.contains(3))
        self.assertFalse(instance.contains("test"))
                