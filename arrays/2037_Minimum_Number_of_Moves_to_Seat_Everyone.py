# python 2037_Minimum_Number_of_Moves_to_Seat_Everyone.py
seats = [3, 1, 5]
students = [2, 7, 4]
# Output: 4

sort_seats = sorted(seats)
sort_students = sorted(students)

sum = 0

for seat, student in zip(sort_seats, sort_students):
    sum += student - seat


print(sort_seats, sort_students, sum)
