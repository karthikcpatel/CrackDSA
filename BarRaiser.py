class FlakyTests:

    def find_flaky_tests(self,test_results):

        result_map = {}
        for test_id, status in test_results:
            if test_id not in result_map:
                result_map[test_id] = set()
            result_map[test_id].add(status)

        flaky_tests = []
        for test_id, statutes in result_map.items():
            if len(statutes) > 1:
                flaky_tests.append(test_id)

        return flaky_tests

test_data = [
    ('TC_101', 'Pass'),
    ('TC_102', 'Fail'),
    ('TC_103', 'Pass'),
    ('TC_101', 'Fail')
]
obj = FlakyTests()
output = obj.find_flaky_tests(test_data)
print("The flaky tests are: ", output)