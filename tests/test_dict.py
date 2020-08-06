#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_dict.py
#  
#  Copyright 2018 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )
import unittest
import sys
sys.path.append('../maskouk')    
sys.path.append('../')    
import maskouk.collocations as msk
import pyarabic.araby as araby
class maskoukTestCase(unittest.TestCase):
    """Tests for `maskouk`."""
    def test_is_collocated(self):
        """#### Test if collocation exists in database"""
        mydict = msk.CollocationClass()
        inpt =  ['كرة', 'القدم']
        output=u"كرة القدم"
        self.assertEqual(mydict.is_collocated(inpt), output)
        
        inpt = ['شمس', 'النهار']
        output = False
        self.assertEqual(mydict.is_collocated(inpt), output)
    
    def test_is_collocated_word(self):
        """####Test if a word has collocations in database"""
        mydict = msk.CollocationClass()
        inpt = u"كرة"
        output = {'القدم': 'كُرَة الْقَدَمِ'}
        self.assertEqual(mydict.is_collocated_word(inpt), output)
        
        inpt = u"بيت"
        output = {'العدة': 'بَيْت الْعِدَّةِ', 'المستأجر': 'بَيْت الْمُسْتَأْجِرِ', 'المشتري': 'بَيْتِ الْمُشْتَرِي', 'الرجل': 'بَيْت الرَّجُلِ', 'البناء': 'بَيْت الْبِنَاءِ', 'الزوج': 'بَيْت الزَّوْجِ', 'المال': 'بيت المال', 'المقدس': 'بَيْت الْمَقْدِسِ', 'البائع': 'بَيْت الْبَائِعِ', 'الخلاء': 'بَيْت الْخَلَاءِ', 'الأب': 'بَيْت الْأَبِ', 'الله': 'بَيْت اللّهِ'}
        self.assertEqual(mydict.is_collocated_word(inpt), output)
    
    def test_ngramfinder(self):
        """####Detect collocation in a phrase"""
        mydict = msk.CollocationClass()
        text = u"لعبنا مباراة كرة القدم في بيت المقدس"
        inpt = araby.tokenize(text)
        output = ['لعبنا', 'مباراة', 'كرة القدم', 'في', 'بيت المقدس']
        self.assertEqual(mydict.ngramfinder(2, inpt), output)
    def test_lookup(self):
        """####Detect collocation in a phrase"""
        mydict = msk.CollocationClass()
        text = u"لعبنا مباراة كرة القدم في بيت المقدس"
        inpt = araby.tokenize(text)
        output = (['لعبنا', 'مباراة', 'كُرَة', 'الْقَدَمِ', 'في', 'بَيْت', 'الْمَقْدِسِ'], 
                ['CO', 'CO', 'CB', 'CI', 'CO', 'CB', 'CI'])
        self.assertEqual(mydict.lookup(inpt), output)
        
    def test_lookup4long(self):
        """####detect long collocations in a phrase"""
        mydict = msk.CollocationClass()
        inpt = u' قلت لهم السلام عليكم ورحمة الله تعالى وبركاته ثم رجعت'
        output = u' قلت لهم السّلامُ عَلَيكُمْ وَرَحْمَةُ اللهِ تَعَالَى وبركاته ثم رجعت'

        self.assertEqual(mydict.lookup4long_collocations(inpt), output)
    
    def test_is_possible_collocation(self):
        """####Detect candidate collocations in phrase"""
        mydict = msk.CollocationClass()
        text = u"ظهر رئيس الوزراء السيد عبد الملك بن عامر ومعه أمير دولة غرناطة ونهر النيل انطلاق السباق"
        inputs = [
            [ ['السباق', 'ظهر'] , 100 ],
            [ ['ظهر', 'رئيس'] , 100 ],
            [ ['رئيس', 'الوزراء'] , 100 ],
            [ ['الوزراء', 'السيد'] , 20 ],
            [ ['السيد', 'عبد'] , 100 ],
            [ ['عبد', 'الملك'] , 15 ],
            [ ['الملك', 'بن'] , 100 ],
            [ ['بن', 'عامر'] , 15 ],
            [ ['عامر', 'ومعه'] , 100 ],
            [ ['ومعه', 'أمير'] , 100 ],
            [ ['أمير', 'دولة'] , 100 ],
            [ ['دولة', 'غرناطة'] , 10 ],
            [ ['غرناطة', 'ونهر'] , 100 ],
            [ ['ونهر', 'النيل'] , 100 ],
            [ ['النيل', 'انطلاق'] , 100 ],
            [ ['انطلاق', 'السباق'] , 100 ],
            ]

        outputs = []
        for wlist, output in inputs:
            self.assertEqual(mydict.is_possible_collocation(wlist, length = 2), output)
         
if __name__  ==  '__main__':
    unittest.main()
