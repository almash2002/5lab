resume = ["Almash", "Yerzhanova", "87072801433", "Satbayev University", "Computer Science"]
print("Lastname:", resume[0], "\nName:", resume[1], "\nPhone:", resume[2], "\nUniversity:", resume[3], "\nSpeciality:", resume[4])

resume.append("20 years old")
print("\n", resume)

resumesecond = ["28.07.2002", "020728651302"]
resume.extend(resumesecond)
print("\n", resume)

x = "87072801433"
resume.insert(2, x)
print("\n", resume)

resume.pop(5)
print("\n", resume)

resume.reverse()
print("\n", resume)

resume.clear()
print("\n", resume)