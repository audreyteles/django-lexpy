import importlib
from django.conf import settings

class ShortKey:
    """Class to manage short keys."""

    def __init__(self, short_key: str):
        # Get language code from settings
        language_settings = settings.LANGUAGE_CODE.replace("-", "_")

        # Load messages package
        lang_module = importlib.import_module(f'lang.{language_settings}')
        self.__messages: dict = lang_module.messages

        # Get short_key and validate
        self.__short_key = short_key
        assert self.__short_key in self.__messages, "This short key don't exists!"

        # Generate a list. before: "foo.bar"  now:["foo", "bar"]
        short_key: list = self.__short_key.split(".")

        assert len(short_key) == 2, "Your call is wrong, try something like 'message.welcome'"

        # Set prefix and content
        self.__prefix, self.__content = short_key

        # Validate prefix
        assert self.__prefix == "message", f"The prefix '{self.__prefix}' isn't allowed, try something like 'message._____'"

    @property
    def short_key(self) -> str:
        """Retrieve the short key.

        Returns
        -------
        str
            The short key.
        """
        return self.__short_key

    @property
    def message(self) -> str:
        """Retrieve the message related to the supplied short key.

        Returns
        -------
        str
            A message in a specific language
        """
        return self.__messages.get(self.__short_key)
