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
#~ import unittest
import sys
sys.path.append('../maskouk')    
sys.path.append('../')    
import maskouk.collocations as msk
import pyarabic.araby as araby
def test():
    mydict = msk.CollocationClass()
    word1 = u"كرة"
    word2 = u"القدم"
    wlist = [word1, word2]
    # test if collocation exists
    print("step1:test if wordlist is collocation")
    results = mydict.is_collocated(wlist)
    print("inuput:", wlist)
    print("output:",results)
    wlist = [u"شمس", u"النهار"]
    results = mydict.is_collocated(wlist)
    print("inuput:", wlist)
    print("output:",results)
    # get all collocations for a specific word
    
    print("step2:get all collocations for a specific word")
    results  = mydict.is_collocated_word(word1)
    print(word1, results)
    print("step3:get all collocations for a specific word")
    word = u"بيت"
    # get all collocations for a specific word
    results  = mydict.is_collocated_word(word)
    print("inuput:", word)
    print("output:",results)
    # detect collocations in phrase    
    print("step4: detect collocations in phrase")
    text = u"لعبنا مباراة كرة القدم في بيت المقدس"
    wordlist = araby.tokenize(text)

    results  = mydict.ngramfinder(2, wordlist)
    print("inuput:", text)
    print("output:",results)
    # detect collocations in phrase    
    print("step4.1: detect collocations in phrase")
    text = u"لعبنا مباراة كرة القدم في بيت المقدس"
    wordlist = araby.tokenize(text)
    results   = mydict.lookup(wordlist)
    print("inuput:", text)
    print("output:",results)
    # get Long collocations
    print("step5: long collocations")
    text = u" قلت لهم السلام عليكم ورحمة الله تعالى وبركاته ثم رجعت"

    results  = mydict.lookup4long_collocations(text)
    print("inuput:", text)
    print("output:",results)   
    # get Long collocations
    print("step5-b: long collocations")
    text = u" قلت لهم السلام عليكم ورحمة الله تعالى وبركاته ثم رجعت"
    results  = mydict.lookup4long_collocations(text)
    print("inuput:", text)
    print("output:",results)   
    print("inpt = u'%s'"%text)
    print("output = u'%s'"%results)   
    # get Long collocations
    print("step6: detect possible collocations")
    text = u"ظهر رئيس الوزراء السيد عبد الملك بن عامر ومعه أمير دولة غرناطة ونهر النيل انطلاق السباق"
    wordlist = araby.tokenize(text)
    previous = "__"
    for wrd in wordlist:
        wlist = [previous, wrd]
        results  = mydict.is_possible_collocation(wlist, lenght = 2)
        print("inuput:", wlist)
        print("output:", results)   
        previous  = wrd
    print("[\n")
    for wrd in wordlist:
        wlist = [previous, wrd]
        results  = mydict.is_possible_collocation(wlist, lenght = 2)
        print("[",wlist, ",", results,"],")
        #~ print("output:", results)   
        previous  = wrd
    print("]")
         
if __name__  ==  '__main__':
    test()
