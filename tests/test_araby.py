#!/usr/bin/python
# -*- coding=utf-8 -*-
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )
import unittest
import sys
sys.path.append('../pyarabic')
import pyarabic.araby as ar

class ArabyTestCase(unittest.TestCase):
    """Tests for `araby.py`."""

    def test_strip_tashkeel(self):
        """Test striped tashkeel for العربية?"""
        word = u"الْعَرَبِيَّةُ"
        word_nm = u'العربية'
        self.assertEqual(ar.strip_tashkeel(word), word_nm)
        self.assertNotEqual(ar.strip_tashkeel(word), word)
    def test_strip_harakat(self):
        """Test striped tashkeel for العربية?"""
        word = u"الْعَرَبِيَّةُ"
        word_nm = u'العربيّة'
        self.assertEqual(ar.strip_harakat(word), word_nm)
        self.assertNotEqual(ar.strip_harakat(word), word)
        
    def test_waznlike(self):
        """Test if wazn like?"""
        word = u"ضارب"
        wazn = u"فَاعِل"
        self.assertTrue(ar.waznlike(word, wazn))

    def test_shaddalike(self):
        """Test if shadda  like?"""
        word1 = u"ردّ"
        word2=u"ردَّ"
        self.assertTrue(ar.shaddalike(word1, word2))
                
    def test_joint(self):
        """Test Join function ?"""
        letters = u"العربية"
        marks = u'\u064e\u0652\u064e\u064e\u064e\u064e\u064f'
        self.assertEqual(ar.joint(letters, marks), u"اَلْعَرَبَيَةُ")
    def test_seperate(self):
        """Test Separate function ?"""
        letters = u"العربية"
        marks = u'\u064e\u0652\u064e\u064e\u064e\u064e\u064f'
        word = u"اَلْعَرَبَيَةُ"
        l, m= ar.separate(word)
        
        self.assertEqual(ar.joint(l,m), word)
        self.assertEqual(ar.separate(ar.joint(letters,marks)), (letters,marks))
    
    def test_vocalized_similarity(self):
        """Test vocalized_similarity function ?"""
        word1 = u"ضَربٌ"
        word2 = u"ضَرْبٌ"
        self.assertTrue(ar.vocalizedlike(word1, word2))
        self.assertNotEqual(ar.vocalized_similarity(word1, word2), -2)
        self.assertTrue(ar.vocalized_similarity(word1, word2))
        
    def test_vocalizedlike(self):
        """Test vocalizedlike function ?"""
        word1 = u"ضَربٌ"
        word2 = u"ضَرْبٌ"
        self.assertTrue(ar.vocalizedlike(word1, word2))
        
    def test_normalize_hamza(self):
        """Test normalize_hamzafunction ?"""
        text1 = u"سئل أحد الأئمة"
        text2 = u"سءل ءحد الءءمة"
        self.assertEqual(ar.normalize_hamza(text1), text2)
        
    def test_reduce_tashkeel(self):
        """Test reduce_tashkeel function ?"""
        word1 = u"يُتَسََلَّمْنَ"
        word2 = u"يُتسلّمن"
        self.assertEqual(ar.reduce_tashkeel(word1), word2, msg=u"%s :"%ar.reduce_tashkeel(word1))
        
        
    def test_tokenize(self):
        """Test  tokenize function ?"""
        text1 = u"العربية: لغة جميلة."
        wordlist = [u'العربية',u":", u"لغة", u"جميلة", u"."]
        self.assertEqual(ar.tokenize(text1), wordlist)


if __name__ == '__main__':
    unittest.main()
