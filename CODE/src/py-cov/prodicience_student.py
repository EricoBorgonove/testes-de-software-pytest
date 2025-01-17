def evaluate_performance(grade, attendance, projects_completed):
    if grade >= 85:
        if attendance >= 90:
            if projects_completed >= 5:
                return "Excellent"
            else:
                return "Good"
        else:
            return "Average"
    else:
        if attendance < 75:
            return "Poor"
        else:
            return "Needs Improvement"
