# TestLoggingGCP
What This Workflow Does:
Logs Testing:
The Python script uses the logging library to emit logs.
unittest validates log messages are correctly formatted and captured.
GitHub Actions Workflow:
Installs Python and required dependencies.
Runs test_logging.py to ensure the logging setup works correctly.
Output Logs:
Any failure or mismatched logs will cause the job to fail, visible in GitHub Actions logs.
