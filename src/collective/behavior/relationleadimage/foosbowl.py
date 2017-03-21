from logging import getLogger
from zope.interface import alsoProvides
from zope.interface import Attribute
from zope.interface import implements
from zope.interface import Interface


logger = getLogger(__name__)


class IBelievable(Interface):
    """An item which can be believed
    """


class IUndeniable(IBelievable):
    """Something that is so believeable it cannot be denied
    """


class IMessage(Interface):
    """A message being communicated
    """

    def shout(noise_level=5):
        """Shout the message
        """

        content = Attribute("The actual text of the message")


class StandardMessage(object):
    implements(IMessage)

    def __init__(self, content):
        self.content = content

    def shout(self, noise_level=5):
        print self.content * noise_level


class StrongMessage(StandardMessage):
    implements(IBelievable)


class ICommunicationFactory(Interface):
    """A Python callable (e.g. classes) which is able to produce
    communication devices (e.g. messages).
    """


alsoProvides(StandardMessage, ICommunicationFactory)
