###############
# Imports:
###############
from lucidic import __version__
from lucidic import Lucidic

# Print Version
print("Package Version: {}\n\n".format(__version__))

######################
# Test Dictionaries: #
######################
TESTDICT = {"Name": "TestDictionary"}
TESTDICT2 = {
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
TESTDICT3 = {
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
                        "Name"
                    ]
                ]
            }
        }
    ]
}


# Test Dict Search:
# ==================

# Construct a new object, passing it the dictionary.
print("Test1: Single Tier")
print("------------------")
lucidicTest = Lucidic(TESTDICT)
results = lucidicTest.search("Name")
print("Results Returned: {}".format(len(results)))
for result in results:
    print(result)
print("\n")

print("Test2: Multi-Tier default (strict:false)")
print("----------------------------------------")
lucidicTest2 = Lucidic(TESTDICT2)
results2 = lucidicTest2.search("Name")
print("Results Returned: {}".format(len(results2)))
for result in results2:
    print(result)
print("\n")

print("Test3: Multi-Tier strict:true")
print("-----------------------------")
lucidicTest3 = Lucidic(TESTDICT2)
results3 = lucidicTest3.search("Name", strict=True)
print("Results Returned: {}".format(len(results3)))
for result in results3:
    print(result)
print("\n")

TestDict = {
    "Records": [
        {"Name": "Record1", "Keywords": ["one", "two", "three"]},
        {"Name": "Record2", "Keywords": ["three", "four", "five"]},
        {"Name": "Record3", "Keywords": [
            {"ListItem": "One"},
            {"ListItem": "Two"},
            {"ListItem": "Three"},
            {"ListItem": [["One"], ["One", "Two"], ["One", "Two", "Three"]]}
        ]}
    ]
}
TestDict = Lucidic(TestDict)
print(TestDict.search("Three"))