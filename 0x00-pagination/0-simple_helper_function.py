#!/usr/bin/env python3
"""
a function that returns a calculated start and end indexes
"""


def index_range(page: int, page_size: int) -> tuple:
    """
        it adjust the page number to be indexed 0
        start_index: calculates the start index for the given
        page and page_size
        end_index: calculates the start index for the given page
        and page_size
        returns a tuple containing the calculated start and end indexes
    """
    page -= 1
    start_index = page * page_size
    end_index = start_index + page_size

    return start_index, end_index
