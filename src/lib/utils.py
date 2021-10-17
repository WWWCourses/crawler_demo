from pathlib import Path

def get_project_folder():
	# project folder is 2 levels above current script path
	script_path = Path(__file__).parent
	return str(Path(script_path).parent.parent)
