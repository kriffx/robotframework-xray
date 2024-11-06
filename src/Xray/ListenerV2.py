import json
from robot.libraries.BuiltIn import BuiltIn

try:
    import config as Config, report as Report, xray as Xray
except ImportError as e:
    from .config import Config
    from .report import Report
    from .xray import Xray

class ListenerV2:
    """Optional base class for listeners using the listener API version 2."""
    ROBOT_LISTENER_API_VERSION = 2
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self.execution = []
        self.suite_index = 0
        self.test_index = 0
        self.keyword_index = 0
        self.config = Config.Config or Config
        self.report = Report.Report or Report
        self.xray = Xray.Xray or Xray

    def start_suite(self, name: str, attributes):
        """Called when a suite starts."""
        if self.config.debug():
            print("start_suite")
            print(json.dumps(attributes, indent=4))

        self.execution.append({
            "id": attributes.get('id'),
            "doc": attributes.get('doc') + ' Test Suite.',
            "metadata": attributes.get('metadata'),
            "starttime": attributes.get('starttime'),
            "longname": attributes.get('longname'),
            "tests": [],
            "suites": attributes.get('suites'),
            "totaltests": attributes.get('totaltests'),
            "source": attributes.get('source'),
        })

    def end_suite(self, name: str, attributes):
        """Called when a suite end."""
        if self.config.debug():
            print("\nend_suite")
            print(json.dumps(attributes, indent=4))

        suite = self.execution[self.suite_index]
        suite['endtime'] = attributes.get('endtime')
        suite['elapsedtime'] = attributes.get('elapsedtime')
        suite['status'] = attributes.get('status')
        suite['message'] = attributes.get('message')
        suite['statistics'] = attributes.get('statistics')

        self.suite_index = self.suite_index + 1
        self.test_index = 0
        self.keyword_index = 0

    def start_test(self, name: str, attributes):
        """Called when a test or task starts."""
        if self.config.debug():
            print("start_test")
            print(json.dumps(attributes, indent=4))

        self.execution[self.suite_index]['tests'].append({
            "id": attributes.get('id'),
            "doc": attributes.get('doc'),
            "tags": attributes.get('tags'),
            "lineno": attributes.get('lineno'),
            "starttime": attributes.get('starttime'),
            "longname": attributes.get('longname'),
            "source": attributes.get('source'),
            "template": attributes.get('template'),
            "originalname": attributes.get('originalname'),
            "endtime": '',
            "elapsedtime": 0,
            "status": 'NOT SET',
            "message": '',
            "keywords": [],
        })
    
    def end_test(self, name: str, attributes):
        """Called when a test or task ends."""
        if self.config.debug():
            print("end_test")
            print(json.dumps(attributes, indent=4))

        test = self.execution[self.suite_index]['tests'][self.test_index]
        test['endtime'] = attributes.get('endtime')
        test['elapsedtime'] = attributes.get('elapsedtime')
        test['status'] = attributes.get('status')
        test['message'] = attributes.get('message')
        
        self.test_index = self.test_index + 1
        self.keyword_index = 0

    def start_keyword(self, name: str, attributes):
        """Called when a keyword or a control structure like IF starts.

        The type of the started item is in ``attributes['type']``. Control
        structures can contain extra attributes that are only relevant to them.
        """
        if self.config.debug():
            print("start_keyword")
            print(json.dumps(attributes, indent=4))

        keyword = self.execution[self.suite_index]['tests'][self.test_index]
        keyword['keywords'].append({
            "doc": attributes.get('doc'),
            "lineno": attributes.get('lineno'),
            "type": attributes.get('type'),
            "status": attributes.get('status'),
            "starttime": attributes.get('starttime'),
            "source": attributes.get('source'),
            "kwname": attributes.get('kwname'),
            "libname": attributes.get('libname'),
            "args": attributes.get('args'),
            "assign": attributes.get('assign'),
            "tags": attributes.get('tags'),
            "messages": [],
            "endtime": '',
            "elapsedtime": 0,
        })

    def end_keyword(self, name: str, attributes):
        """Called when a keyword or a control structure like IF ends.

        The type of the started item is in ``attributes['type']``. Control
        structures can contain extra attributes that are only relevant to them.
        """
        if self.config.debug():
            print("end_keyword")
            print(json.dumps(attributes, indent=4))
            
        keyword = self.execution[self.suite_index]['tests'][self.test_index]['keywords'][self.keyword_index]
        keyword['status'] = attributes.get('status')
        keyword['endtime'] = attributes.get('endtime')
        keyword['elapsedtime'] = attributes.get('elapsedtime')

        self.keyword_index = self.keyword_index + 1

    def log_message(self, message):
        """Called when a normal log message are emitted.

        The messages are typically logged by keywords, but also the framework
        itself logs some messages. These messages end up to output.xml and
        log.html.
        """
        if self.config.debug():
            print("log_message")
            print(json.dumps(message, indent=4))

        msg = self.execution[self.suite_index]['tests'][self.test_index]['keywords'][self.keyword_index]
        msg['messages'].append({
            "timestamp": message.get('timestamp'),
            "message": message.get('message'),
            "level": message.get('level'),
            "html": message.get('html'),
        })

    def message(self, message):
        """Called when framework's internal messages are emitted.

        Only logged by the framework itself. These messages end up to the syslog
        if it is enabled.
        """
        if self.config.debug():
            print("message")
            print(json.dumps(message, indent=4))

    def library_import(self, name: str, attributes):
        """Called after a library has been imported."""
        if self.config.debug():
            print("library_import")
            print(json.dumps(attributes, indent=4))

    def resource_import(self, name: str, attributes):
        """Called after a resource file has been imported."""
        if self.config.debug():
            print("resource_import")
            print(json.dumps(attributes, indent=4))

    def variables_import(self, name: str, attributes):
        """Called after a variable file has been imported."""
        if self.config.debug():
            print("variables_import")
            print(json.dumps(attributes, indent=4))

    def output_file(self, path: str):
        """Called after the output file has been created.

        At this point the file is guaranteed to be closed.
        """

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
        test_plan = BuiltIn().get_variable_value("${TESTPLAN}")
        report_names = self.report.cucumber(self, self.execution, test_plan)
        self.xray.importExecutionCucumber(self, report_names, test_plan)