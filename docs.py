import re
import vitedoc
from vitedoc import Action, Feature


version = ""
with open("discohook/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)  # type: ignore

if __name__ == '__main__':
    vitedoc.init(
        base_dir="docs",
        title="discohook",
        description="A discord interaction API wrapper for serverless applications.",
        actions=[
            Action(
                theme="brand",
                text="Get started",
                link=f"/guide/{version}/introduction",
            ),
            Action(
                theme="alt",
                text="GitHub",
                link="https://github.com/jnsougata/discohook"
            ),
        ],
        features=[
            Feature(
                icon_emoji="🚀",
                title="Serverless Optimized",
                details="Built specifically for cloud environments to ensure fast and low latency Discord "
                        "interactions without persistent connections."
            ),
            Feature(
                icon_emoji="🧩",
                title="Unified Command System",
                details="Quickly build and register various Discord interaction types including slash commands, "
                        "user commands, and message commands all within one intuitive interface."
            )
        ]
    )
