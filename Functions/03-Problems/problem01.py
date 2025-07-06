def calculate_total_steps(current_total_steps, steps_today):
   return current_total_steps + steps_today

total_steps = 0

for day in range(1,8):
   today_steps = int(input(f"Day {day}: Enter steps for today: "))

   total_steps = calculate_total_steps(total_steps, today_steps)

   print(f"Total steps so far: {total_steps}")