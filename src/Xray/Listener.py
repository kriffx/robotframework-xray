from logging import info
from .attributes import *
from .config import Config
from .xray import Xray
from robot.libraries.BuiltIn import BuiltIn

b = BuiltIn()

class Listener:
    """Optional base class for listeners using the listener API version 2."""
    ROBOT_LISTENER_API_VERSION = 2
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    XRAY : Xray

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self.XRAY = Xray()

    def start_suite(self, name: str, attributes: StartSuiteAttributes):
        """Called when a suite starts."""
        


    def end_suite(self, name: str, attributes: EndSuiteAttributes):
        """Called when a suite end."""
        


    def start_test(self, name: str, attributes: StartTestAttributes):
        """Called when a test or task starts."""
        


    def end_test(self, name: str, attributes: EndTestAttributes):
        """Called when a test or task ends."""
        


    def start_keyword(self, name: str, attributes: StartKeywordAttributes):
        """Called when a keyword or a control structure like IF starts.

        The type of the started item is in ``attributes['type']``. Control
        structures can contain extra attributes that are only relevant to them.
        """
        


    def end_keyword(self, name: str, attributes: EndKeywordAttributes):
        """Called when a keyword or a control structure like IF ends.

        The type of the started item is in ``attributes['type']``. Control
        structures can contain extra attributes that are only relevant to them.
        """
        


    def log_message(self, message: MessageAttributes):
        """Called when a normal log message are emitted.

        The messages are typically logged by keywords, but also the framework
        itself logs some messages. These messages end up to output.xml and
        log.html.
        """

    def message(self, message: MessageAttributes):
        """Called when framework's internal messages are emitted.

        Only logged by the framework itself. These messages end up to the syslog
        if it is enabled.
        """


    def library_import(self, name: str, attributes: LibraryAttributes):
        """Called after a library has been imported."""


    def resource_import(self, name: str, attributes: ResourceAttributes):
        """Called after a resource file has been imported."""


    def variables_import(self, name: str, attributes: VariablesAttributes):
        """Called after a variable file has been imported."""


    def output_file(self, path: str):
        """Called after the output file has been created.

        At this point the file is guaranteed to be closed.
        """
        print('potencial screenshot')

    def log_file(self, path: str):
        """Called after the log file has been created."""


    def report_file(self, path: str):
        """Called after the report file has been created."""


    def xunit_file(self, path: str):
        """Called after the xunit compatible output file has been created."""


    def debug_file(self, path: str):
        """Called after the debug file has been created."""


    def close(self):
        """Called when the whole execution ends.

        With library listeners called when the library goes out of scope.
        """
        info("Execution ended.")
    
