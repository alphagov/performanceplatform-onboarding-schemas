import sys
import json
from Draft4StrictValidator import Draft4StrictValidator
from jsonschema import Draft4Validator
from jsonschema import SchemaError

class JSONSchemaValidator:
    
    def __init__(self,dir_name, file_name):
        self.dir_name = dir_name
        self.file_name = file_name
        
    def validate(self):
        
        schema_location = self.dir_name + "/" + self.file_name
        #print "Schema location: " + schema_location
        
        # get the schema
        schema = open(schema_location).read()
        #print "Schema: " + schema
        schema_obj = json.loads(schema)
            
        # check the schema object
        try:
            Draft4StrictValidator.check_schema(schema_obj)
            print " ... PASS"
            return True
        except SchemaError as e:
            print " ... FAIL"
            print "\tSchemaError: " + e.message
            return False
        except Exception:
            print " ... FAIL"
            print "\tUnexpected Error" , sys.exc_info()[0]
            return False
