from git import Repo

def git_commit_and_push(commit_message):
    try:
        repo = Repo('.')
        repo.git.add(A=True)
        
        if repo.is_dirty():
            repo.git.commit(m=commit_message)
            print("Changes committed.")
        else:
            print("No changes to commit.")
        
        origin = repo.remote(name='origin')
        origin.push()
        print("Changes pushed.")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    git_commit_and_push("Auto commit")