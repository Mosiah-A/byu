with open('w06\hr_system.txt') as system:

    for line in system:
        line = line.split()
        name = line[0]
        id_number = line[1]
        job_title = line[2]
        salary = float(line[3]) / 24

        if job_title.strip() == "Engineer":
            salary += 1000
        
        print(f"Name: {name} (ID: {id_number}), {job_title} - ${salary:.2f}")