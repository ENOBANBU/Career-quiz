import csv

def load_career_data(file_path):
    careers = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            career = {
                'Career': row[0],
                'Science': int(row[1]),
                'Technology': int(row[2]),
                'Art': int(row[3]),
                'Social': int(row[4]),
                'Business': int(row[5]),
                'Nature': int(row[6]),
                'Description': row[7],
                'Average Salary (USD)': float(row[8].replace(',', '')),
                'Education Level': row[9]
            }
            careers.append(career)
    return careers

def run_quiz():
    categories = ['Science', 'Technology', 'Art', 'Social', 'Business', 'Nature']
    scores = {category: 0 for category in categories}
    
    print("Answer the following questions by selecting the best option (A, B, C, etc.):\n")

    print("1. Which activity do you find most interesting?")
    print("A) Conducting experiments\nB) Building gadgets\nC) Creating art\nD) Helping people\nE) Managing a business\nF) Exploring nature")
    answer = input("Your answer: ").upper()
    if answer == 'A':
        scores['Science'] += 1
    elif answer == 'B':
        scores['Technology'] += 1
    elif answer == 'C':
        scores['Art'] += 1
    elif answer == 'D':
        scores['Social'] += 1
    elif answer == 'E':
        scores['Business'] += 1
    elif answer == 'F':
        scores['Nature'] += 1

    print("\n2. What would you enjoy doing in your free time?")
    print("A) Reading scientific articles\nB) Programming or gaming\nC) Designing or crafting\nD) Volunteering at a charity\nE) Learning about stocks or finances\nF) Hiking or observing wildlife")
    answer = input("Your answer: ").upper()
    if answer == 'A':
        scores['Science'] += 1
    elif answer == 'B':
        scores['Technology'] += 1
    elif answer == 'C':
        scores['Art'] += 1
    elif answer == 'D':
        scores['Social'] += 1
    elif answer == 'E':
        scores['Business'] += 1
    elif answer == 'F':
        scores['Nature'] += 1

    print("\n3. Which of these hobbies would you prefer?")
    print("A) Solving complex math problems\nB) Building robots or machines\nC) Drawing, painting, or sculpting\nD) Mentoring or teaching others\nE) Developing business plans\nF) Gardening or taking care of animals")
    answer = input("Your answer: ").upper()
    if answer == 'A':
        scores['Science'] += 1
    elif answer == 'B':
        scores['Technology'] += 1
    elif answer == 'C':
        scores['Art'] += 1
    elif answer == 'D':
        scores['Social'] += 1
    elif answer == 'E':
        scores['Business'] += 1
    elif answer == 'F':
        scores['Nature'] += 1

    print("\n4. If you could choose one of these activities, which would it be?")
    print("A) Researching medical discoveries\nB) Building apps or games\nC) Designing clothes or furniture\nD) Working at a community center\nE) Starting a new company\nF) Working in conservation or environmental protection")
    answer = input("Your answer: ").upper()
    if answer == 'A':
        scores['Science'] += 1
    elif answer == 'B':
        scores['Technology'] += 1
    elif answer == 'C':
        scores['Art'] += 1
    elif answer == 'D':
        scores['Social'] += 1
    elif answer == 'E':
        scores['Business'] += 1
    elif answer == 'F':
        scores['Nature'] += 1

    print("\n5. What type of work environment would you prefer?")
    print("A) A lab or research center\nB) A tech startup\nC) An art studio\nD) A nonprofit organization\nE) A corporate office\nF) Outdoors, in nature")
    answer = input("Your answer: ").upper()
    if answer == 'A':
        scores['Science'] += 1
    elif answer == 'B':
        scores['Technology'] += 1
    elif answer == 'C':
        scores['Art'] += 1
    elif answer == 'D':
        scores['Social'] += 1
    elif answer == 'E':
        scores['Business'] += 1
    elif answer == 'F':
        scores['Nature'] += 1

    print("\n6. What kind of projects do you find fulfilling?")
    print("A) Conducting scientific research\nB) Creating new software or tools\nC) Designing or decorating spaces\nD) Supporting a local community\nE) Building a profitable company\nF) Working on environmental sustainability")
    answer = input("Your answer: ").upper()
    if answer == 'A':
        scores['Science'] += 1
    elif answer == 'B':
        scores['Technology'] += 1
    elif answer == 'C':
        scores['Art'] += 1
    elif answer == 'D':
        scores['Social'] += 1
    elif answer == 'E':
        scores['Business'] += 1
    elif answer == 'F':
        scores['Nature'] += 1

    return scores

def match_careers(careers, scores):
    best_matches = []
    min_diff = float('inf')
    
    for career in careers:
        diff = sum(abs(scores[category] - career[category]) for category in scores)
        
        if diff < min_diff:
            best_matches = [career]
            min_diff = diff
        elif diff == min_diff:
            best_matches.append(career)
    
    return best_matches

# Main execution flow
if __name__ == "__main__":
    csv_file_path = 'careers.csv'
    careers = load_career_data(csv_file_path)

    quiz_scores = run_quiz()

    best_careers = match_careers(careers, quiz_scores)

    print("\nBased on your answers, you might be interested in these careers:")
    for career in best_careers:
        print(f"Career: {career['Career']}")
        print(f"Description: {career['Description']}")
        print(f"Average Salary: ${career['Average Salary (USD)']:,.2f}")
        print(f"Education Level: {career['Education Level']}\n")
