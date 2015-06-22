import sys
import json
from Draft4StrictValidator import Draft4StrictValidator
from jsonschema import Draft4Validator
from jsonschema import validate
from jsonschema import FormatChecker
from jsonschema import SchemaError
from jsonschema import ValidationError

class JSONDocumentValidator:
    
    def __init__(self,schema, instance):
        self.schema = schema
        self.instance = instance
        
    def validate(self):

        schema = open(self.schema).read()
        schema_obj = json.loads(schema)
        data = open(self.instance).read()
        data_obj = json.loads(data)
        
        result = True
        errors_found = False
        errors = []
        
        try:
            # lazy iterator to capture as many errors in one go
            v = Draft4StrictValidator(schema_obj, format_checker=FormatChecker())
            for error in sorted(v.iter_errors(data_obj), key=str):
                errors.append(error)
            if len(errors) > 0:
                print " ... FAIL"
                # un-comment these if you can't see what is going wrong!
                #for err in errors:
                #    print "\tValidation error: " + err.message
                result = False
            else:
                print " ... PASS"
        except SchemaError as e:
            print " ... EXCEPTION"
            print "\tSchemaError: " + e.message
            return False
        except Exception:
            print " ... EXCEPTION"
            print "\tUnexpected Exception" , sys.exc_info()[0]
            print errors
            result = False
            
        return result

