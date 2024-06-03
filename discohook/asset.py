class Asset:
    """
    Represents a Discord asset.

    This is used internally by the library. You should not need to use this.

    Parameters
    ----------
    hash: :class:`str`
        The hash of the asset.
    fragment: :class:`str`
        The fragment of the asset path.
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
        Checks if the asset is animated.

        Returns
        -------
        :class:`bool`
        """
        return self.hash.startswith("a_")

    @property
    def default(self) -> bool:
        """
        Checks if the asset is a default avatar.

        Returns
        -------
        :class:`bool`
        """
        return len(self.hash) == 1

    @property
    def url(self) -> str:
        """
        Returns the URL of the asset in its default size with `.webp` format.

        Returns
        -------
        :class:`str`
        """
        return str(self)

    def url_as(self, *, format: str = "png", size: int = 1024) -> str:  # noqa
        """
        Returns the URL of the asset in the specified size and format.

        Parameters
        ----------
        size: :class:`int`
            The size of the asset.
        format: :class:`str`
            The format of the asset.

        Returns
        -------
        :class:`str`

        """
        return f"{self.BASE_URL}/{self.fragment}/{self.hash}.{format}?size={size}"
