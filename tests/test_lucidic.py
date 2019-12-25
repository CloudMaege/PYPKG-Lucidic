from lucidic import __version__
from lucidic import Lucidic


def test_version():
    assert __version__ == '0.1.0'

def test_search():
    # Construct a test single level dictionary
    testDict = {}
    testDict.update(name="Test Dictionary")
    
    # Construct a new object, passing it the dictionary.
    lucidicTest = Lucidic(testDict)
    results = lucidicTest.search("name")
    assert isinstance(results, dict)
    print(results)
