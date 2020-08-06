Maskouk-pysqlite مكتبة مسكوك
============================

Arabic collocations library and data for Python +SQLite API |maskouk
logo|

|downloads| |downloads2|

Developpers: Taha Zerrouki: http://tahadz.com taha dot zerrouki at gmail
dot com

+---------+------------------------------------------------------------------+
| Feature | value                                                            |
| s       |                                                                  |
+=========+==================================================================+
| Authors | `Authors.md <https://github.com/linuxscout/maskouk-pysqlite/mast |
|         | er/AUTHORS.md>`__                                                |
+---------+------------------------------------------------------------------+
| Release | 0.1                                                              |
+---------+------------------------------------------------------------------+
| License | `GPL <https://github.com/linuxscout/maskouk-pysqlite/master/LICE |
|         | NSE>`__                                                          |
+---------+------------------------------------------------------------------+
| Tracker | `linuxscout/maskouk/Issues <https://github.com/linuxscout/maskou |
|         | k-pysqlite/issues>`__                                            |
+---------+------------------------------------------------------------------+
| Website | `http://maskouk.sourceforge.net <http://maskouk-pysqlite.sourcef |
|         | orge.net>`__                                                     |
+---------+------------------------------------------------------------------+
| Source  | `Github <http://github.com/linuxscout/maskouk-pysqlite>`__       |
+---------+------------------------------------------------------------------+
| Downloa | `sourceforge <http://maskouk.sourceforge.net>`__                 |
| d       |                                                                  |
+---------+------------------------------------------------------------------+
| Feedbac | `Comments <https://github.com/linuxscout/maskouk-pysqlite/>`__   |
| ks      |                                                                  |
+---------+------------------------------------------------------------------+
| Account | [@Twitter](https://twitter.com/linuxscout)                       |
| s       | [@Sourceforge](http://sourceforge.net/projects/maskouk/)         |
+---------+------------------------------------------------------------------+

Description
-----------

Maskouk is a database of arab ic collocations extracted from Wikipedia.

Arabic wikipedia data base 2011-Jun-21.

install
~~~~~~~

.. code:: shell

    pip install maskouk-pysqlite

Usage
~~~~~

import
^^^^^^

.. code:: python

    >>> import pyarabic.araby as araby
    >>> import maskouk.collocations as msk
    >>> mydict = msk.CollocationClass()

Test if collocation exists in database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    >>> wlist = [u"كرة", u"القدم"]
    >>> # test if collocation exists
    >>> results = mydict.is_collocated(wlist)
    >>> print("inuput:", wlist)
    >>> print("output:",results)
    inuput: ['كرة', 'القدم']
    output: كرة القدم
    >>> wlist = [u"شمس", u"النهار"]
    >>> results = mydict.is_collocated(wlist)
    >>> print("inuput:", wlist)
    >>> print("output:",results)
    inuput: ['شمس', 'النهار']
    output: False

Test if a word has collocations in database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    >>> # get all collocations for a specific word
    >>> word1 = u"كرة"
    >>> results  = mydict.is_collocated_word(word1)
    >>> print("inuput:", word1)
    >>> print("output:",results)
    inuput: كرة
    output: {'القدم': 'كُرَة الْقَدَمِ'}
    >>>
    >>> word = u"بيت"
    >>> # get all collocations for a specific word
    >>> results  = mydict.is_collocated_word(word)
    >>> print("inuput:", word)
    >>> print("output:",results)
    inuput: بيت
    output: {'العدة': 'بَيْت الْعِدَّةِ', 'المستأجر': 'بَيْت الْمُسْتَأْجِرِ', 'المشتري': 'بَيْتِ الْمُشْتَرِي', 'الرجل': 'بَيْت الرَّجُلِ', 'البناء': 'بَيْت الْبِنَاءِ', 'الزوج': 'بَيْت الزَّوْجِ', 'المال': 'بيت المال', 'المقدس': 'بَيْت الْمَقْدِسِ', 'البائع': 'بَيْت الْبَائِعِ', 'الخلاء': 'بَيْت الْخَلَاءِ', 'الأب': 'بَيْت الْأَبِ', 'الله': 'بَيْت اللّهِ'}

Detect collocation in a phrase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It can be presented asseparated lists or tagged forms

.. code:: python

    >>> # detect collocations in phrase    
    >>> text = u"لعبنا مباراة كرة القدم في بيت المقدس"
    >>> wordlist = araby.tokenize(text)
    >>> results  = mydict.ngramfinder(2, wordlist)
    >>> print("inuput:", text)
    >>> print("output:",results)
    inuput: لعبنا مباراة كرة القدم في بيت المقدس
    output: ['لعبنا', 'مباراة', 'كرة القدم', 'في', 'بيت المقدس']
    >>> # detect collocations in phrase    
    >>> text = u"لعبنا مباراة كرة القدم في بيت المقدس"
    >>> wordlist = araby.tokenize(text)
    >>> results   = mydict.lookup(wordlist)
    >>> print("inuput:", text)
    >>> print("output:",results)
    inuput: لعبنا مباراة كرة القدم في بيت المقدس
    output: (['لعبنا', 'مباراة', 'كُرَة', 'الْقَدَمِ', 'في', 'بَيْت', 'الْمَقْدِسِ'], ['CO', 'CO', 'CB', 'CI', 'CO', 'CB', 'CI'])
    >>> 

detect long collocations in a phrase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some collocations are too long to be used in a bigrams database like
"بسم الله الرحمن الرحيم" "السلام عليكم ورحمة الله وبركاته" "أهلا وسهلا
بكم"

.. code:: python

    >>> # get Long collocations
    ... text = u" قلت لهم السلام عليكم ورحمة الله تعالى وبركاته ثم رجعت"
    >>> results  = mydict.lookup4long_collocations(text)
    >>> print("inuput:", text)
    inuput:  قلت لهم السلام عليكم ورحمة الله تعالى وبركاته ثم رجعت
    >>> print("output:",results)   
    output:  قلت لهم السّلامُ عَلَيكُمْ وَرَحْمَةُ اللهِ تَعَالَى وبركاته ثم رجعت

Detect candidate collocations in phrase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The candidate collocation doesn't exists in the database, this feature
is used to extract collocations based on rules. It returns a rule code,
100 as default (no collocation)

.. code:: python

    >>> text = u"ظهر رئيس الوزراء السيد عبد الملك بن عامر ومعه أمير دولة غرناطة ونهر النيل انطلاق السباق"
    >>> wordlist = araby.tokenize(text)
    >>> previous = "__"
    >>> for wrd in wordlist:
    ...     wlist = [previous, wrd]
    ...     results  = mydict.is_possible_collocation(wlist, lenght = 2)
    ...     print("inuput:", wlist)
    ...     print("output:", results)   
    ...     previous  = wrd
    ... 
    inuput: ['__', 'ظهر']
    output: 100
    inuput: ['ظهر', 'رئيس']
    output: 100
    inuput: ['رئيس', 'الوزراء']
    output: 100
    inuput: ['الوزراء', 'السيد']
    output: 20
    inuput: ['السيد', 'عبد']
    output: 100
    inuput: ['عبد', 'الملك']
    output: 15
    inuput: ['الملك', 'بن']
    output: 100
    inuput: ['بن', 'عامر']
    output: 15
    inuput: ['عامر', 'ومعه']
    output: 100
    inuput: ['ومعه', 'أمير']
    output: 100
    inuput: ['أمير', 'دولة']
    output: 100
    inuput: ['دولة', 'غرناطة']
    output: 10
    inuput: ['غرناطة', 'ونهر']
    output: 100
    inuput: ['ونهر', 'النيل']
    output: 100
    inuput: ['النيل', 'انطلاق']
    output: 100
    inuput: ['انطلاق', 'السباق']
    output: 100
    >>> 

[requirement]
^^^^^^^^^^^^^

::

    1- pyarabic 
    2. sqlite

Data Structure:
---------------

Colocations database
~~~~~~~~~~~~~~~~~~~~

.. code:: sql

    CREATE TABLE "collocations" (
        "id" INTEGER PRIMARY KEY  NOT NULL , 
        "vocalized" VARCHAR,
        "unvocalized" VARCHAR,
        "rule" VARCHAR, 
        "category" VARCHAR, 
        "note" VARCHAR,
        "first" VARCHAR,
        "second" VARCHAR
        );

CSV Structure:

1. id : id unique in the database
2. vocalized : vocalized collocation
3. unvocalized : unvocalized collocation
4. rule : the extraction rule number
5. category : collocation category
6. note :
7. first: first word
8. second: second word



.. |maskouk logo| image:: doc/maskouk_header.png
.. |downloads| image:: https://img.shields.io/sourceforge/dt/maskouk.svg
   :target: http://sourceforge.org/projects/maskouk
.. |downloads2| image:: https://img.shields.io/sourceforge/dm/maskouk.svg
   :target: http://sourceforge.org/projects/maskouk
