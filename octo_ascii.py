import math
from typing import Tuple, List, Any
def create_ascii_table(headers: List[str], columns: List[List[Any]],
                       column_sep: str = " | ", header_divider: str = "=") -> Tuple[str, List[str]]:
    # TODO: Get this into a package of its own, it's handy - Octo
    header: str = ""
    max_column_len: int = len(max(columns, key=len))
    content_lengths: List[int] = []
    rows: List[str] = []

    # Generate header
    for i, column in enumerate(columns):
        content_len = len(max([str(i) for i in column] + [headers[i]], key=len))
        content_lengths.append(content_len)
        header += headers[i].ljust(content_len) + column_sep
        column += [''] * (max_column_len - len(column))  # Pad each column to the length of the longest
    header = header[:-len(column_sep)]  # Cut the separator off the end
    header += "\n" + header_divider * math.ceil(len(header) / len(header_divider))  # Separate the header from the body

    # Generate rows
    for n in range(max_column_len):
        # Breaking down this awful, awful line:
        # For each column, extract the right data value, then left-justify it to the correct length for the column
        # Then combine all columns with the separator to finish the row
        rows.append(column_sep.join([str(x[n]).ljust(content_lengths[i]) for i, x in enumerate(columns)]))

    return header, rows

d1,d2 = create_ascii_table(['asdf','xkcd','smbc'], [[1,2,3,4],[4,5,6,4],[2,4,6,3]])
print(d1)
for i in d2:
    print(i)