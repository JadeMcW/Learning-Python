# 👟 Problem 1: Daily Steps Tracker

> **Objective**: Learn how functions can process data collected over time using loops to track and accumulate daily step counts.

---

## 🎯 Scenario

You want to track your daily steps for a week. After each day, you'll record your steps, and the program will tell you how many steps you've accumulated so far.

---

## 📋 Requirements & Guidelines

### 🔧 Function Specifications

| Requirement | Details |
|------------|---------|
| **Function Name** | `calculate_total_steps` |
| **Parameters** | `current_total_steps`, `steps_today` (both integers) |
| **Return Value** | Sum of `current_total_steps` and `steps_today` |

### 📝 Implementation Steps

1. **🔄 Loop Structure**: Use a `for` loop to simulate **7 days** of tracking

2. **📊 Variable Management**:
   - Keep a running `total_steps` variable that starts at **0**
   - Update this variable using your function each day

3. **📥 Daily Input Process** *(Inside the loop)*:
   - Ask the user for `steps_today` using `input()`
   - **Important**: Convert the input to a number using `int()`

4. **🔄 Crucial Step**: Update `total_steps` by:
   - Calling your `calculate_total_steps` function
   - Assigning its returned value back to `total_steps`

5. **📤 Daily Output**: After each day's input, print the current `total_steps`

---

## 💡 Example Output

```text
Day 1: Enter steps for today: 5000
Total steps so far: 5000

Day 2: Enter steps for today: 3000
Total steps so far: 8000

Day 3: Enter steps for today: 7500
Total steps so far: 15500
... (continues for 7 days)
```

---

## 🎯 Success Criteria

- ✅ Function correctly adds current total and daily steps
- ✅ Loop runs for exactly 7 days
- ✅ User input is properly converted to integers
- ✅ Running total is updated using the function each day
- ✅ Daily totals are displayed after each input
- ✅ Program tracks weekly step accumulation accurately
