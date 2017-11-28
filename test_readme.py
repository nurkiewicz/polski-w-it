import pytest

@pytest.fixture
def readme():
    with open("README.md", "r", encoding="utf-8") as myfile:
    	return list([line for line in myfile.readlines()])

def test_all_rows_in_table_equal_length():
	rows = [line for line in readme() if line[0] == '|']
	first_row = rows[0]
	assert len(set([len(row) for row in rows])) == 1
