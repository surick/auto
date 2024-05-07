import typer
import os
import subprocess
from typing_extensions import Annotated
from rich.progress import Progress, BarColumn, TextColumn, TaskProgressColumn

app = typer.Typer()

base = r"D:\Projects"
branch = "develop"
successlist = ""
failedlist = ""

@app.command()
def deploy(name: str):
    global successlist, failedlist
    print()
    print(f"Deploying {name}...")
    print(f"Base path: {base}")
    print(f"Current branch: {branch}")

    project_path = find_project_path(base, name)
    if project_path is None:
        typer.echo(f"Failed: '{name}'")
        failedlist += f"{name}\n"
        return

    print(f"Project path: {project_path}")
    os.chdir(project_path)
    switch_to_branch(branch)
    #run_maven_command("mvn clean deploy -Dmaven.test.skip=true")
    #os.system("mvn clean deploy -Dmaven.test.skip=true")
    if run_maven_command("mvn clean deploy -Dmaven.test.skip=true"):
        print(f"Success: {name}")
        successlist += f"{name}\n"
    else:
        print(f"Faile Compile: {name}")
        failedlist += f"{name}\n" 


@app.command()
def deployAll(path: Annotated[str, typer.Argument()], env: Annotated[str, typer.Argument()]):
    global base, branch
    base = path
    branch = env
    deployList = "irt-common-redis-starter,irt-common-core,irt-log-api,irt-cfg-api,irt-subject-api,irt-supply-api,irt-rand-api,irt-report-api".split(",")
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn()
    ) as progress:
        task = progress.add_task("[cyan]Deploying progress", total=len(deployList))
        for item in deployList:
            progress.update(task, advance=1)
            deploy(item)
    
    print(f"Processed {len(deployList)} packages.")
    if len(successlist) > 0:
        print(f"Success List: \n{successlist}")
    if len(failedlist) > 0:
        print(f"Failed List: \n{failedlist}")

def find_project_path(base_path: str, project_folder: str) -> str:
    for root, dirs, files in os.walk(base_path):
        if project_folder in dirs:
            return os.path.join(root, project_folder)
    return None

def switch_to_branch(branch_name: str):
    os.system(f"git checkout {branch_name}")
    os.system("git pull")

def run_maven_command(command: str):
    try:
        subprocess.check_output(command, shell=True)
        return True
    except subprocess.CalledProcessError as e:
        return False

if __name__ == "__main__":
    app()