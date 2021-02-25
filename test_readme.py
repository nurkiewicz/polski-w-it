import re

import pytest


@pytest.fixture
def readme():
    with open("README.adoc", "r", encoding="utf-8") as readme:
        return [line for line in readme.readlines() if line[0] == '|']


def english_term(row):
    return row[1:row[1:].find('|')].strip()


@pytest.mark.skip(reason="TODO: skipped after migrating to AsciiDoc")
def test_terms_are_sorted(readme):
    all_english_terms = [english_term(line) for line in readme[2:]]
    assert all_english_terms == sorted(all_english_terms)


def test_does_not_contain_untranslateble_words(readme):
    with open("untranslatable.adoc", "r", encoding="utf-8") as untranslatable:
        untranslateble = [line[1:].strip() for line in untranslatable.readlines() if re.fullmatch('^\\| [a-z ]+\n$', line)]
    for line in readme:
        assert line[1:].strip() not in untranslateble
