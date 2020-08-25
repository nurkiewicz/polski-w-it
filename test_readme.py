import re

import pytest


@pytest.fixture
def readme():
    with open("README.md", "r", encoding="utf-8") as myfile:
        return [line for line in myfile.readlines() if line[0] == '|']


def english_term(row):
    return row[1:row[1:].find('|')].strip()


@pytest.mark.skip(reason="TODO: skipped after migrating to AsciiDoc")
def test_all_rows_in_table_equal_length(readme):
    assert len(set([len(row) for row in readme])) == 1


@pytest.mark.skip(reason="TODO: skipped after migrating to AsciiDoc")
def test_terms_are_sorted(readme):
    all_english_terms = [english_term(line) for line in readme[2:]]
    assert all_english_terms == sorted(all_english_terms)


@pytest.mark.skip(reason="TODO: skipped after migrating to AsciiDoc")
def test_columns_are_aligned(readme):
    def column_position(row):
        return [m.start() for m in re.finditer('|', row)]

    column_position_in_each_line = [str(column_position(line)) for line in readme]
    assert len(set(column_position_in_each_line)) == 1
