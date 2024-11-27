import logging
import unittest
from io import StringIO

class TestLogging(unittest.TestCase):
    def setUp(self):
        # Set up a logger with a StringIO stream
        self.log_stream = StringIO()
        self.logger = logging.getLogger("test_logger")
        self.logger.setLevel(logging.DEBUG)

        # Create a stream handler
        handler = logging.StreamHandler(self.log_stream)
        handler.setFormatter(logging.Formatter('%(levelname)s:%(message)s'))
        self.logger.addHandler(handler)

    def tearDown(self):
        # Remove all handlers after the test
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
            handler.close()

    def test_debug_logging(self):
        self.logger.debug("This is a debug message")
        self.assertIn("DEBUG:This is a debug message", self.log_stream.getvalue())

    def test_info_logging(self):
        self.logger.info("This is an info message")
        self.assertIn("INFO:This is an info message", self.log_stream.getvalue())

    def test_error_logging(self):
        self.logger.error("This is an error message")
        self.assertIn("ERROR:This is an error message", self.log_stream.getvalue())

if __name__ == "__main__":
    unittest.main()
