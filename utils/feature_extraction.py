import subprocess
import re
from radon.complexity import cc_visit


# ---------------------------------------------------
# Get latest commit message
# ---------------------------------------------------

def get_latest_commit_message():

    result = subprocess.check_output(
        ["git", "log", "-1", "--pretty=%B"]
    )

    return result.decode("utf-8").strip()


# ---------------------------------------------------
# Extract LOC + Churn + Modified Files
# ---------------------------------------------------

def get_git_diff_metrics():

    result = subprocess.check_output(
        ["git", "show", "--stat", "--oneline", "HEAD"]
    )

    output = result.decode("utf-8")
    print(output)

    files_modified = 0
    insertions = 0
    deletions = 0

    file_match = re.search(r"(\d+) file[s]?", output)

    insert_match = re.search(r"(\d+) insertion[s]?", output)

    delete_match = re.search(r"(\d+) deletion[s]?", output)

    if file_match:
        files_modified = int(file_match.group(1))

    if insert_match:
        insertions = int(insert_match.group(1))

    if delete_match:
        deletions = int(delete_match.group(1))

    loc = insertions + deletions

    churn = loc

    return {

        "loc": loc,

        "churn": churn,

        "files_modified": files_modified
    }


# ---------------------------------------------------
# Commit Frequency
# ---------------------------------------------------

def get_commit_frequency():

    result = subprocess.check_output(
        ["git", "rev-list", "--count", "HEAD"]
    )

    return int(
        result.decode("utf-8").strip()
    )


# ---------------------------------------------------
# Developer Activity
# ---------------------------------------------------

def get_developer_activity():

    result = subprocess.check_output(
        ["git", "log", "--pretty=%an"]
    )

    authors = result.decode("utf-8").splitlines()

    return len(authors)


# ---------------------------------------------------
# Cyclomatic Complexity
# ---------------------------------------------------

def get_complexity(file_path):

    try:

        with open(file_path, "r") as f:

            code = f.read()

        complexity = cc_visit(code)

        if complexity:

            avg_complexity = sum(
                c.complexity for c in complexity
            ) / len(complexity)

            return round(avg_complexity, 2)

        return 1

    except:

        return 1


# ---------------------------------------------------
# Historical Defect Indicators
# ---------------------------------------------------

def get_historical_defects(commit_message):

    risky_keywords = [

        "temporary",

        "workaround",

        "rollback",

        "hotfix",

        "crash",

        "urgent"
    ]

    count = 0

    for word in risky_keywords:

        if word in commit_message.lower():

            count += 1

    return count

# ------------------------------------------------
# Latest modified Python file
# ------------------------------------------------

def get_latest_python_file():

    result = subprocess.check_output(

        [
            "git",
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "-r",
            "HEAD"
        ]
    )

    files = result.decode("utf-8").splitlines()

    for file in files:

        if file.endswith(".py"):

            return file

    return "main.py"