from pathlib import Path
import yaml
from jinja2 import Template

BASE_DIR = Path(__file__).parent
PROMPT_DIR = BASE_DIR
CONFIG_PATH = BASE_DIR / "prompt_config.yaml"
DEFAULT_MODE = "maestro_yaml_generator"

def load_config() -> dict:
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


def load_module(name: str) -> str:
    path = PROMPT_DIR / f"{name}.md"
    if not path.exists():
        raise FileNotFoundError(f"Prompt module not found: {path}")
    return path.read_text().strip()


def render_module(raw_text: str, **kwargs) -> str:
    template = Template(raw_text)
    return template.render(**kwargs).strip()


def build_system_prompt(mode: str = DEFAULT_MODE, **kwargs) -> str:
    config = load_config()
    if mode not in config:
        raise ValueError(f"Unknown mode '{mode}'. Available modes: {list(config.keys())}")
    modules = config[mode]
    rendered_parts = []
    for module_name in modules:
        raw = load_module(module_name)
        rendered = render_module(raw, **kwargs)
        if rendered:
            rendered_parts.append(rendered)

    return "\n\n---\n\n".join(rendered_parts)
