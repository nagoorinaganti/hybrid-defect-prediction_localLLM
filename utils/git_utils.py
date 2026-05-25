import subprocess

def get_latest_commit_message():

    try:

        commit_message = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=%B'],
            text=True
        ).strip()

        return commit_message

    except Exception as e:

        print(f"Error reading commit message: {e}")

        return "No commit message found"