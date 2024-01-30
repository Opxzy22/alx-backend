#!/usr/bin/env python3
"""
A module that provides pagination functionality for
a database of popular baby names.
"""

import csv
import math
from typing import List, Tuple, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Adjust the page number to be indexed 0.
    Args:
        page (int): Page number (starting from 1).
        page_size (int): Number of items per page.
    Returns:
        Tuple[int, int]: Calculated start and end
        indexes for the given page and page_size.
    """
    page -= 1
    start_index = page * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server object.
        """
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """
        Retrieve the cached dataset.

        Returns:
            List[List[str]]: The dataset containing popular baby names.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Get a specific page of the dataset.

        Args:
            page (int): Page number to retrieve (default is 1).
            page_size (int): Number of items per page (default is 10).

        Returns:
            List[List[str]]: The dataset for the specified page.
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        start_index, end_index = index_range(page, page_size)
        if start_index > len(self.__dataset)
        or end_index > len(self.__dataset):
            return []
        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict[str, Any]:
        """
        Get hypermedia information for the specified page.
        Args:
            page (int): Page number to retrieve (default is 1).
            page_size (int): Number of items per page (default is 10).
        Returns:
            dict: Hypermedia information including page size,
            current page, dataset, next page,
                  previous page, and total number of pages.
        """
        start_index, end_index = index_range(page, page_size)
        page_size = end_index - start_index
        current_page = page
        dataset_page = self.__dataset[start_index:end_index]
        next_page = page + 1 if end_index < len(self.__dataset) else None
        prev_page = current_page - 1 if current_page > 0 else None
        total_pages = math.ceil(len(self.__dataset) / page_size)

        data_dict = {
            "page_size": page_size,
            "page": current_page,
            "data": dataset_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return data_dict
