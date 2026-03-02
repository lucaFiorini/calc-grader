from tester import CellPosition, Tester
from bs4 import BeautifulSoup

if __name__ == '__main__':
  with open('test.xhtml') as f:
    tests = Tester(BeautifulSoup(f,"html.parser"))    
    print(tests.is_formula(CellPosition("C",2)))
    
    for cell in CellPosition.Range(CellPosition.From_String("A22"),CellPosition.From_String("B22")):
      