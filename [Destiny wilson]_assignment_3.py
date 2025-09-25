student_name = "Destiny wilson"
current_gpa = 3.5
study_hours = 20
social_points = 50
stress_level = 70


print("Welcome", student_name, "!")
print("Current GPA:", current_gpa)
print("Study hours:", study_hours)
print("Social Points:", social_points)
print("Stress Level:", stress_level)
print("Choose your couser load:")
print("A) Light (12 Credits)")
print("B) Standard (15 Credits)")
print("C) Heavy (18 Credits)")


choice = input("Your choice: ")


if choice == "A":
    study_hours = 5
    stress_level = 10
    print("You chose a course load thats easier with less stress and study hours!")


elif choice == "B":
    study_hours = 10
    stress_level = 20
    print("You chose a course load thats medium with a but more stress and study hours!")


elif choice == "C":
    study_hours = 15
    stress_level = 30
    print("You chose a course load that is the hardest with lots of stress and study hours.")


else:
    print("You did not choose so you will have Light load.")
    study_hours = 5
    stress_level = 10


study_options = ["Programming", "Math", "English", "History"]
study_choice = input("Your study option: ")


if study_choice in study_options:
    print("You chose", study_choice, "as your study option!")
    
    if study_choice == "Math" or study_choice == "Programming":
        current_gpa += 0.2
        social_points -= 5
    elif study_choice == "English":
        current_gpa += 0.1
        social_points += 5
    else:
        current_gpa += 0.05    
elif study_choice not in study_options: 
    print("No changes to GPA or Social points!")
