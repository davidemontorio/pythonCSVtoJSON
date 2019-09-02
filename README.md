# pythonCSVtoJSON
Simple and dirt python script to convert a CSV file to a JSON file.

This script has been created for a quick conversion for the synonyms feature of the AWS Analysis Schemes.
From a dictionary file in a .csv format we needed to build a json file with the following format:
```
{
  "AI": [
    "Artificial Intelligence"
  ],
  "AML": [
    "Anti Money Laundering",
    "Anti-money laundering"
  ]
}
```

The script reads the dict.csv file and, as a result, create a dict.json file
