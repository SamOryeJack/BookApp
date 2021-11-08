import ebooklib
from ebooklib import epub

raw = epub.read_epub('app/Redwall_books/Redwall.epub')
book = raw.get_items_of_type(ebooklib.ITEM_DOCUMENT)
# for items in book:
    # print(items)

# print(book.get_metadata('DC','subject'))
# print(type(book.get_items))
# for item in book.get_items():
#     if item.get_type() == ebooklib.ITEM_DOCUMENT:
#         #give names of all 
#         # print(item.get_name())
#         print(item.get_content())


# items = book.get_items_of_type(ebooklib.ITEM_DOCUMENT)
#     test = book.get_item_with_href('OPS/xhtml/chapter_001.html')
#     # print({item.get_content() for item in book.get_items() == ebooklib.ITEM_DOCUMENT})

#     # print(book.get_metadata('DC','subject'))
#     chapters = []
#     for item in book.get_items():
#         if item.get_type() == ebooklib.ITEM_DOCUMENT:

#             print(item.get_name())
#             print('name')
#             chapters.append(item.get_content())
#             #give names of all 
#             # return item.get_name()
#             print(item.get_content())
#             print('here')

#             # return item.get_content()
#             return chapters
# # 'OPS/xhtml/chapter_003.html'