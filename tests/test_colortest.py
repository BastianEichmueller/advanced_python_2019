
import pytest
import sys, os
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# EOBlock

import playground

def test_find_peaks():
    peaks = playground.colortest.find_peaks([(1,1,1),(0,0,0),(1,1,1)])
    assert peaks == [1]  
    
def test_find_two_peaks():
    peaks = playground.colortest.find_peaks([(1,1,1),(0,0,0),(1,1,1),(0,0,0),(1,1,1)])
    assert peaks == [1, 3]

def test_find_peaks_max_edge():
    peaks = playground.colortest.find_peaks([(1,1,1),(0,0,0)])
    assert peaks == [] 
    
def test_find_peaks_empty_list():
    peaks = playground.colortest.find_peaks([])
    assert peaks == [] 
