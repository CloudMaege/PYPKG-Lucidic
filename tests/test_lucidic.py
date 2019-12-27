from lucidic import __version__
from lucidic import Lucidic
import pytest

################
# Test Dicts:  #
################
# Construct a simple test dict object
SimpleTestDict = {"Name": "Test Dictionary"}

# Construct a simple nested test dict object
SimpleNestedTestDict = {"Record": {"Name": "Test Dictionary", "Type": "SomeRecordTypeName"}}

# Construct a test dict with None, Null, Nil and empty string values
NullTestDict = {
    "FirstTierKey1": "FirstTierValue",
    "FirstTierKey2": "Null",
    "FirstTierKey3": {
        "SecondTierKey1": "SomeValue",
        "SecondTierKey2": "Nil",
        "SecondTierKey3": "",
        "SecondTierKey4": {
            "ThirdTierKey1": "null",
            "ThirdTierKey2": [
                {"FourthListTierKey1": "nil"},
                {"FourthListTierKey2": ""},
                {"FourthListTierKey3": "FourthListTierValue3"}
            ]
        }
    }
}

# Construct a nested test dict object
NestedDict = {
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

# Construct a nested test dict object for comparison against the first nested dict object.
NestedCompareDict = {
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

# Construct a simple list test object
SimpleList = ["Name", "TestList"]


################################
# Begin Internal Method Tests: #
################################
def test_version():
    '''Test Lucidic Version'''
    assert __version__ == '0.1.2'


def test_init():
    '''Test Lucidic class constructor'''
    
    # Create a copy of the SimpleTestDict (This will allow us to test no modifications to the instantiation source dict.)
    TestDict = SimpleTestDict.copy()
    
    # Set the Lucidic Test Dict Object
    Lucidict = Lucidic(TestDict)
    
    '''Test class constructor:'''
    # Test instantiated class instance with dict specified
    assert(Lucidict.dict == SimpleTestDict)

    # Test to ensure original source dict is not modified
    Lucidict.dict.clear()
    assert(TestDict == SimpleTestDict)
    assert(Lucidict.dict != SimpleTestDict)
    assert(Lucidict.dict != TestDict)
    assert(Lucidict.dict == {})
    
    # Test instantiated class instance with no dict specified
    EmptyLucidict = Lucidic()
    assert(EmptyLucidict.dict == {})

    # Test instantiated class instance with non dict object
    with pytest.raises(AssertionError): LucidictFail = Lucidic(SimpleList)

    '''Clean Up'''
    del TestDict
    del Lucidict
    del EmptyLucidict


def test_results():
    '''Test the internal class _get_results, _set_results, _clear_results methods'''

    # Instantiate Lucidic Object
    Lucidict = Lucidic(SimpleTestDict)

    '''Test Lucidic._set_result, Lucidic._get_result and Lucidic._clear_result method actions'''
    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 0)
    assert(get_results == [])
    set_results = {"Key": "Value"}
    Lucidict._set_results(set_results)
    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 1)
    assert(get_results == [set_results])
    Lucidict._clear_results()
    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 0)
    assert(get_results == [])

    '''Clean Up'''
    del Lucidict
    del get_results
    del set_results


def test_keyword():
    '''Test the internal class _get_keyword, _set_keyword, _clear_keyword methods'''

    # Instantiate Lucidic Object
    Lucidict = Lucidic(SimpleTestDict)

    '''Test expected method assertion exceptions:'''
    # keyword = str
    with pytest.raises(AssertionError): Lucidict._set_keyword(SimpleTestDict)
    
    '''Test Lucidic._set_keyword, Lucidic._get_keyword and Lucidic._clear_keyword method actions'''
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == "")
    set_keyword = "MyKeywordAwesomes"
    Lucidict._set_keyword(set_keyword)
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == set_keyword)
    Lucidict._clear_keyword()
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == "")

    '''Clean Up'''
    del Lucidict
    del get_keyword
    del set_keyword


def test_strict():
    '''Test the internal class get_strict, _set_strict, _unset_strict methods'''

    # Instantiate Lucidic Object
    Lucidict = Lucidic(SimpleTestDict)
    
    '''Test Lucidic._get_strict, Lucidic._set_strict and Lucidic._unset_strict method actions'''
    get_strict = Lucidict._get_strict()
    assert(isinstance(get_strict, bool))
    Lucidict._set_strict()
    get_strict = Lucidict._get_strict()
    assert(isinstance(get_strict, bool))
    assert(get_strict == True)
    Lucidict._unset_strict()
    get_strict = Lucidict._get_strict()
    assert(isinstance(get_strict, bool))
    assert(get_strict == False)

    '''Clean Up'''
    del Lucidict
    del get_strict


def test_set_search_result():
    '''Test the Lucidic Update Results Internal Method'''

    # Set the Lucidic Test Dict Object
    Lucidict = Lucidic(SimpleTestDict)

    '''Test expected method assertion exceptions:'''
    # keypath = list
    with pytest.raises(AssertionError): Lucidict._set_search_result("SimpleList", SimpleTestDict)
    # match = dict
    with pytest.raises(AssertionError): Lucidict._set_search_result(SimpleList, "SimpleTestDict")

    '''Test Lucidic._set_search_result method actions'''
    # Ensure the result list object is empty
    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 0)
    assert(get_results == [])
    
    # Call the method and pass it an empty keypath list, and mock K/V Dict
    Lucidict._set_search_result([], {"Key1": "Value1"})
    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 1)
    assert(isinstance(get_results[0], dict))
    assert(get_results[0] == {'keypath': [], 'match': {'Key1': 'Value1'}})

    # Call the method again and pass it an 1 item keypath list, and mock K/V Dict
    Lucidict._set_search_result(["Key1"], {"SubKey1": "Value2"})
    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 2)
    assert(isinstance(get_results[0], dict))
    assert(get_results[0] == {'keypath': [], 'match': {'Key1': 'Value1'}})
    assert(isinstance(get_results[1], dict))
    assert(get_results[1] == {'keypath': ["Key1"], 'match': {'SubKey1': 'Value2'}})

    '''Clean Up'''
    # Clear the search results, in case we run it later
    Lucidict._clear_results()
    get_results = Lucidict._get_results()
    assert(len(get_results) == 0)
    del get_results
    del Lucidict
    

def test_construct_list_keypath():
    '''Test the Lucidic method that constructs a keypath string that can be appended to the result list from a list item and it's index.'''

    # Set the Lucidic Test Dict Object
    Lucidict = Lucidic(SimpleTestDict)
    
    '''Test expected method assertion exceptions:'''
    # keypath = list
    with pytest.raises(AssertionError): Lucidict._construct_list_keypath("SimpleList", "Key", 0)
    # k = str
    with pytest.raises(AssertionError): Lucidict._construct_list_keypath(SimpleList, ["Key"], 0)
    # list_index = int
    with pytest.raises(AssertionError): Lucidict._construct_list_keypath(SimpleList, "Key", "0")

    '''Test Lucidic._construct_list_keypath method actions'''
    # Test Setting results in the _search_results internal method by calling method with valid parameters.
    list_keypath = Lucidict._construct_list_keypath(SimpleList, "Key1", 0)
    assert(isinstance(list_keypath, list))
    assert(len(list_keypath) == 3)
    assert(list_keypath[0] == "Name")
    assert(list_keypath[1] == "TestList")
    assert(list_keypath[2] == "Key1[0]")

    '''Clean Up'''
    del list_keypath
    del Lucidict
    
    
def test_search_item_match():
    '''Test the Lucidic method that attempts to match the specified keyword with the current list item, or dict key/value'''
    
    # Set the Lucidic Test Dict Object
    Lucidict = Lucidic(SimpleNestedTestDict)

    '''Test expected method assertion exceptions:'''
    # key = str
    with pytest.raises(AssertionError): Lucidict._search_item_match(["Key1"], "Item", SimpleList)
    # value = !dict
    with pytest.raises(AssertionError): Lucidict._search_item_match("Key1", {"Name": "Item"}, SimpleList)
    # value = !list
    with pytest.raises(AssertionError): Lucidict._search_item_match("Key1", ["Item"], SimpleList)
    # keyPath = list
    with pytest.raises(AssertionError): Lucidict._search_item_match("Key1", "Item", "SimpleListObj")
    
    '''Test Lucidic._search_item_match method actions'''
    '''Loose Search Test'''
    # Construct the object test conditions by setting necessary Lucidic attributes.
    get_results = Lucidict._get_results()
    get_strict = Lucidict._get_strict()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 0)
    assert(isinstance(get_strict, bool))
    assert(get_strict == False)
    set_keyword = Lucidict._set_keyword("Name")
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == "Name")

    # Call the search method and validate the expected results.
    # Because we know the dict is a 2 layer dict, write the test to validate it as such
    for k1, v1 in Lucidict.dict.items():
        if isinstance(v1, dict):
            for k2, v2 in v1.items():
                Lucidict._search_item_match(k2, v2, [k1])
        else:
            Lucidict._search_item_match(k1, v1, [])

    # Check the set result list to ensure that the results match accordingly to the passed dict obj.
    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 2)
    assert(isinstance(get_results[0], dict))
    assert(get_results[0] == {'keypath': ["Record"], 'match': {"Name": "Test Dictionary"}})
    assert(isinstance(get_results[1], dict))
    assert(get_results[1] == {'keypath': ["Record"], 'match': {"Type": "SomeRecordTypeName"}})

    '''Exact Search Test'''
    # Reset the _search_results variable to get a fresh result set.
    Lucidict._clear_results()
    # reset the _strict variable to enforce strict match
    Lucidict._set_strict()

    # Call the search method and validate the expected results.
    # Because we know the dict is a 2 layer dict, write the test to validate it as such
    for k1, v1 in Lucidict.dict.items():
        if isinstance(v1, dict):
            for k2, v2 in v1.items():
                Lucidict._search_item_match(k2, v2, [k1])
        else:
            Lucidict._search_item_match(k1, v1, [])

    # Check the set result list to ensure that the results match accordingly to the passed dict obj.
    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 1)
    assert(isinstance(get_results[0], dict))
    assert(get_results[0] == {'keypath': ["Record"], 'match': {"Name": "Test Dictionary"}})

    '''Clean Up'''
    Lucidict._clear_keyword()
    Lucidict._unset_strict()
    Lucidict._clear_results()
    del get_results
    del get_strict
    del get_keyword
    del set_keyword
    del Lucidict


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


def test_replace_null_dict_values():
    '''Test the Lucidic method that attempts to scan the specified dict and replace None, Null, Nil, or Empty String values with a specified default value.'''
    
    # Set the Lucidic Test Dict Object
    NullDict = NullTestDict.copy()
    validDict = Lucidic(NullDict)

    '''Test expected method assertion exceptions:'''
    # Set replace key and value instances to None, this is normally handled via the public method call.
    validDict._replace_key_instance = None
    validDict._replace_value_instance = None

    # dictobj = dict
    with pytest.raises(AssertionError): validDict._replace_null_dict_values("NotaDict", "Undefined")

    validDict._replace_null_dict_values(validDict.dict, "Undefined")
    assert(isinstance(validDict.dict, dict))
    assert(validDict.dict != NullTestDict)
    assert(validDict.dict.get('FirstTierKey2') == validDict._replace_null_str)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey2') == validDict._replace_null_str)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey3') == validDict._replace_null_str)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == validDict._replace_null_str)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == validDict._replace_null_str)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == validDict._replace_null_str)

    # Set the new null replace string (this will replace any found key instances)
    validDict._replace_null_str = "ChangedKey1"
    # Set the key name to be replaced with the replace_null_str if found
    validDict._replace_key_instance = "FourthListTierKey3"
    # Run the method on the dict
    validDict._replace_null_dict_values(validDict.dict)
    # Set a variable to use as a reference to validate that the previously replace values are still in tact.
    confirmVal = "Undefined"
    assert(isinstance(validDict.dict, dict))
    assert(validDict.dict != NullTestDict)
    assert(validDict.dict.get('FirstTierKey2') == confirmVal)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey2') == confirmVal)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey3') == confirmVal)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == confirmVal)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == confirmVal)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == confirmVal)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[2].get(validDict._replace_null_str) == "FourthListTierValue3")
    
    # Test replace value instances
    # Set the new null replace string (this will replace any found key instances)
    validDict._replace_null_str = "ChangedValue1"
    # Set the key name to be replaced with the replace_null_str if found
    validDict._replace_value_instance = "FourthListTierValue3"
    # Run the method on the dict
    validDict._replace_null_dict_values(validDict.dict)
    # Set a variable to use as a reference to validate that the previously replace values are still in tact.
    confirmVal = "Undefined"
    assert(isinstance(validDict.dict, dict))
    assert(validDict.dict != NullTestDict)
    assert(validDict.dict.get('FirstTierKey2') == confirmVal)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey2') == confirmVal)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey3') == confirmVal)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == confirmVal)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == confirmVal)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == confirmVal)
    assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[2].get('ChangedKey1') == validDict._replace_null_str)
    

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


def test_replaceNull():
    '''Test the Lucidic public method that attempts to scan the specified dict and replace None, Null, Nil, or Empty String values with a specified default value.'''
    
    # Set the Lucidic Test Dict Object
    validDict = Lucidic(NullTestDict)
    assert(validDict == NullTestDict)

    '''Test expected method assertion exceptions:'''
    # dictobj = dict
    with pytest.raises(AssertionError): validDict.replaceNull(dictobj = "NotaDict")
    # replace_str = str
    with pytest.raises(AssertionError): validDict.replaceNull(replace_str = ["UnKnown"])
    
    # Assign SanitizedDict as the return target and call the method.
    SanitizedDict = validDict.replaceNull(replace_str = "UnKnown")

    # Check the values of SanitizedDict
    assert(validDict._replace_null_str == "UnKnown")
    assert(isinstance(SanitizedDict, dict))
    assert(SanitizedDict != validDict.dict)
    assert(SanitizedDict.get('FirstTierKey2') == "UnKnown")
    assert(SanitizedDict.get('FirstTierKey3').get('SecondTierKey2') == "UnKnown")
    assert(SanitizedDict.get('FirstTierKey3').get('SecondTierKey3') == "UnKnown")
    assert(SanitizedDict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == "UnKnown")
    assert(SanitizedDict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == "UnKnown")
    assert(SanitizedDict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == "UnKnown")

    # Test replace key instances
    # # Set the new null replace string (this will replace any found key instances)
    # validDict._replace_null_str = "ChangedKey1"
    # # Set the key name to be replaced with the replace_null_str if found
    # validDict._replace_key_instance = "FourthListTierKey3"
    # # Run the method on the dict
    # validDict._replace_null_dict_values(validDict.dict)
    # # Set a variable to use as a reference to validate that the previously replace values are still in tact.
    # confirmVal = "Undefined"
    # assert(isinstance(validDict.dict, dict))
    # assert(validDict.dict != NullTestDict)
    # assert(validDict.dict.get('FirstTierKey2') == confirmVal)
    # assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey2') == confirmVal)
    # assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey3') == confirmVal)
    # assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == confirmVal)
    # assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == confirmVal)
    # assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == confirmVal)
    # assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[2].get(validDict._replace_null_str) == "FourthListTierValue3")
    
    # # Test replace value instances
    # # Set the new null replace string (this will replace any found key instances)
    # validDict._replace_null_str = "ChangedValue1"
    # # Set the key name to be replaced with the replace_null_str if found
    # validDict._replace_value_instance = "FourthListTierValue3"
    # # Run the method on the dict
    # validDict._replace_null_dict_values(validDict.dict)
    # # Set a variable to use as a reference to validate that the previously replace values are still in tact.
    # confirmVal = "Undefined"
    # assert(isinstance(validDict.dict, dict))
    # assert(validDict.dict != NullTestDict)
    # assert(validDict.dict.get('FirstTierKey2') == confirmVal)
    # assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey2') == confirmVal)
    # assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey3') == confirmVal)
    # assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == confirmVal)
    # assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == confirmVal)
    # assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == confirmVal)
    # assert(validDict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[2].get('ChangedKey1') == validDict._replace_null_str)

# def test_replaceKey():

# def test_replaceVal():