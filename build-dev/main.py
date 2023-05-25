import os
from cto_ai import ux, prompt, sdk

def main():
    repo = prompt.input(name="repo", message="Which application do you want to deploy?", allowEmpty=False)

    # Add your workflow code here
    os.system('ls -asl')
    sdk.log('Here is how you can send logs')
    ux.print('Hey there, you are now connected to the server!')
    ux.print(f'🚀 {repo}\'s successful build has been executed!')

    event = {
        "event_name": "build",
        "event_action": "succeeded",
        "branch": "main",
        "repo": repo
    }
    sdk.track([], "", event)


if __name__ == "__main__":
    main()
