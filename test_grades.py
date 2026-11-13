from practice import summarize_grades

grades = {
    "Calculus": 78,
    "Academic Literacy": 91,
    "Intro to Information Systems": 85,
    "Python": 100,
    "Statistics": 55,
    "English": 67,
}
original = dict(grades)

r = summarize_grades(grades)
assert r["highest"] == ("Python", 100)
assert r["lowest"] == ("Statistics", 55)
assert round(r["average"], 2) == 79.33
assert r["above_60"] == 5
assert grades == original

r = summarize_grades({"Python": 100})
assert r["highest"] == ("Python", 100)
assert r["lowest"] == ("Python", 100)
assert r["average"] == 100
assert r["above_60"] == 1

r = summarize_grades({"A": 50, "B": 40})
assert r["highest"] == ("A", 50)
assert r["lowest"] == ("B", 40)
assert r["average"] == 45
assert r["above_60"] == 0

r = summarize_grades({"A": 60, "B": 61})
assert r["above_60"] == 1

print(summarize_grades({"A": 90, "B": 90}))
print(summarize_grades({}))
print("All checks passed")