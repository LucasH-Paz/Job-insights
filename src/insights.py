from src.jobs import read


def get_unique_job_types(path):
    data = read(path)

    types = set()
    for job in data:
        types.add(job["job_type"])

    return types


def filter_by_job_type(jobs, job_type):
    result = [job for job in jobs if job["job_type"] == job_type]

    return result


def get_unique_industries(path):
    data = read(path)

    industries = set()
    for job in data:
        if job["industry"]:
            industries.add(job["industry"])

    return industries


def filter_by_industry(jobs, industry):
    result = [job for job in jobs if job["industry"] == industry]

    return result


def get_max_salary(path):
    data = read(path)

    salaries = [
        int(job["max_salary"]) for job in data if job["max_salary"].isdigit()
    ]

    return max(salaries)


def get_min_salary(path):
    data = read(path)

    result = [
        int(job["min_salary"]) for job in data if job["min_salary"].isdigit()
    ]

    return min(result)


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError()
    if (
        type(job["max_salary"]) != int
        or type(job["min_salary"]) != int
        or job["min_salary"] > job["max_salary"]
        or type(salary) != int
    ):
        raise ValueError()
    else:
        return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    result = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result.append(job)
        except ValueError:
            pass

    return result
