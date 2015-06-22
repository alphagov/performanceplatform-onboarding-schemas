import unittest
import os
import json
from JSONSchemaValidator import JSONSchemaValidator
from JSONDocumentValidator import JSONDocumentValidator

class JSONSchemaTests(unittest.TestCase):

    def test_schemas(self):
        # Set the directory you want to start from
        rootDir = '../../schema'
        print
        print "SCHEMA CHECK TESTS: " + rootDir
        for dir_name, sub_dir_list, file_list in os.walk(rootDir):
            for file_name in file_list:
                if file_name.endswith(".json"):
                    #assume any json file is a schema
                    print('%s/%s' % (dir_name, file_name)),
                    scheme = JSONSchemaValidator(dir_name,file_name)
                    self.assertTrue(scheme.validate())

    def test_documents(self):
        print
        print "JSON DOCUMENT VALIDATION TESTS: "
        # get the test config
        test_list = open("../configuration/schema-test-config.json").read()
        tests = json.loads(test_list)
        for test in tests:
            print test['instance'] + " : " + test['description'],
            validation = JSONDocumentValidator(test['schema'],test['instance'])
            if test['assertion']:
                self.assertTrue(validation.validate())
            else:
                self.assertFalse(validation.validate())

if __name__ == '__main__':
    unittest.main()
 
