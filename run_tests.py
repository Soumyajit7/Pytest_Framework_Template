

import pytest
import sys

def main():
    system_arguments = sys.argv
    try:
        if len(system_arguments) > 1:
            tags = system_arguments[1:]
            for tag in tags:
                print(f"Running tests with tag: {tag}")
                pytest.main(['-m', tag, '-v', f'--html=Reports/Reports_{tag}.html'.format(tag)])
        else:
            pytest.main(['-v', f'--html=Reports/Reports_{tag}.html'])
    except Exception as e:
        print(f"Something went wrong: {e}")
        
        
if __name__ == "__main__":
    main()