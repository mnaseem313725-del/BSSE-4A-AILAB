test_cases = [
    [85, True, 90, 5],
    [80, True, 60, 10],
    [80, True, 85, 25],
    [70, True, 75, 19]
]
for i, test in enumerate(test_cases, 1):
    score, doc, att, plag= test
    if (score >= 70 and doc == True
        and att >= 75 and plag< 20):
        actual = "PASS"
    else:
        actual = "FAIL"
    expected = ["PASS", "FAIL", "FAIL", "PASS"][i-1]
    reasons = [
        "conditions satisfied.",
        "Attendance is below 75%.",
        "Plagiarism is above 20%.",
        "Score and attendance meet the minimum limits."
    ]
    print("\nTest Case:", i)
    print("Input:", test)
    print("Expected:", expected)
    print("Actual:", actual)
    print("Reason:", reasons[i-1])
