# 🧮 Problem 3: Grade Calculator - Part 2: Average Score

> **Objective**: Build upon the previous function to collect multiple grades using loops and calculate the overall average score for all subjects.

---

## 🎯 Scenario

Now that we have a function to get individual subject grades, let's use it to calculate the average for **all subjects** a student is taking.

---

## 📋 Requirements & Guidelines

### 🔗 Prerequisites

- **Must reuse** the `get_subject_grade` function from **Problem 2**

### 🔧 Implementation Specifications

| Component | Details |
|-----------|---------|
| **Subjects List** | Create a list of subject names (e.g., `["Math", "Science", "History", "Art"]`) |
| **Loop Type** | Use a `for` loop to iterate through the subjects list |
| **Data Collection** | Collect grades into a new list called `grades_list` |
| **Calculation** | Calculate average using sum and count of grades |

### 📝 Implementation Steps

1. **📚 Setup Subjects**: Create a list of subject names

   ```python
   subjects = ["Math", "Science", "History", "Art"]
   ```

2. **🔄 Loop Through Subjects**: Use a `for` loop to iterate through your subjects list

3. **📥 Collect Grades** *(Inside the loop)*:
   - Call `get_subject_grade(subject_name)` for each subject
   - Add the returned grade to `grades_list`

4. **🧮 Calculate Average** *(After the loop)*:
   - Calculate the sum of all grades in `grades_list`
   - Divide the sum by the number of grades using `len(grades_list)`

5. **📤 Display Results**:
   - Print the complete `grades_list`
   - Print the calculated `average_grade`

---

## 💡 Example Output

```text
Enter grade for Math: 80
Enter grade for Science: 90
Enter grade for History: 85
Enter grade for Art: 95

Grades entered: [80, 90, 85, 95]
Average grade: 87.5
```

### Simplified Example

> Using fewer subjects for clarity

```text
Enter grade for Math: 80
Enter grade for Science: 90

Grades entered: [80, 90]
Average grade: 85.0
```

---

## 🎯 Success Criteria

- ✅ Successfully reuses `get_subject_grade` function from Problem 2
- ✅ Creates and uses a subjects list
- ✅ Implements `for` loop to iterate through subjects
- ✅ Collects all grades into `grades_list`
- ✅ Correctly calculates sum of all grades
- ✅ Properly calculates average using division
- ✅ Displays both the grades list and final average
- ✅ Handles multiple subjects efficiently
