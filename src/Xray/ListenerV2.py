import os, base64, pyscreenrec
from .attributes import *
from .config import Config
from .report import Report
from .xray import Xray
from robot.libraries.BuiltIn import BuiltIn

b = BuiltIn()

class ListenerV2:
    """Optional base class for listeners using the listener API version 2."""
    ROBOT_LISTENER_API_VERSION = 2
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self.report = []
        self.suite_index = 0
        self.test_index = 0
        self.keyword_index = 0
        self.recorder = pyscreenrec.ScreenRecorder()

    def start_suite(self, name: str, attributes: StartSuiteAttributes):
        """Called when a suite starts."""
        self.report.append({
            "id": attributes.get('id'),
            "longname": attributes.get('longname'),
            "doc": attributes.get('doc'),
            "metadata": attributes.get('metadata'),
            "source": attributes.get('source'),
            "suites": attributes.get('suites'),
            "tests": [],
            "totaltests": attributes.get('totaltests'),
            "starttime": attributes.get('starttime'),
        })

    def end_suite(self, name: str, attributes: EndSuiteAttributes):
        """Called when a suite end."""
        suite = self.report[self.suite_index]
        suite['endtime'] = attributes.get('endtime')
        suite['elapsedtime'] = attributes.get('elapsedtime')
        suite['status'] = attributes.get('status')
        suite['statistics'] = attributes.get('statistics')
        suite['message'] = attributes.get('message')

        self.suite_index = self.suite_index + 1
        self.test_index = 0
        self.keyword_index = 0

    def start_test(self, name: str, attributes: StartTestAttributes):
        """Called when a test or task starts."""
        self.report[self.suite_index]['tests'].append({
            "id": attributes.get('id'),
            "longname": attributes.get('longname'),
            "originalname": attributes.get('originalname'),
            "doc": attributes.get('doc'),
            "tags": attributes.get('tags'),
            "template": attributes.get('template'),
            "source": attributes.get('source'),
            "lineno": attributes.get('lineno'),
            "starttime": attributes.get('starttime'),
            "endtime": '',
            "elapsedtime": 0,
            "message": '',
            "xraytest": '',
            "keywords": [],
            "video": '',
        })

        for tag in attributes.get('tags'):
            if Config.project_key() in tag:
                test = self.report[self.suite_index]['tests'][self.test_index]
                test['xraytest'] = tag

        self.recorder.start_recording("{}.mp4".format(attributes.get('id')), 10)

    def end_test(self, name: str, attributes: EndTestAttributes):
        """Called when a test or task ends."""
        test = self.report[self.suite_index]['tests'][self.test_index]
        test['endtime'] = attributes.get('endtime')
        test['elapsedtime'] = attributes.get('elapsedtime')
        test['status'] = attributes.get('status')
        test['message'] = attributes.get('message')

        self.recorder.stop_recording()
        try:
            recording = "{}.mp4".format(attributes.get('id'))
            with open(recording, 'rb') as video_file:
                test['video'] = base64.b64encode(video_file.read()).decode('utf-8')

            if os.path.isfile(recording):
                os.remove(recording)
            else:
                print("Error: %s file not found" % recording)
        except Exception:
            print("An error occurred while generating/attaching the video to the test.")

        self.test_index = self.test_index + 1
        self.keyword_index = 0

    def start_keyword(self, name: str, attributes: StartKeywordAttributes):
        """Called when a keyword or a control structure like IF starts.

        The type of the started item is in ``attributes['type']``. Control
        structures can contain extra attributes that are only relevant to them.
        """
        keyword = self.report[self.suite_index]['tests'][self.test_index]
        keyword['keywords'].append({
            "type": attributes.get('type'),
            "kwname": attributes.get('kwname'),
            "libname": attributes.get('libname'),
            "doc": attributes.get('doc'),
            "args": attributes.get('args'),
            "assign": attributes.get('assign'),
            "tags": attributes.get('tags'),
            "source": attributes.get('source'),
            "lineno": attributes.get('lineno'),
            "status": attributes.get('status'),
            "starttime": attributes.get('starttime'),
            "endtime": '',
            "elapsedtime": 0,
        })

    def end_keyword(self, name: str, attributes: EndKeywordAttributes):
        """Called when a keyword or a control structure like IF ends.

        The type of the started item is in ``attributes['type']``. Control
        structures can contain extra attributes that are only relevant to them.
        """
        keyword = self.report[self.suite_index]['tests'][self.test_index]['keywords'][self.keyword_index]
        keyword['endtime'] = attributes.get('endtime')
        keyword['elapsedtime'] = attributes.get('elapsedtime')
        keyword['status'] = attributes.get('status')

        self.keyword_index = self.keyword_index + 1

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
        if Config.test_type() == "ROBOT":
            Report.robot(self.report)
            testExecutionId = Xray.importExecutionRobot()
            print('Report sent successfully')
            print('------------------------------------------------------------------------------')
            print('Now if there is evidence we will be sending it, wait a moment...')
            self._send_evidence(self.report, testExecutionId['issueId'])
            print('==============================================================================')
        elif Config.test_type() == "CUCUMBER":
            Report.cucumber(self.report)
            print('Report sent successfully')
            print('------------------------------------------------------------------------------')
            Xray.importExecutionCucumber()
        else:
            print('Set the TEST_TYPE in .env!')
    
    def _send_evidence(self, report, testExecutionId):
        for suite in report:
            for test in suite['tests']:
                if test['video'] and test['xraytest']:
                    xrayTestIssueId = Xray.getTest(test['xraytest'])
                    id = Xray.getTestRun(xrayTestIssueId, testExecutionId)
                    Xray.addEvidenceToTestRun(id, 'Evidence_{}.mp4'.format(test['xraytest']), test['video'])
                    print('- {} test evidence submitted successfully!'.format(test['xraytest']))
                else:
                    print('- {} test does not have evidence, skip step...'.format(test['xraytest']))