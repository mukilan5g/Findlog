import os
from nose.tools import *
import findlog.findlog as findlog


def test_files_in_dir():
    assert findlog.get_files_in_dir(os.getcwd()) == ['setup.py']
    assert findlog.get_files_in_dir(os.getcwd()+'\\testfiles\\empty') == []
	
def test_search_files_by_re():
    assert findlog.search_files_by_re(os.path.abspath('testfiles\\[a-z0-9]*.(p(y))$')) == [os.path.abspath('testfiles\\helloworld.py'),
                                                                                           os.path.abspath('testfiles\\import.py')]
    assert findlog.search_files_by_re(os.path.abspath('testfiles\\[a-z0-9]*.txt$')) == [os.path.abspath('testfiles\\goodbye.txt'),
                                                                                        os.path.abspath('testfiles\\welcome.txt')]
    assert findlog.search_files_by_re(os.path.abspath('testfiles\\^g')) == [os.path.abspath('testfiles\\goodbye.txt')]

def test_files_match_any():
    