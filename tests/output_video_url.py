from robot.libraries.BuiltIn import BuiltIn
import time

def output_video_url():
    session_id = BuiltIn().get_library_instance('SeleniumLibrary').driver.session_id
    BuiltIn().log_to_console("VIDEO_URL={}".format(session_id))
    time.sleep(15)