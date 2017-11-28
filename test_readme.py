import pytest


@pytest.fixture
def readme():
    with open("README.md", "r", encoding="utf-8") as myfile:
        return [line for line in myfile.readlines() if line[0] == '|']

def english_term(line):
    return line[1:line[1:].find('|')].strip()


def test_all_rows_in_table_equal_length():
    assert len(set([len(row) for row in readme()])) == 1


def test_terms_are_sorted():
    all_english_terms = [english_term(line) for line in readme()[2:]]
    assert all_english_terms == sorted(all_english_terms)