hacker_profile = {
        "name": "Alice",
        "level": 9,
        "skill": ["Python","C", "Web Security"]
}

print(f"Name: {hacker_profile['name']}, Level: {hacker_profile['level']}, Skills: {', '.join(hacker_profile['skill'])}")

with open("hacker_profile.txt", "w", encoding="utf-8") as file:
    file.write(f"Name: {hacker_profile['name']}\n")
    file.write(f"Level: {hacker_profile['level']}\n")
    file.write(f"Skills: {', '.join(hacker_profile['skill'])}\n")
    
print("Hacker profile saved to hacker_profile.txt")