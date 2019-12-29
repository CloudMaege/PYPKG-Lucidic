from lucidic import __version__
from lucidic import Lucidic
import pytest

################
# Test Dicts:  #
################
# Construct a simple test dict object
def getTestDict(select):
    '''Simple Function to return one of the test dicts below so that each test function gets a clean dict as an object instantiation target.'''

    # Define a simple test dictionary
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
    NestedTestDict = {
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
    NestedCompareTestDict = {
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
    SimpleTestList = ["Name", "TestList"]

    # Based on the selection, return the requested object
    if select == "simple_dict":
        return SimpleTestDict
    elif select == "simple_nested_dict":
        return SimpleNestedTestDict
    elif select == "nested_dict":
        return NestedTestDict
    elif select == "nested_compare_dict":
        return NestedCompareTesetDict
    elif select == "null_dict":
        return NullTestDict
    elif select == "simple_list":
        return SimpleTestList
    else:
        return {}


################################
# Begin Internal Method Tests: #
################################
def test_version():
    '''Test Lucidic Version'''
    assert __version__ == '0.1.2'


def test_init():
    '''Test Lucidic class constructor'''
    
    # Create a copy of the SimpleTestDict (This will allow us to test no modifications to the instantiation source dict.)
    TestDict = getTestDict("simple_dict")
    TestList = getTestDict("simple_list")
    Lucidict = Lucidic(TestDict)
    
    '''Test class constructor:'''
    # Test instantiated class instance with dict specified
    assert(Lucidict.dict == TestDict)

    # Test to ensure original source dict is not modified
    Lucidict.dict.clear()
    assert(TestDict == getTestDict("simple_dict"))
    assert(Lucidict.dict != TestDict)
    assert(Lucidict.dict == {})
    
    # Test instantiated class instance with no dict specified
    EmptyLucidict = Lucidic()
    assert(EmptyLucidict.dict == {})

    # Test instantiated class instance with non dict object
    with pytest.raises(AssertionError): LucidictFail = Lucidic(TestList)

    '''Clean Up'''
    Lucidict._reset_instance()
    del TestDict
    del TestList
    del Lucidict
    del EmptyLucidict


def test_results():
    '''Test the internal class _get_results, _set_results, _clear_results methods'''

   # Set the Lucidic Test Dict Object
    TestDict = getTestDict("simple_dict")
    Lucidict = Lucidic(TestDict)

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
    Lucidict._reset_instance()
    del TestDict
    del Lucidict
    del get_results
    del set_results


def test_keyword():
    '''Test the internal class _get_keyword, _set_keyword, _clear_keyword methods'''

    # Set the Lucidic Test Dict Object
    TestDict = getTestDict("simple_dict")
    Lucidict = Lucidic(TestDict)

    '''Test expected method assertion exceptions:'''
    # keyword = str
    with pytest.raises(AssertionError): Lucidict._set_keyword(TestDict)
    
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
    Lucidict._reset_instance()
    del TestDict
    del Lucidict
    del get_keyword
    del set_keyword


def test_strict():
    '''Test the internal class get_strict, _set_strict, _unset_strict methods'''

    # Set the Lucidic Test Dict Object
    TestDict = getTestDict("simple_dict")
    Lucidict = Lucidic(TestDict)
    
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
    Lucidict._reset_instance()
    del TestDict
    del Lucidict
    del get_strict


def test_rest_instance():
    '''Test the Lucidic Reset Instance Environment Method'''

    # Set the Lucidic Test Dict Object
    TestDict = getTestDict("simple_dict")
    Lucidict = Lucidic(TestDict)

    # Set and Validate values for results, keyword, and strict
    Lucidict._set_strict()
    get_strict = Lucidict._get_strict()
    assert(isinstance(get_strict, bool))
    assert(get_strict == True)

    Lucidict._set_keyword("TestKeyword")
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == "TestKeyword")

    set_results = {"Key": "Value"}
    Lucidict._set_results(set_results)
    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 1)
    assert(get_results == [set_results])

    # Use the reset
    Lucidict._reset_instance()

    # Validate all previously assigned values were removed.
    get_strict = Lucidict._get_strict()
    assert(isinstance(get_strict, bool))
    assert(get_strict == False)

    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == "")

    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 0)
    assert(get_results == [])

    '''Clean Up'''
    Lucidict._reset_instance()
    del TestDict
    del Lucidict
    del get_strict
    del get_keyword
    del set_results
    del get_results


def test_set_search_result():
    '''Test the Lucidic Update Results Internal Method'''

    # Set the Lucidic Test Dict Object
    TestDict = getTestDict("simple_dict")
    TestList = getTestDict("simple_list")
    Lucidict = Lucidic(TestDict)

    '''Test expected method assertion exceptions:'''
    # keypath = list
    with pytest.raises(AssertionError): Lucidict._set_search_result("TestList", TestDict)
    # match = dict
    with pytest.raises(AssertionError): Lucidict._set_search_result(TestList, "TestDict")

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
    Lucidict._reset_instance()
    del TestDict
    del TestList
    del get_results
    del Lucidict
    

def test_construct_list_keypath():
    '''Test the Lucidic method that constructs a keypath string that can be appended to the result list from a list item and it's index.'''

    # Set the Lucidic Test Dict Object
    TestDict = getTestDict("simple_dict")
    TestList = getTestDict("simple_list")
    Lucidict = Lucidic(TestDict)
    
    '''Test expected method assertion exceptions:'''
    # keypath = list
    with pytest.raises(AssertionError): Lucidict._construct_list_keypath("TestList", "Key", 0)
    # k = str
    with pytest.raises(AssertionError): Lucidict._construct_list_keypath(TestList, ["Key"], 0)
    # list_index = int
    with pytest.raises(AssertionError): Lucidict._construct_list_keypath(TestList, "Key", "0")

    '''Test Lucidic._construct_list_keypath method actions'''
    # Test Setting results in the _search_results internal method by calling method with valid parameters.
    list_keypath = Lucidict._construct_list_keypath(TestList, "Key1", 0)
    assert(isinstance(list_keypath, list))
    assert(len(list_keypath) == 3)
    assert(list_keypath[0] == "Name")
    assert(list_keypath[1] == "TestList")
    assert(list_keypath[2] == "Key1[0]")

    '''Clean Up'''
    Lucidict._reset_instance()
    del TestDict
    del TestList
    del list_keypath
    del Lucidict
    
    
def test_search_item_match():
    '''Test the Lucidic method that attempts to match the specified keyword with the current list item, or dict key/value'''
    
    # Set the Lucidic Test Dict Object
    TestDict = getTestDict("simple_nested_dict")
    TestList = getTestDict("simple_list")
    Lucidict = Lucidic(TestDict)

    '''Test expected method assertion exceptions:'''
    # key = str
    with pytest.raises(AssertionError): Lucidict._search_item_match(["Key1"], "Item", TestList)
    # value = !dict
    with pytest.raises(AssertionError): Lucidict._search_item_match("Key1", {"Name": "Item"}, TestList)
    # value = !list
    with pytest.raises(AssertionError): Lucidict._search_item_match("Key1", ["Item"], TestList)
    # keyPath = list
    with pytest.raises(AssertionError): Lucidict._search_item_match("Key1", "Item", "TestList")
    
    '''Test Lucidic._search_item_match method actions'''
    '''Loose Search Test'''
    # Construct the object test conditions by setting necessary Lucidic attributes.
    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 0)

    get_strict = Lucidict._get_strict()
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
    Lucidict._reset_instance()
    del TestDict
    del TestList
    del get_results
    del get_strict
    del get_keyword
    del set_keyword
    del Lucidict


def test_search_recursive_dict():
    '''Test the Lucidic method that attempts to recursively search a python dictionary'''
    
    # Set the Lucidic Test Dict Object
    TestDict = getTestDict("nested_dict")
    TestList = getTestDict("simple_list")
    Lucidict = Lucidic(TestDict)

    '''Test expected method assertion exceptions:'''
    # subdict = dict
    with pytest.raises(AssertionError): Lucidict._search_recursive_dict("TestDict", TestList)
    # keypath = list
    with pytest.raises(AssertionError): Lucidict._search_recursive_dict(TestDict, "TestList")

    '''Test Lucidic._search_recursive_dict method actions'''
    # Set the keypath and keyword variables manually, this happens as part of the public search method call
    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 0)
    
    Lucidict._set_strict()
    get_strict = Lucidict._get_strict()
    assert(isinstance(get_strict, bool))
    assert(get_strict == True)
    
    set_keyword = Lucidict._set_keyword("12345")
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == "12345")

    # Set the search dict method as a mock method so we can validate the recursive call count. 
    Lucidict._search_recursive_dict(Lucidict.dict, [])

    # To validate that the search was successful, we can take a look at the results list.
    get_results = Lucidict._get_results()
    assert(len(get_results) == 3)
    assert(get_results[0] == {'keypath': ['Customers', 'Address'], 'match': {'ZipCode': '12345'}})
    assert(get_results[1] == {'keypath': ['Business[0]', 'Address'], 'match': {'ZipCode': '12345'}})
    assert(get_results[2] == {'keypath': ['Business[0]', 'Address', 'Passcode[0]'], 'match': {'Name': '12345'}})

    '''Clean Up'''
    Lucidict._reset_instance()
    del TestDict
    del TestList
    del get_results
    del get_strict
    del get_keyword
    del set_keyword
    del Lucidict


def test_search_recursive_list():
    '''Test the Lucidic method that attempts to recursively search a python list'''
    
    # Set the Lucidic Test Dict Object
    TestDict = getTestDict("nested_dict")
    TestList = getTestDict("simple_list")
    Lucidict = Lucidic(TestDict)

    '''Test expected method assertion exceptions:'''
    # k = str
    with pytest.raises(AssertionError): Lucidict._search_recursive_list(["parentKey"], TestList, TestList)
    # sublist = list
    with pytest.raises(AssertionError): Lucidict._search_recursive_list("parentKey", "TestList", TestList)
    # keypath = list
    with pytest.raises(AssertionError): Lucidict._search_recursive_list("parentKey", TestList, "TestList")

    '''Test Lucidic._search_recursive_list method actions'''
    # Set the keypath and keyword variables manually, this happens as part of the public search method call
    get_results = Lucidict._get_results()
    assert(isinstance(get_results, list))
    assert(len(get_results) == 0)
    
    Lucidict._set_strict()
    get_strict = Lucidict._get_strict()
    assert(isinstance(get_strict, bool))
    assert(get_strict == True)
    
    set_keyword = Lucidict._set_keyword("Unique")
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == "Unique")
    
    # Set the search dict method as a mock method so we can validate the recursive call count. 
    Lucidict._search_recursive_list("Business", Lucidict.dict.get('Business'), [])

    # To validate that the search was successful, we can take a look at the results list.
    get_results = Lucidict._get_results()
    assert(len(get_results) == 1)
    assert(get_results[0] == {'keypath': ['Business[0]', 'Address', 'TestList[3]', 'TestList[3][2]'], 'match': {'TestList[3][2][2]': 'Unique'}})

    '''Clean Up'''
    Lucidict._reset_instance()
    del TestDict
    del TestList
    del get_results
    del get_strict
    del get_keyword
    del set_keyword
    del Lucidict


def test_replace_null_dict_values():
    '''Test the Lucidic method that attempts to scan the specified dict and replace None, Null, Nil, or Empty String values with a specified default value.'''
    
    # Copy the origin dict as the find null values public method will, and then set the Lucidic Test Dict Object
    TestDict = getTestDict("null_dict")
    Lucidict = Lucidic(TestDict)

    '''Test Lucidic._replace_null_dict_values None, Null, Nil, EmptyString replacement method action'''
    # dictobj = dict
    with pytest.raises(AssertionError): Lucidict._replace_null_dict_values("NotaDict")

    # Set the keyword variables and call the method.
    set_keyword = Lucidict._set_keyword("Undefined")
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == "Undefined")

    # Run the method on the dict
    Lucidict._replace_null_dict_values(Lucidict.dict)
    
    assert(isinstance(Lucidict.dict, dict))
    assert(Lucidict.dict != TestDict)
    ValidateDict = Lucidict.dict
    assert(ValidateDict.get('FirstTierKey2') == get_keyword)
    assert(ValidateDict.get('FirstTierKey3').get('SecondTierKey2') == get_keyword)
    assert(ValidateDict.get('FirstTierKey3').get('SecondTierKey3') == get_keyword)
    assert(ValidateDict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == get_keyword)
    assert(ValidateDict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == get_keyword)
    assert(ValidateDict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == get_keyword)

    del ValidateDict

    '''Test Lucidict._replace_null_dict_values replace key method action'''
    # Testing the key replacement of the following dict: {"FourthListTierKey3": "FourthListTierValue3"}
    
    # key_replace = str
    with pytest.raises(AssertionError): Lucidict._replace_null_dict_values(Lucidict.dict, key_replace=["FourthListTierKey3"])
    
    # Set the keyword variables and call the method.
    set_keyword = Lucidict._set_keyword("ChangedKey1")
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == "ChangedKey1")
    
    # Run the method on the dict
    Lucidict._replace_null_dict_values(Lucidict.dict, key_replace="FourthListTierKey3")
    
    # Set a variable to use as a reference to validate that the previously replace values are still in tact.
    confirmVal = "Undefined"
    assert(isinstance(Lucidict.dict, dict))
    assert(Lucidict.dict != TestDict)
    assert(Lucidict.dict.get('FirstTierKey2') == confirmVal)
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey2') == confirmVal)
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey3') == confirmVal)
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == confirmVal)
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == confirmVal)
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == confirmVal)
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[2].get(get_keyword) == "FourthListTierValue3")
    
    '''Test Lucidic._replace_null_dict_values replace value method action'''
    # Testing the value replacement of the following dict: {"FourthListTierKey3": "FourthListTierValue3"}
    
    # value_replace = str
    with pytest.raises(AssertionError): Lucidict._replace_null_dict_values(Lucidict.dict, value_replace=["FourthListTierKey3"])
    
    # Set the keyword variables and call the method.
    set_keyword = Lucidict._set_keyword("ChangedValue1")
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == "ChangedValue1")
    
    # Run the method on the dict
    Lucidict._replace_null_dict_values(Lucidict.dict, value_replace="FourthListTierValue3")
    
    # Set a variable to use as a reference to validate that the previously replace values are still in tact.
    confirmVal = "Undefined"
    assert(isinstance(Lucidict.dict, dict))
    assert(Lucidict.dict != TestDict)
    assert(Lucidict.dict.get('FirstTierKey2') == confirmVal)
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey2') == confirmVal)
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey3') == confirmVal)
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == confirmVal)
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == confirmVal)
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == confirmVal)
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[2].get('ChangedKey1') == get_keyword)

    '''Clean Up'''
    Lucidict._reset_instance()
    del TestDict
    del get_keyword
    del set_keyword
    del Lucidict
    

################################
# Begin Public Method Tests: #
################################
def test_search():
    '''Test the Lucidic public method that searches through the specified dictionary class instance for a given keyword.'''
    
    # Copy the origin dict as the find null values public method will, and then set the Lucidic Test Dict Object
    TestDict = getTestDict("nested_dict")
    Lucidict = Lucidic(TestDict)

    '''Test expected method assertion exceptions:'''
    # keyword = str
    with pytest.raises(AssertionError): Lucidict.search(["name"], strict=True)
    # strict = bool
    with pytest.raises(AssertionError): Lucidict.search(["name"], strict="True")

    '''Test Lucidict.search method actions'''
    # Perform Loose Search and validate the results
    SearchResults = Lucidict.search("name")
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
    SearchResults = Lucidict.search("Name", strict=True)
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
    SearchResults = Lucidict.search("bogus")
    assert(isinstance(SearchResults, list))
    assert(len(SearchResults) == 0)

    '''Clean Up'''
    Lucidict._reset_instance()
    del TestDict
    del SearchResults
    del Lucidict


def test_replaceNull():
    '''Test the Lucidic public method that attempts to scan the specified dict and replace None, Null, Nil, or Empty String values with a specified default value.'''
    
    # Copy the origin dict as the find null values public method will, and then set the Lucidic Test Dict Object
    TestDict = getTestDict("null_dict")
    Lucidict = Lucidic(TestDict)
    
    assert(Lucidict.dict == TestDict)
    
    '''Test expected method assertion exceptions:'''
    # keyword = str
    with pytest.raises(AssertionError): Lucidict.replaceNull(["UnKnown"])

    # Validate the values of Lucidict.dist before running the key replace method
    assert(isinstance(Lucidict.dict, dict))
    assert(Lucidict.dict == TestDict)
    assert(Lucidict.dict.get('FirstTierKey2') == "Null")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey2') == "Nil")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey3') == "")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == "null")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == "nil")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == "")
    
    # Assign SanitizedDict as the return target and call the method.
    SanitizedDict = Lucidict.replaceNull("UnKnown")

    # Check Keyword Assignment
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == "UnKnown")
    
    # Validate the values of Lucidict.dist after running the key replace method
    assert(isinstance(Lucidict.dict, dict))
    assert(Lucidict.dict == Lucidict.dict)
    assert(Lucidict.dict != TestDict)
    assert(Lucidict.dict.get('FirstTierKey2') == "UnKnown")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey2') == "UnKnown")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey3') == "UnKnown")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == "UnKnown")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == "UnKnown")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == "UnKnown")

    # Validate the values of SanitizedDict after running the key replace method (Should be exact copy of Lucidict.dist)
    assert(isinstance(SanitizedDict, dict))
    assert(SanitizedDict == Lucidict.dict)
    assert(SanitizedDict != TestDict)

    '''Clean Up'''
    Lucidict._reset_instance()
    del TestDict
    del SanitizedDict
    del Lucidict
    del get_keyword


def test_replaceKey():
    '''Test the Lucidic public method that attempts to scan the specified dict and replace any found keys matching the provided key_search to the value specified.'''
    
    # Copy the origin dict as the find null values public method will, and then set the Lucidic Test Dict Object
    TestDict = getTestDict("null_dict")
    Lucidict = Lucidic(TestDict)
    assert(Lucidict.dict == TestDict)

    # Set the test condition vars
    key_search = "FourthListTierKey3"
    replace_value = "ChangedKey1"
    
    '''Test expected method assertion exceptions:'''
    # key_search = str
    with pytest.raises(AssertionError): Lucidict.replaceKey([key_search], replace_value)
    # replace_value = str
    with pytest.raises(AssertionError): Lucidict.replaceKey(key_search, [replace_value])
    
    # Validate the values of before running key replace method
    assert(isinstance(Lucidict.dict, dict))
    assert(Lucidict.dict == TestDict)
    assert(Lucidict.dict.get('FirstTierKey2') == "Null")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey2') == "Nil")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey3') == "")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == "null")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == "nil")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == "")
    assert(key_search in Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[2].keys())
    assert(replace_value not in Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[2].keys())
    
    # Assign SanitizedDict as the return target and call the method.
    KeyReplaceDict = Lucidict.replaceKey(key_search, replace_value)

    # Check Keyword Assignment
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == replace_value)
    
    # Validate the values of KeyReplaceDict after running the replace method
    assert(isinstance(Lucidict.dict, dict))
    assert(Lucidict.dict != TestDict)
    assert(Lucidict.dict.get('FirstTierKey2') == "Null")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey2') == "Nil")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey3') == "")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == "null")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == "nil")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == "")
    assert(replace_value in Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[2].keys())
    assert(key_search not in Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[2].keys())

    # Validate the values of KeyReplaceDict after running the key replace method (Should be exact copy of Lucidict.dist)
    assert(isinstance(KeyReplaceDict, dict))
    assert(KeyReplaceDict == Lucidict.dict)
    assert(KeyReplaceDict != TestDict)

    '''Clean Up'''
    Lucidict._reset_instance()
    del TestDict
    del KeyReplaceDict
    del Lucidict
    del get_keyword
    del key_search
    del replace_value


def test_replaceValue():
    '''Test the Lucidic public method that attempts to scan the specified dict and replace any found key values matching the provided valname to the value specified.'''
    
    # Copy the origin dict as the find null values public method will, and then set the Lucidic Test Dict Object
    TestDict = getTestDict("null_dict")
    Lucidict = Lucidic(TestDict)
    assert(Lucidict.dict == TestDict)

    # Set the test condition vars
    val_search = "FourthListTierValue3"
    replace_value = "ChangedVal1"
    
    '''Test expected method assertion exceptions:'''
    # val_Search = str
    with pytest.raises(AssertionError): Lucidict.replaceKey([val_search], replace_value)
    # value = str
    with pytest.raises(AssertionError): Lucidict.replaceKey(val_search, [replace_value])
    
    # Validate the values of before running key replace method
    assert(isinstance(Lucidict.dict, dict))
    assert(Lucidict.dict == TestDict)
    assert(Lucidict.dict.get('FirstTierKey2') == "Null")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey2') == "Nil")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey3') == "")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == "null")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == "nil")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == "")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[2].get('FourthListTierKey3') == val_search)
    
    # Assign SanitizedDict as the return target and call the method.
    ValReplaceDict = Lucidict.replaceValue(val_search, replace_value)

    # Check Keyword Assignment
    get_keyword = Lucidict._get_keyword()
    assert(isinstance(get_keyword, str))
    assert(get_keyword == replace_value)
    
    # Validate the values of KeyReplaceDict after running the replace method
    assert(isinstance(Lucidict.dict, dict))
    assert(Lucidict.dict != TestDict)
    assert(Lucidict.dict.get('FirstTierKey2') == "Null")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey2') == "Nil")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey3') == "")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey1') == "null")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[0].get('FourthListTierKey1') == "nil")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[1].get('FourthListTierKey2') == "")
    assert(Lucidict.dict.get('FirstTierKey3').get('SecondTierKey4').get('ThirdTierKey2')[2].get('FourthListTierKey3') == replace_value)

    # Validate the values of ValReplaceDict after running the key replace method (Should be exact copy of Lucidict.dist)
    assert(isinstance(ValReplaceDict, dict))
    assert(ValReplaceDict == Lucidict.dict)
    assert(ValReplaceDict != TestDict)

    '''Clean Up'''
    Lucidict._reset_instance()
    del TestDict
    del ValReplaceDict
    del Lucidict
    del get_keyword
    del val_search
    del replace_value
