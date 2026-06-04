import re
import vitedoc
from vitedoc import Action


version = ""
with open("discohook/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)  # type: ignore

if __name__ == '__main__':
    vitedoc.init(
        base_dir="docs",
        title="discohook",
        description="A discord interaction API wrapper for serverless applications.",
        logo_path="/favicon.png",
        actions=[
            Action(
                theme="brand",
                text="Docs",
                link=f"/guide/{version}/introduction",
            ),
            Action(
                theme="alt",
                text="GitHub",
                link="https://github.com/jnsougata/discohook"
            ),
        ]
    )
