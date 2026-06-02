class Asset:
    """
    Represents a Discord asset.

    This is used internally by the library. You should not need to use this.
    Args:
        hash (str): The hash of the asset.
        fragment (str): The fragment of the asset.
    """

    BASE_URL = "https://cdn.discordapp.com"

    def __init__(self, *, hash: str, fragment: str) -> None:  # noqa
        self.hash = hash
        self.fragment = fragment

    def __str__(self) -> str:
        if self.dynamic:
            return f"{self.BASE_URL}/{self.fragment}/{self.hash}.gif?size=1024"
        if self.default:
            return f"{self.BASE_URL}/{self.fragment}/{self.hash}.png"
        return f"{self.BASE_URL}/{self.fragment}/{self.hash}.webp?size=1024"

    @property
    def dynamic(self) -> bool:
        """
        Checks if the asset is animated or not.

        Returns:
            bool: Whether the asset is animated.
        """
        return self.hash.startswith("a_")

    @property
    def default(self) -> bool:
        """
        Checks if the asset is a default avatar.

        Returns:
            bool: Whether the asset is a default avatar.
        """
        return len(self.hash) == 1

    @property
    def url(self) -> str:
        """
        Constructs the URL of the asset in its default size with `.webp` format.

        Returns:
            str: The URL of the asset in its default size with `.webp` format.
        """
        return str(self)

    def url_as(self, *, format: str = "png", size: int = 1024) -> str:  # noqa
        """
        Constructs the URL of the asset in the specified size and format.

        Args:
            format (str): The format of the asset.
            size (int): The size of the asset.

        Returns:
            str: The URL of the asset in the specified size and format.

        """
        return f"{self.BASE_URL}/{self.fragment}/{self.hash}.{format}?size={size}"
