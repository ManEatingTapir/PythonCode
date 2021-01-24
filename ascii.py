from typing import List, Any

def _print(value: str):
    """Convenience method. Equivalent of Java's print, does not add a newline to the end."""
    print(value, end='')

def set_num_fields(data: List[List[Any]]) -> int:
    """Returns the highest number of fields for any row in the table."""
    num_fields = 0
    for row in data:
        if len(row) > num_fields:
            num_fields = len(row)
    return num_fields

def set_column_widths(titles) -> List[int]:
    """Uses the first row (assumed to be the titles) to set a consistent column width to use in future rows.
    Returns a list of integers where the ith item is the width of the ith column."""
    column_widths = []
    for title in titles:
        # Ensure title is of type string
        # Add 4 to ensure two spaces on both sides of the word in actual table
        column_widths.append(len(str(title)) + 4)
    return column_widths

def print_cell_horizontal(width: int):
    """Prints everything except the leftmost character of the horizontal border of an ASCII cell."""
    _print(f'{"-":-<{width}}+')

def print_cell_data(word: str, width: int):
    """Prints the section containing data of an ASCII cell. Does not print the leftmost character."""
    _print(f'{word:^{width}}|')

def print_table_horizontal(column_widths: List[int], num_fields: int):
    """Print full horizontal border of a table row and move to next line."""
    # Begin horizontal border
    _print('+')
    for integer in range(num_fields):
        try:
            print_cell_horizontal(column_widths[integer])
        except IndexError as err:
            # A row has more fields than the first row
            # Add default width to list of column widths to prevent another error in draw_row
            column_widths.append(9)
            print_cell_horizontal(column_widths[integer])
    # Move to newline
    print()

def print_table_row(column_widths: List[int], num_fields: int, data: List[Any]):
    """Prints every cell on a row except for the top borders. Moves to the next line as well."""
    # Assume already on newline, begin vertical border
    _print('|')
    # TODO: Turn the data printing into a method that can create multi line cells. - MET
    for integer in range(num_fields):
        try:
            print_cell_data(data[integer], column_widths[integer])
        except IndexError as err:
            # Assumption: at this point, all IndexErrors that could happen in column_widths have been dealt with
            # Therefore this exception occurs when the row has less fields than number of fields.
            print_cell_data('ERROR', column_widths[integer])
    # Move to newline
    print()
    print_table_horizontal(column_widths, num_fields)

def print_table(data: List[List[Any]]):
    """Print full ASCII table based on data passed in."""
    num_fields = set_num_fields(data)
    column_widths = set_column_widths(data[0])
    print_table_horizontal(column_widths, num_fields)
    for row in data:
        print_table_row(column_widths, num_fields, row)

# Sample code
if __name__ == '__main__':
    input = [
        ['asdf','xkcd','smbc'],
        ['asdf','xkcd','smbc','pgte'],
        ['asdf','','xkcd']
    ]
    print_table(input)