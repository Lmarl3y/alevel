import json
import docx

DOC = "studyperiods.docx"
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

with open(schedule := "schedules.json", "r") as f:
    schedule = json.load(f)

my_schedule = schedule["me"]
their_schedule = schedule["them"]

def extract_study_periods(doc_path):
    doc = docx.Document(DOC)
    study_periods = {
        "Week A": {day: [] for day in days},
        "Week B": {day: [] for day in days}
    }
    week = None

    for table in doc.tables:
        table_text = f" ".join(cell.text for row in table.rows for cell in row.cells)
        if "Week A" in table_text:
            week = "Week A"
        if "Week B" in table_text:
            week = "Week B"
        if "Leighton" not in table_text:
            continue
        if week is None:
            continue
        for r, row in enumerate(table.rows[1:6]):
            day = days[r]
            for c, cell in enumerate(row.cells[1:6], start=1):
                if "Leighton" in cell.text:
                    study_periods[week][day].append(c)
    return study_periods

def get_free_periods(schedule):
    free = {}
    for week in schedule:
        free[week] = {}
        for day in days:
            free[week][day] = [
                i+1 for i,p in enumerate(schedule[week][day]) 
                if p.lower() == "free"
            ]
    return free

def get_study_periods(schedule):
    """Get all non-free periods with their subjects"""
    study = {}
    for week in schedule:
        study[week] = {}
        for day in days:
            study[week][day] = [
                (i+1, p) for i,p in enumerate(schedule[week][day]) 
                if p.lower() != "free"
            ]
    return study

def find_shared(my_free, study, their_free):
    shared = {}
    for week in ["Week A", "Week B"]:
        shared[week] = {}
        for day in days:
           my_available = set(my_free[week][day] + study[week][day])
           their_available = set(their_free[week][day])

           shared_periods = sorted(my_available.intersection(their_available))
           shared[week][day] = shared_periods
    return shared

study_periods = extract_study_periods(DOC)
my_free = get_free_periods(my_schedule)
their_free = get_free_periods(their_schedule)
my_study = get_study_periods(my_schedule)
their_study = get_study_periods(their_schedule)
shared_periods = find_shared(my_free, study_periods, their_free)

def format_schedule(schedule, week, day):
    """Format schedule as period numbers only"""
    return ' '.join([f"P{i+1}:{s[:4]}" for i, s in enumerate(schedule[week][day])])

output = []
output.append("SCHEDULE COMPARISON TABLE\n")

for week in ["Week A", "Week B"]:
    output.append(f"\n{week}")
    output.append("=" * 150)
    output.append(f"{'Day':<12} | {'My Schedule':<40} | {'Their Schedule':<40} | {'My Study':<25} | {'Shared Free':<20}")
    output.append("-" * 150)
    
    for day in days:
        my_sched = format_schedule(my_schedule, week, day)
        their_sched = format_schedule(their_schedule, week, day)
        my_study_str = ', '.join([f"P{p}" for p, _ in my_study[week][day]]) if my_study[week][day] else "None"
        shared_str = ', '.join([f"P{p}" for p in shared_periods[week][day]]) if shared_periods[week][day] else "None"
        
        output.append(f"{day:<12} | {my_sched:<40} | {their_sched:<40} | {my_study_str:<25} | {shared_str:<20}")
    
    output.append("")

# Print to console
for line in output:
    print(line)

# Save to file
with open("schedule_table.txt", "w") as f:
    f.write("\n".join(output))

