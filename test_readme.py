import re

import pytest


@pytest.fixture
def readme():
    with open("README.adoc", "r", encoding="utf-8") as readme:
        return [line for line in readme.readlines()]


def english_term(row):
    return row[1:row[1:].find('|')].strip()


def test_terms_are_sorted(readme):
    all_english_terms = [tup[1][1:].strip() for tup in zip(readme, readme[1:])
                         if tup[0].strip() == '' and tup[1].startswith('| ')]
    assert list(all_english_terms) == sorted(all_english_terms , key=str.lower)


def test_does_not_contain_untranslateble_words(readme):
    with open("untranslatable.adoc", "r", encoding="utf-8") as untranslatable:
        untranslateble = [line[1:].strip() for line in untranslatable.readlines() if re.fullmatch('^\\| [a-z ]+\n$', line)]
    for line in readme:
        assert line[1:].strip() not in untranslateble
