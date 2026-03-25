from git import Repo

def extract_commit_features():

    repo_path = r"C:\Users\sneha\OneDrive\Documents\cicd_supply_chain_attack_detection"
    repo = Repo(repo_path)

    commits = list(repo.iter_commits())

    if len(commits) == 0:
        print("No commits found")
        return []

    features = []

    for commit in commits:

        file_count = len(commit.stats.files)
        message_length = len(commit.message)
        author_length = len(commit.author.name)

        features.append([file_count, message_length, author_length])

    return features