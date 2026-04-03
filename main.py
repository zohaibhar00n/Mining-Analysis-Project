import csv

def calculate_average_grade(file):
    total_grade = 0
    count = 0
    
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_grade += float(row['grade'])
            count += 1
    
    return total_grade / count if count > 0 else 0

def main():
    avg_grade = calculate_average_grade('data.csv')
    print(f"Average Ore Grade: {avg_grade:.2f}%")

if __name__ == "__main__":
    main()
