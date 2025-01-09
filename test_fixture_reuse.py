# GOALS:
# - have a fixture per-class, so that just one fixture object is
#   used for all test functions in the class
# - reuse a shared fixture with custom data

import pytest

g = 0


@pytest.fixture(scope="class")
def setup_db(request):
    global g
    g += 1
    marker_obj = request.node.get_closest_marker("fixt_data")

    data = {"args": marker_obj.args, "kwargs": marker_obj.kwargs, "g": g}
    # populate database and return metadata
    return data


def samples():
    return list(range(1, 5))


@pytest.mark.fixt_data(1, 2, x=3, samples=samples())
@pytest.mark.usefixtures("setup_db")
class Test_ABC:
    def test1(self):
        print("test1")

    def test2(self, setup_db):
        print("test2", setup_db)


def samples():
    return list(range(7, 10))


@pytest.mark.fixt_data(500, 600, y=700, samples=samples())
@pytest.mark.usefixtures("setup_db")
class Test_XYZ:
    def test1(self, setup_db):
        print("test1", setup_db)

    def test2(self, setup_db):
        print("test2", setup_db)


def test_some():
    print("some test")
