#Performance Platform onboarding schemas

This repo contains schemas and examples of data records that can be uploaded to the [Performance Platform](https://www.gov.uk/performance) using the [Write API](http://performance-platform.readthedocs.org/en/latest/api/write-api.html)

The purpose is to provide guidance and support to government organisations wanting to automate data upload.

We use the draft 4 spec of [JSON Schema](http://json-schema.org/) though the current schema definitions should be compliant with draft 3.

The platform Write API supports POST of either :

* a single json data record object
* an array of json data record objects of the same type

The schema are described at the single object level to allow record validation rather than 'post' payload validation ... (and enter the chaos of 'oneOf' at the root level of the schema)

##How the repo is structured
```
performanceplatform-onboarding-schema
├── readme.md
├── run_tests.sh
├── schema
│   ├── common
│   │   ├── metric-name
│   │   └── ...
│   ├── service-name
│   ├── ...
│   └── templates
│       ├── event-base-schema.json
│       ├── aggregate-base-schema.json
│       └── snippets
└── tools
    ├── configuration
    │   └── schema-test-config.json
    ├── fixtures
    └── tests
        ├── Draft4StrictValidator.py
        ├── JSONSchemaTests.py
        ├── JSONSchemaValidator.py
        └── JSONDocumentValidator.py
```
Schema are organised in the 'common' or a service specific folder (when the data has service specific tags).
Folders in 'common' are organised by 'metric' and can contain more than one schema.
The 'templates' folder contains a set of 'base' schema and snippets of regularly used tags to use in constructing new schema.
The 'tools' folder contains code, configuration and test json documents.

##Updating and adding schema
Users should always check if a schema in the 'common' folder can be used before requesting/proposing a service specific schema and should as a minimum add a test for a well-formed and valid document.

##Running the tests
Tests can be run from the command line

Assuming you are your 
```
$ ./run_tests.sh
```
The tests check 2 things:

* validate all json documents in the 'schema' folder using strict validation (see Draft4StrictValidator.py)
* run the tests listed in schema-test-config.json to check each document in the  'fixtures' folder against the corresponding schema and check the output against the expected value

##Adding tests
Tests for document validation need to be added to the schema-test-config.json file

Each test is added as a new json object in the file with the following format:
```
{
    "description": "test description - Expected PASS/FAIL",
    "schema": "schema to validate against",
    "instance": "json document to validate",
    "assertion": true/false
}
```
The description is to allow users to understand the intent of the test.  The assertion indicates whether the validation is expected to pass(true) or fail(false).# performanceplatform-onboarding-schemas
