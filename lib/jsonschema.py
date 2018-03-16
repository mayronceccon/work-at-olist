from jsonschema import Draft4Validator


class JsonSchema():
    messagesOfErrors = []

    def valid(self, schema, data):
        v = Draft4Validator(schema)
        listErrors = []
        errors = sorted(v.iter_errors(data), key=lambda e: e.path)
        for error in errors:
            listErrors.append(error.message)
        if len(listErrors) > 0:
            self.messagesOfErrors = [listErrors]
            return False
        return True

    def getErrors(self):
        return self.messagesOfErrors
