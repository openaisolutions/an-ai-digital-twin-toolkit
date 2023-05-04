# quality_thread/jira.py

from jira import JIRA

class JiraQuality:
    def __init__(self, server, username, api_key):
        """
        Initialize JiraQuality object with JIRA server and authentication details.

        Args:
            server (str): URL of the JIRA server.
            username (str): JIRA username.
            api_key (str): JIRA API key.
        """
        self.jira = JIRA(server=server, basic_auth=(username, api_key))

    def create_issue(self, project, issue_type, summary, description, priority):
        """
        Create a JIRA issue for quality management.

        Args:
            project (str): Project key in JIRA.
            issue_type (str): Type of issue to be created.
            summary (str): Summary of the issue.
            description (str): Description of the issue.
            priority (str): Priority of the issue.

        Returns:
            jira.resources.Issue: The created JIRA issue.
        """
        issue_data = {
            "project": {"key": project},
            "issuetype": {"name": issue_type},
            "summary": summary,
            "description": description,
            "priority": {"name": priority},
        }
        return self.jira.create_issue(fields=issue_data)

    def update_issue(self, issue_key, status, comment=None):
        """
        Update a JIRA issue's status and add an optional comment.

        Args:
            issue_key (str): Key of the JIRA issue to update.
            status (str): New status of the issue.
            comment (str, optional): Comment to add to the issue. Defaults to None.
        """
        issue = self.jira.issue(issue_key)
        self.jira.transition_issue(issue, status)

        if comment:
            self.jira.add_comment(issue, comment)
