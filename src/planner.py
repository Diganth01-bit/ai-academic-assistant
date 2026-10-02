from datetime import (
    datetime,
    date
)


def calculate_days_remaining(
    exam_date
):

    today = date.today()

    days = (
        exam_date - today
    ).days

    return days


def generate_study_plan(
    subjects,
    exam_date,
    hours_per_day
):

    if not subjects:

        return (
            "Please enter at least "
            "one subject."
        )

    days_remaining = (
        calculate_days_remaining(
            exam_date
        )
    )

    if days_remaining <= 0:

        return (
            "The examination date "
            "must be in the future."
        )

    total_hours = (
        days_remaining *
        hours_per_day
    )

    subject_count = len(
        subjects
    )

    hours_per_subject = (
        total_hours /
        subject_count
    )

    result = []

    result.append(
        "PERSONALIZED STUDY PLAN"
    )

    result.append(
        "=" * 40
    )

    result.append(
        f"Days remaining: "
        f"{days_remaining}"
    )

    result.append(
        f"Available hours/day: "
        f"{hours_per_day}"
    )

    result.append(
        f"Total available hours: "
        f"{total_hours}"
    )

    result.append("")

    result.append(
        "Approximate subject allocation:"
    )

    for subject in subjects:

        result.append(
            f"- {subject}: "
            f"{hours_per_subject:.1f} hours"
        )

    return "\n".join(
        result
    )