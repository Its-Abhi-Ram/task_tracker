from models import Task
from datetime import date, timedelta
from collections import Counter

def generate_insights():
    tasks = Task.query.all()
    summary = {}

    priorities = Counter([t.priority for t in tasks if t.status != 'Done'])
    due_soon = [t for t in tasks if t.due_date <= date.today() + timedelta(days=3) and t.status != 'Done']
    busiest_day = Counter([t.due_date for t in tasks if t.status != 'Done']).most_common(1)

    summary['total_open'] = len([t for t in tasks if t.status != 'Done'])
    summary['priority_counts'] = dict(priorities)
    summary['due_soon_count'] = len(due_soon)
    summary['busiest_day'] = busiest_day[0][0].isoformat() if busiest_day else None

    summary['message'] = f"You have {summary['total_open']} open tasks — most are {priorities.most_common(1)[0][0]} priority and {summary['due_soon_count']} are due soon."

    return summary
