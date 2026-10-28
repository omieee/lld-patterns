"""
So if we are calling find_Self function with book id: B412 it should return S5
"""


class PracticeMp1:
    def find_shelf(self, books, book_id) -> str:
        for book in books:
            if book_id == book[0]:
                return book[1]
        return "Not Found"
