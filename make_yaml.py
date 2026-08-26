import re
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent  # mobile_agentic_testing/ folder

def extract_yaml(response_text: str) -> str:
    text = response_text.strip()
    fence_match = re.search(r"```(?:yaml)?\s*\n(.*?)```", text, re.DOTALL)
    if fence_match:
        text = fence_match.group(1)

    return text.strip()


def save_yaml_flow(response_text: str, filename: str | None = None) -> Path:
    yaml_content = extract_yaml(response_text)
    output_path = OUTPUT_DIR / filename
    output_path.write_text(yaml_content + "\n")
    return output_path