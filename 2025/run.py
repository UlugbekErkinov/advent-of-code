import sys
import importlib.util
from pathlib import Path

def run_day(day):
    day_path = Path(__file__).parent / str(day)
    main_file = day_path / "main.py"
    input_file = day_path / "input.txt"
    
    if not main_file.exists():
        print(f"Error: Day {day} main.py not found.")
        return
    
    if not input_file.exists():
        print(f"Error: Day {day} input.txt not found.")
        return
    
    spec = importlib.util.spec_from_file_location("solution", main_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    try:
        print("PART 1: {}".format(module.part1(str(input_file))))
        print("PART 2: {}".format(module.part2(str(input_file))))
    except AttributeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_day(sys.argv[1])
    else:
        print("Usage: python run.py <day>")