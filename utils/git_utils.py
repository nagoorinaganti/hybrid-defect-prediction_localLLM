import subprocess


def get_latest_commit_message():

    try:

        commit_message = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=%B'],
            text=True
        ).strip()

        return commit_message

    except Exception as e:

        return "No commit message found"


def get_git_metrics():

    try:

        diff_output = subprocess.check_output(
            ['git', 'diff', '--shortstat', 'HEAD~1'],
            text=True
        )

        files_modified = 1
        loc = 50
        churn = 10

        if "file changed" in diff_output:

            parts = diff_output.split(',')

            files_modified = int(
                parts[0].split()[0]
            )

            insertions = 0
            deletions = 0

            for part in parts:

                if "insertion" in part:

                    insertions = int(
                        part.strip().split()[0]
                    )

                if "deletion" in part:

                    deletions = int(
                        part.strip().split()[0]
                    )

            loc = insertions + deletions

            churn = loc

        return {
            "loc": max(loc, 10),
            "complexity": max(files_modified * 3, 2),
            "churn": churn,
            "commit_frequency": 5,
            "developer_experience": 4,
            "files_modified": files_modified
        }

    except Exception as e:

        print(f"Git metric extraction failed: {e}")

        return {
            "loc": 50,
            "complexity": 5,
            "churn": 10,
            "commit_frequency": 5,
            "developer_experience": 4,
            "files_modified": 1
        }