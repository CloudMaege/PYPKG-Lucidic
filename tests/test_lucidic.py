from lucidic import __version__
from lucidic import Lucidic
import pytest

################
# Test Dicts:  #
################
SimpleTestObj = {"Name": "Test Dictionary"}

SimpleNestedTestObj = {"Record": {"Name": "Test Dictionary", "Type": "SomeRecordTypeName"}}

NestedTestObj = {
    "Name": "TestDictionary2",
    "Customers": {
        "Name": "John Doe",
        "Address": {
            "Name": "Home",
            "AliasName": "Home",
            "House": "76",
            "Street": "Totter's Lane",
            "City": "Shoreitch",
            "State": "CA",
            "ZipCode": "12345"
        }
    },
    "Business": [
        {
            "Name": "SomeBusiness",
            "Address": {
                "Name": "Primary",
                "Building": "100",
                "Street": "Totter's Lane",
                "City": "Shoreitch",
                "State": "CA",
                "ZipCode": 12345,
                "Passcode": [
                    { "Name": "12345"},
                    { "Name": "54321"},
                    { "Name": "34512"}
                ],
                "TestList": [
                    "Test",
                    "Name",
                    "In",
                    [
                        "Sub",
                        "Test",
                        [
                            "Sub",
                            "Test",
                            "Unique",
                            "Name"
                        ]
                    ]
                ]
            }
        }
    ]
}

NestedCompareTestObj = {
    "Name": "TestDictionary3",
    "Customers": {
        "Name": "John Doe Jr.",
        "Address": {
            "Name": "Home",
            "House": 76,
            "Street": "Totter's Lane",
            "City": "Shoreitch",
            "State": "NY",
            "ZipCode": 12345
        }
    },
    "Business": [
        {
            "Name": "SomeBusiness",
            "Address": {
                "Name": "Primary",
                "Alias": "PrimaryName",
                "Building": "100",
                "Street": "Totter's Lane",
                "City": "Shoreitch",
                "State": "CA",
                "ZipCode": 54321,
                "Passcode": [
                    { "Name": "12345"},
                    { "Name": "54321"},
                    { "Name": "34512"}
                ],
                "TestList": [
                    "Test",
                    "Name",
                    "In",
                    [
                        "Sub",
                        "Test",
                        [
                            "Sub",
                            "Test",
                            "Unique",
                            "Name"
                        ]
                    ]
                ]
            }
        }
    ]
}

SimpleListObj = ["Name", "TestList"]


################################
# Begin Internal Method Tests: #
################################
def test_version():
    '''Test Lucidic Version'''
    assert __version__ == '0.1.1'


def test_init():
    '''Test Lucidic class constructor'''
    
    # Set the Lucidic Test Dict Object
    validDict = Lucidic(SimpleTestObj)
    
    '''Test class constructor:'''
    # Test instantiated class instance with dict specified
    assert(validDict.dict == SimpleTestObj)

    # Test instantiated class instance with no dict specified
    noDict = Lucidic()
    assert(noDict.dict == {})

    # Test instantiated class instance with non dict object
    with pytest.raises(AssertionError): invalidDict = Lucidic(SimpleListObj)


def test_update_search_results():
    '''Test the Lucidic Update Results Internal Method'''

    # Set the Lucidic Test Dict Object
    validDict = Lucidic(SimpleTestObj)

    '''Test expected method assertion exceptions:'''
    # keypath = list
    with pytest.raises(AssertionError): validDict._update_search_results("SimpleListObj", SimpleTestObj)
    # match = dict
    with pytest.raises(AssertionError): validDict._update_search_results(SimpleListObj, "SimpleTestObj")

    '''Test Lucidic._update_search_results method actions'''
    # Set the _search_results variable as normally, this var is set by calling Lucidic.search()
    validDict._search_results = []
    
    # Test Setting results in the _search_results internal method.
    assert(isinstance(validDict._search_results, list))
    assert(len(validDict._search_results) == 0)
    
    # Call the method and pass it an empty keypath list, and mock K/V Dict
    validDict._update_search_results([], {"Key1": "Value1"})
    assert(isinstance(validDict._search_results, list))
    assert(len(validDict._search_results) == 1)
    assert(isinstance(validDict._search_results[0], dict))
    assert(validDict._search_results[0] == {'keypath': [], 'match': {'Key1': 'Value1'}})

    # Call the method again and pass it an 1 item keypath list, and mock K/V Dict
    validDict._update_search_results(["Key1"], {"SubKey1": "Value2"})
    assert(isinstance(validDict._search_results, list))
    assert(len(validDict._search_results) == 2)
    assert(isinstance(validDict._search_results[0], dict))
    assert(validDict._search_results[0] == {'keypath': [], 'match': {'Key1': 'Value1'}})
    assert(isinstance(validDict._search_results[1], dict))
    assert(validDict._search_results[1] == {'keypath': ["Key1"], 'match': {'SubKey1': 'Value2'}})

    # Clear the search results, in case we run it later
    validDict._search_results.clear()
    

def test_search_set_list_keypath():
    '''Test the Lucidic method that appends an item to the keypath list with a list item and index.'''

    # Set the Lucidic Test Dict Object
    validDict = Lucidic(SimpleTestObj)
    
    '''Test expected method assertion exceptions:'''
    # keypath = list
    with pytest.raises(AssertionError): validDict._search_set_list_keypath("SimpleListObj", "Key", 0)
    # k = str
    with pytest.raises(AssertionError): validDict._search_set_list_keypath(SimpleListObj, ["Key"], 0)
    # list_index = int
    with pytest.raises(AssertionError): validDict._search_set_list_keypath(SimpleListObj, "Key", "0")

    '''Test Lucidic._search_set_list_keypath method actions'''
    # Test Setting results in the _search_results internal method by calling method with valid parameters.
    list_keypath = validDict._search_set_list_keypath(SimpleListObj, "Key1", 0)
    assert(isinstance(list_keypath, list))
    assert(len(list_keypath) == 3)
    assert(list_keypath[0] == "Name")
    assert(list_keypath[1] == "TestList")
    assert(list_keypath[2] == "Key1[0]")
    
    
def test_search_item_match():
    '''Test the Lucidic method that attempts to match the specified keyword with the current list item, or dict key/value'''
    
    # Set the Lucidic Test Dict Object
    validDict = Lucidic(SimpleNestedTestObj)

    '''Test expected method assertion exceptions:'''
    # key = str
    with pytest.raises(AssertionError): validDict._search_item_match(["Key1"], "Item", SimpleListObj)
    # item2eval = !dict
    with pytest.raises(AssertionError): validDict._search_item_match("Key1", {"Name": "Item"}, SimpleListObj)
    # item2eval = !list
    with pytest.raises(AssertionError): validDict._search_item_match("Key1", ["Item"], SimpleListObj)
    # keyPath = list
    with pytest.raises(AssertionError): validDict._search_item_match("Key1", "Item", "SimpleListObj")
    
    '''Test Lucidic._search_item_match method actions'''

    '''Loose Search Test'''
    # Set the _search_results variable as normally, this var is set by calling Lucidic.search()
    validDict._search_results = []
    # Set the _keyword and _strict variables as normally, these vars are set by calling Lucidic.search()
    validDict._keyword = "Name"
    validDict._strict = False

    # Call the search method and validate the expected results.
    # Because we know the dict is a 2 layer dict, write the test to validate it as such
    for k1, v1 in validDict.dict.items():
        if isinstance(v1, dict):
            for k2, v2 in v1.items():
                validDict._search_item_match(k2, v2, [k1])
        else:
            validDict._search_item_match(k1, v1, [])

    # Check the set result list to ensure that the results match accordingly to the passed dict obj.
    assert(isinstance(validDict._search_results, list))
    assert(len(validDict._search_results) == 2)
    assert(isinstance(validDict._search_results[0], dict))
    assert(validDict._search_results[0] == {'keypath': ["Record"], 'match': {"Name": "Test Dictionary"}})
    assert(isinstance(validDict._search_results[1], dict))
    assert(validDict._search_results[1] == {'keypath': ["Record"], 'match': {"Type": "SomeRecordTypeName"}})

    '''Exact Search Test'''
    # Reset the _search_results variable to get a fresh result set.
    validDict._search_results = []
    # reset the _strict variable to enforce strict match
    validDict._strict = True

    # Call the search method and validate the expected results.
    # Because we know the dict is a 2 layer dict, write the test to validate it as such
    for k1, v1 in validDict.dict.items():
        if isinstance(v1, dict):
            for k2, v2 in v1.items():
                validDict._search_item_match(k2, v2, [k1])
        else:
            validDict._search_item_match(k1, v1, [])

    # Check the set result list to ensure that the results match accordingly to the passed dict obj.
    assert(isinstance(validDict._search_results, list))
    assert(len(validDict._search_results) == 1)
    assert(isinstance(validDict._search_results[0], dict))
    assert(validDict._search_results[0] == {'keypath': ["Record"], 'match': {"Name": "Test Dictionary"}})

    # Clear the search results, in case we run it later
    validDict._search_results.clear()


def test_search_recursive_dict():
    '''Test the Lucidic method that attempts to recursively search a python dictionary'''
    
    # Set the Lucidic Test Dict Object
    validDict = Lucidic(NestedTestObj)

    '''Test expected method assertion exceptions:'''
    # subdict = dict
    with pytest.raises(AssertionError): validDict._search_recursive_dict("NestedTestObj", SimpleListObj)
    # keypath = list
    with pytest.raises(AssertionError): validDict._search_recursive_dict(NestedTestObj, "SimpleListObj")

    '''Test Lucidic._search_recursive_dict method actions'''
    # Set the keypath and keyword variables manually, this happens as part of the public search method call
    validDict._search_results = []
    validDict._keypath = []
    validDict._keyword = "12345"
    validDict._strict = True

    # Set the search dict method as a mock method so we can validate the recursive call count. 
    validDict._search_recursive_dict(validDict.dict, validDict._keypath)

    # To validate that the search was successful, we can take a look at the results list.
    assert(len(validDict._search_results) == 3)
    assert(validDict._search_results[0] == {'keypath': ['Customers', 'Address'], 'match': {'ZipCode': '12345'}})
    assert(validDict._search_results[1] == {'keypath': ['Business[0]', 'Address'], 'match': {'ZipCode': '12345'}})
    assert(validDict._search_results[2] == {'keypath': ['Business[0]', 'Address', 'Passcode[0]'], 'match': {'Name': '12345'}})

    # Clear the search results, in case we run it later
    validDict._search_results.clear()


def test_search_recursive_list():
    '''Test the Lucidic method that attempts to recursively search a python list'''
    
    # Set the Lucidic Test Dict Object
    validDict = Lucidic(NestedTestObj)

    '''Test expected method assertion exceptions:'''
    # k = str
    with pytest.raises(AssertionError): validDict._search_recursive_list(["parentKey"], SimpleListObj, SimpleListObj)
    # sublist = list
    with pytest.raises(AssertionError): validDict._search_recursive_list("parentKey", "SimpleListObj", SimpleListObj)
    # keypath = list
    with pytest.raises(AssertionError): validDict._search_recursive_list("parentKey", SimpleListObj, "SimpleListObj")

    '''Test Lucidic._search_recursive_list method actions'''
    # Set the keypath and keyword variables manually, this happens as part of the public search method call
    validDict._search_results = []
    validDict._keypath = []
    validDict._keyword = "Unique"
    validDict._strict = True

    # Set the search dict method as a mock method so we can validate the recursive call count. 
    validDict._search_recursive_list("Business", validDict.dict.get('Business'), validDict._keypath)

    # To validate that the search was successful, we can take a look at the results list.
    assert(len(validDict._search_results) == 1)
    assert(validDict._search_results[0] == {'keypath': ['Business[0]', 'Address', 'TestList[3]', 'TestList[3][2]'], 'match': {'TestList[3][2][2]': 'Unique'}})

    # Clear the search results, in case we run it later
    validDict._search_results.clear()


################################
# Begin Public Method Tests: #
################################
def test_search():
    '''Test the Lucidic public method that searches through the specified dictionary class instance for a given keyword.'''
    
    # Set the Lucidic Test Dict Object
    validDict = Lucidic(NestedTestObj)

    '''Test expected method assertion exceptions:'''
    # keyword = str
    with pytest.raises(AssertionError): validDict.search(["name"], strict=True)
    # strict = bool
    with pytest.raises(AssertionError): validDict.search(["name"], strict="True")

    '''Test Lucidic.search method actions'''
    # Perform Loose Search and validate the results
    SearchResults = validDict.search("name")
    assert(isinstance(SearchResults, list))
    assert(len(SearchResults) == 11)
    assert(SearchResults[0] == {'keypath': [], 'match': {'Name': 'TestDictionary2'}})
    assert(SearchResults[1] == {'keypath': ['Customers'], 'match': {'Name': 'John Doe'}})
    assert(SearchResults[2] == {'keypath': ['Customers', 'Address'], 'match': {'Name': 'Home'}})
    assert(SearchResults[3] == {'keypath': ['Customers', 'Address'], 'match': {'AliasName': 'Home'}})
    assert(SearchResults[4] == {'keypath': ['Business[0]'], 'match': {'Name': 'SomeBusiness'}})
    assert(SearchResults[5] == {'keypath': ['Business[0]', 'Address'], 'match': {'Name': 'Primary'}})
    assert(SearchResults[6] == {'keypath': ['Business[0]', 'Address', 'Passcode[0]'], 'match': {'Name': '12345'}})
    assert(SearchResults[7] == {'keypath': ['Business[0]', 'Address', 'Passcode[1]'], 'match': {'Name': '54321'}})
    assert(SearchResults[8] == {'keypath': ['Business[0]', 'Address', 'Passcode[2]'], 'match': {'Name': '34512'}})
    assert(SearchResults[9] == {'keypath': ['Business[0]', 'Address'], 'match': {'TestList[1]': 'Name'}})
    assert(SearchResults[10] == {'keypath': ['Business[0]', 'Address', 'TestList[3]', 'TestList[3][2]'], 'match': {'TestList[3][2][3]': 'Name'}})

    # Perform Exact Search and validate the results
    SearchResults = validDict.search("Name", strict=True)
    assert(isinstance(SearchResults, list))
    assert(len(SearchResults) == 10)
    assert(SearchResults[0] == {'keypath': [], 'match': {'Name': 'TestDictionary2'}})
    assert(SearchResults[1] == {'keypath': ['Customers'], 'match': {'Name': 'John Doe'}})
    assert(SearchResults[2] == {'keypath': ['Customers', 'Address'], 'match': {'Name': 'Home'}})
    assert(SearchResults[3] == {'keypath': ['Business[0]'], 'match': {'Name': 'SomeBusiness'}})
    assert(SearchResults[4] == {'keypath': ['Business[0]', 'Address'], 'match': {'Name': 'Primary'}})
    assert(SearchResults[5] == {'keypath': ['Business[0]', 'Address', 'Passcode[0]'], 'match': {'Name': '12345'}})
    assert(SearchResults[6] == {'keypath': ['Business[0]', 'Address', 'Passcode[1]'], 'match': {'Name': '54321'}})
    assert(SearchResults[7] == {'keypath': ['Business[0]', 'Address', 'Passcode[2]'], 'match': {'Name': '34512'}})
    assert(SearchResults[8] == {'keypath': ['Business[0]', 'Address'], 'match': {'TestList[1]': 'Name'}})
    assert(SearchResults[9] == {'keypath': ['Business[0]', 'Address', 'TestList[3]', 'TestList[3][2]'], 'match': {'TestList[3][2][3]': 'Name'}})

    # Test No Results
    searchResults = validDict.search("bogus")
    assert(isinstance(validDict._search_results, list))
    assert(len(validDict._search_results) == 0)

