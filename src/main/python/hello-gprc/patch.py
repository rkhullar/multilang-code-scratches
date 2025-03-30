import sys
from pathlib import Path

def patch_path() -> None:
    generated_path = Path(__file__).parent / 'protos' / 'generated'
    sys.path.insert(0, str(generated_path))
