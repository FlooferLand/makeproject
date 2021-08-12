import os
EDITOR = "codium"

# Declaring file contents here since the working directory gets messed up when using open()
# (I think it has something to do with the Batch script i'm running this script with)
template_tasks = """{
	"version": "2.0.0",
	"tasks": [
		{
			"label": "Build",
			"type": "shell",
			"command": "g++",
			"args": [
				"src/*.cpp",
				"-o",
				"bin/{PROJECT_NAME}.exe"
			]
		},
		
		{
			"label": "Run",
			"type": "shell",
			"command": "cd bin; ./{PROJECT_NAME}.exe"
		},
		
		{
			"label": "Build & Run",
			"type": "shell",
			"command": "cd bin; ./{PROJECT_NAME}.exe",
			"dependsOn": ["Build"]
		}
	]
}"""

template_main = """#include <iostream>

int main()
{
	std::cout << "Hello World!" << std::endl;
}"""


# Variables
working_dir = input("Path (where the project will be made): ")


# Quit if project name could be a mistake
if len(working_dir) < 10:  quit("did a cat step on your keyboard?")


# Making the directories
os.mkdir(os.path.join(working_dir, ".vscode"))
os.mkdir(os.path.join(working_dir, "bin"))
os.mkdir(os.path.join(working_dir, "src"))


# Inserting variables into template files
template_tasks = template_tasks.replace(
	"{PROJECT_NAME}",
	os.path.basename(working_dir).replace(' ', '-')
)


# Writting code template files
open(
	os.path.join(working_dir, "src", "Main.cpp"),
	'w'
).write(template_main)

# Writting tasks file
open(
	os.path.join(working_dir, ".vscode", "tasks.json"),
	'w'
).write(template_tasks)


# Opening editor
os.system(f"{EDITOR} \"{working_dir}\"")
