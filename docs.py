import vitedoc
from vitedoc import Action


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
                link="/content/discohook",
            ),
            Action(
                theme="alt",
                text="GitHub",
                link="https://github.com/jnsougata/discohook"
            ),
        ]
    )
