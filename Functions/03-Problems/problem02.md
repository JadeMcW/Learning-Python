# 📚 Problem 2: Grade Calculator - Part 1: Individual Grade

> **Objective**: Create a function that calculates and handles individual subject grades as part of a larger grade calculation system.

---

## 🎯 Scenario

You need to calculate the average grade for a student. As a first step, let's create a function that handles just **one subject's grade** at a time.

---

## 📋 Requirements & Guidelines

### 🔧 Function Specifications

| Requirement | Details |
|------------|---------|
| **Function Name** | `get_subject_grade` |
| **Parameters** | `subject_name` (string) |
| **Return Value** | The grade entered by the user (integer) |

### 📝 Implementation Steps

1. **📥 User Input**: Use `input()` to prompt the user with:

   ```text
   Enter grade for [subject_name]: 
   ```

2. **🔢 Input Validation** *(Hint)*:
   - Grades should be numbers
   - Use `int()` to convert the input
   - **🏆 Extra Challenge**: Implement input validation using a `while` loop with `try-except` block
     > *Note: This advanced feature can be saved for a future session if too complex*

3. **↩️ Function Return**: Return the validated grade

4. **🚫 No Loops Yet**: For this problem, simply call the function a few times (e.g., for "Math" and "Science") and print the returned grades

---

## 💡 Example Output

```text
Enter grade for Math: 85
Grade for Math: 85

Enter grade for Science: 90
Grade for Science: 90
```

---

## 🎯 Success Criteria

- ✅ Function accepts a subject name as parameter
- ✅ Function prompts user for grade input
- ✅ Function returns the entered grade
- ✅ Function works correctly when called multiple times
- ✅ Output matches the expected format
