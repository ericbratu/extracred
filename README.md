# EC Assignment

## How to Run/Test

1. Download the .py file
2. Copy and paste the code below into the bottom of the code in the .py file to test all of the implemented functions similar to how Figure 2 in the assignment instructions tests it:

**Function Test Code:**

 ```
db = InMemoryDB()

print(db.get("A"))

try:
    db.put("A", 5)
except Exception as e:
    print(e)


db.begin_transaction()

db.put("A", 5)


print(db.get("A"))


db.put("A", 6)

db.commit()


print(db.get("A"))


try:
    db.commit()
except Exception as e:
    print(e)


try:
    db.rollback()
except Exception as e:
    print(e)


print(db.get("B"))


db.begin_transaction()


db.put("B", 10)


db.rollback()


print(db.get("B"))
   ```



---

## Write-Up

The templates/figures in this assignment should be in a language familiar with most students, such as Python. Java is confusing to most people since it is not as readable as languages like Python or C++. If you want the functions to be tested seperately in its own file, perhaps mention it in the assignment details so that students don't need to have any "set=up" steps and the graders can just run the test file. The grading scale currently seems effective. No other complaints.
