def find_flaky_tests(test_results):
    result_map = {}

    # Step 1: Collect results per test case
    for test_id, status in test_results:
        if test_id not in result_map:
            result_map[test_id] = set()
        result_map[test_id].add(status)

    # Step 2: Identify flaky tests
    flaky_tests = []
    for test_id, statuses in result_map.items():
        if len(statuses) > 1:
            flaky_tests.append(test_id)

    return flaky_tests


# Example input
test_data = [
    ('TC_101', 'Pass'),
    ('TC_102', 'Fail'),
    ('TC_103', 'Pass'),
    ('TC_101', 'Fail')
]

print(find_flaky_tests(test_data))