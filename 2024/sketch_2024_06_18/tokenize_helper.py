
"""
Functions useful draw source code lines with colors,
to get comments, and also to get multi-line (doc)strings.
"""
import tokenize
import io
from os import path

from parse_ansi_strings import parse_ansi_strings, STYLE

tokenize.DOCSTRING = -tokenize.STRING # some monkeying around

def get_comments(tokens):
    return [token for toktype, token, start, end_, ln
            in tokens if toktype == tokenize.COMMENT]

def get_docstrings(tokens):
    return [token for toktype, token, start, end_, ln
            in tokens if toktype == tokenize.STRING
            and starting_triple_quote(token)]

def starting_triple_quote(s):
    return s.startswith('"' * 3) or s.startswith("'" * 3)

def get_tokens(text_lines):
    """
    A helper to produce a list of "token tuples" using Python's tokenize
    """
    buffer = io.StringIO("".join(text_lines))
    return list(tokenize.generate_tokens(buffer.readline))

def reassemble_tokens(token_tuples, styles={}):
    """
    Gets a list of "tokens tuples" from a tokenized  text
    and returns text styled/colored with ansi escape codes.
    
    The style dict maps tokenize's token-type constants 
    to STYLE dict keys from the parse_ansi_strings helper
    that will in turn inform the ansi formatting to be added.

    """
    lines = []
    current_line = ""
    current_line_number = 1
    current_column = 0
    for tok_type, tok_text, (start_row, start_col), (end_row, end_col), _ in token_tuples:
        # Handle new lines
        while current_line_number < start_row:
            lines.append(current_line)
            current_line = ""
            current_line_number += 1
            current_column = 0
        # Handle spacing
        if current_column < start_col:
            current_line += " " * (start_col - current_column)
            current_column = start_col
        # Add token text to the current line
        if tok_type == tokenize.STRING and starting_triple_quote(tok_text):
            tok_type = tokenize.DOCSTRING
        if e := styles.get(tok_type):
            tok_text = STYLE[e] + tok_text + STYLE['END']
        current_line += tok_text
        current_column = end_col
    lines.append(current_line)
    return "".join(lines)

if __name__ == '__main__':
    """For testing."""
    with open('tokenize_helper.py') as f:
        src_lines = f.readlines()
    tokens = get_tokens(src_lines)
    comments = get_comments(tokens) + get_docstrings(tokens)
    styles = {
        tokenize.COMMENT: 'PURPLE',
        tokenize.STRING: 'BLUE',
        tokenize.DOCSTRING: 'RED',
        }
    print(reassemble_tokens(tokens, styles))
