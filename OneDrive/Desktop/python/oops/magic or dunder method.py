#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     12-09-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
class Sample:
    def __init__(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages
    def __str__(self):
        return f'{self.name} is writtrn by {self.author} has {self.pages} pages'
    def __len__(self):
        return self.pages
book=Sample('python','rohit',200)
print(book)
print(len(book))