import sqlite3;
import json;

class Schema:

    String = str();
    Number = float();

    def __init__(self,new_schema=None):
        self.schema = {};
        if new_schema != None:
            if type(new_schema) == str:
                self.schema = json.loads(new_schema);
            elif type(new_schema) == dict:
                self.schema = new_schema
        return;
    
    def __str__(self):
        op_string = json.dumps(self.schema);
        op_string = op_string.replace("\"\"","String");
        op_string = op_string.replace("0.0","Number");
        return(op_string);
    
    def __type__(self):
        return("Schema");

    def setSchema(self,new_schema):
        if type(new_schema) == str:
            self.schema = json.loads(new_schema);
        elif type(new_schema) == dict:
            self.schema = new_schema;

if __name__ == "__main__":

    my_schema = Schema();
    
    my_schema.setSchema({
        "name": Schema.String,
        "age": Schema.Number
    });

    print(my_schema);

    other_schema = Schema({
        "title": Schema.String,
        "author": Schema.String
    });

    print(other_schema);