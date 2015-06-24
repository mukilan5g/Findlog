from nose.tools import *
import findlog.findlog as findlog


# def Test_list_all_match():
    # assert set(findlog.list_all_match(['sentence'])) == set(['C:\Users\mukilan\Desktop\ex26.py'])
    # assert set(findlog.list_all_match(['sentence','words'])) == set(['C:\\Users\\mukilan\\Desktop\\ex26.py',
                                                                     # 'C:\\Users\\mukilan\\Desktop\\count.py'])
    # assert set(findlog.list_all_match(['sentence','play'])) == set(['C:\Users\mukilan\Desktop\ex26.py',
                                                                    # 'C:\Users\mukilan\Desktop\hi2.txt'])
    # assert set(findlog.list_all_match([' ','play'])) == set(['C:\Users\mukilan\Desktop\ex26.py',
                                                             # 'C:\Users\mukilan\Desktop\hi2.txt'])
    # print "Matching all patterns is successful"

def test_files_in_dir():
    assert findlog.get_files_in_dir('E:\git\skeleton\src') == ['new_file.txt','setup.py']
    assert findlog.get_files_in_dir('E:\git\skeleton') == []
	
def test_search_files_by_re():
    assert findlog.search_files_by_re(r'E:\git\skeleton\src\[a-z]') == ['E:\\git\\skeleton\\src\\new_file.txt'
                                                                        ,'E:\\git\skeleton\src\setup.py']
    assert findlog.search_files_by_re(r'E:\git\skeleton\src\[a-z]*.(p(y))$') == ['E:\\git\\skeleton\\src\\setup.py']
    assert findlog.search_files_by_re(r'E:\git\skeleton\src\set') == ['E:\\git\\skeleton\\src\\setup.py']

def test_search_files_by_re():
    assert findlog.f.search_files_by_re('C:\Users\mukilan\Desktop\[a-z0-9]*.(p(y))$') == ['C:\\Users\\mukilan\\Desktop\\arith.py',
                                                                                          'C:\\Users\\mukilan\\Desktop\\count.py',
                                                                                          'C:\\Users\\mukilan\\Desktop\\ex26.py',
                                                                                          'C:\\Users\\mukilan\\Desktop\\hello.py',
                                                                                          'C:\\Users\\mukilan\\Desktop\\n.py',
                                                                                          'C:\\Users\\mukilan\\Desktop\\new.py',
                                                                                          'C:\\Users\\mukilan\\Desktop\\test.py']
    
def test_basic():
    print "I RAN!"