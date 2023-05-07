"""
Jira-related functions for materials management thread.
"""

class JiraMaterialsManager:
    """
    Class to interact with Jira for materials management tasks.
    """

    def __init__(self, url, username, password):
        """
        Constructor for JiraMaterialsManager class.

        Args:
            url (str): The URL of the Jira instance.
            username (str): The username to authenticate with.
            password (str): The password to authenticate with.
        """
        self.jira = JIRA(url, basic_auth=(username, password))

    def create_issue(self, summary, description, project_key='MATS', issue_type='Task'):
        """
        Create a new issue in Jira.

        Args:
            summary (str): A short summary of the issue.
            description (str): A detailed description of the issue.
            project_key (str): The key of the project to create the issue in.
            issue_type (str): The type of the issue to create.

        Returns:
            str: The key of the created issue.
        """
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type},
        }

        new_issue = self.jira.create_issue(fields=issue_dict)
        return new_issue.key

    def search_issues(self, jql_query):
        """
        Search for issues in Jira using a JQL query.

        Args:
            jql_query (str): The JQL query to search with.

        Returns:
            List: A list of issue objects matching the query.
        """
        issues = self.jira.search_issues(jql_query)
        return issues
