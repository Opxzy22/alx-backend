#!/usr/bin/env python3
"""
a function that returns a calculated start and end indexes
"""
import csv
import math
from typing import List
import os


def index_range(page: int, page_size: int) -> tuple:
    """
        it adjust the page number to be indexed 0
        start_index: calculates the start index for the given
        page and page_size
        end_index: calculates the start index for the given page and page_size
        returns a tuple containing the calculated start and end indexes
    """
    page -= 1
    start_index = page * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = os.path.join(os.path.dirname(__file__),
                             "Popular_Baby_Names.csv")

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
             get the specified page with the documents
        Args:
            page (int, optional): the page number to display. Defaults to 1.
            page_size (int, optional): the size of document. Defaults to 10.
        Returns:
            List[List]: the document
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start_index, end_index = index_range(page, page_size)
        if start_index > len(self.dataset())
        or end_index > len(self.dataset()):
            return []

        return self.__dataset[start_index:end_index]
