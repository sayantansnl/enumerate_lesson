from incomplete_main import clean_and_analyze

# Constructing distinct test data profiles
normal_run = [10, 12, -1, 14, 11, 15, 12]
flat_line = [5, 5, 5, 5, 5]
multiple_corrupted = [20, -1, 40, -1, 20, 25, 10]
all_peaks = [10, 20, 10, 30, 15, 40, 20]
edge_corrupted_trap = [10, 15, -1, 5, 8]
empty_or_small = [10, 12]

run_cases = [
    # Format: (input_data, (expected_cleaned_data, expected_peaks))
    (normal_run, ([10, 12, 13, 14, 11, 15, 12], [3, 5])),
    (flat_line, ([5, 5, 5, 5, 5], [])),
]

submit_cases = run_cases + [
    (empty_or_small, ([10, 12], [])),
    (multiple_corrupted, ([20, 30, 40, 30, 20, 25, 10], [2, 5])),
    (all_peaks, ([10, 20, 10, 30, 15, 40, 20], [1, 3, 5])),
    (edge_corrupted_trap, ([10, 15, 10, 5, 8], [1])),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input readings:\n * {input1}")
    print(f"Expected (Cleaned, Peaks): {expected_output}")
    
    # Mutate a copy to avoid passing a reference trap if vanity-sorting/modifying in place
    result = clean_and_analyze(list(input1)) 
    
    print(f"Actual (Cleaned, Peaks):   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
