from jira import JIRA


class JiraIntegration:
    """
    JiraIntegration class for handling JIRA integration.

    This class provides methods for interacting with JIRA, including creating,
    updating, and fetching issues related to Engineering Change Proposals (ECPs).

    Attributes:
        jira_client (JIRA): The JIRA client instance.
    """

    def __init__(self, server, username, password):
        """
        Initialize JiraIntegration with JIRA server credentials.

        Args:
            server (str): The JIRA server URL.
            username (str): The JIRA username.
            password (str): The JIRA password.
        """
        self.jira_client = JIRA(server=server, basic_auth=(username, password))

    def create_issue(self, project_key, issue_data):
        """
        Create a new JIRA issue.

        Args:
            project_key (str): The JIRA project key.
            issue_data (dict): A dictionary containing issue data.

        Returns:
            jira.resources.Issue: The created JIRA issue.
        """
        issue_fields = {
            "project": {"key": project_key},
            "summary": issue_data["summary"],
            "description": issue_data["description"],
            "issuetype": {"name": issue_data["issue_type"]},
        }
        if "priority" in issue_data:
            issue_fields["priority"] = {"name": issue_data["priority"]}

        return self.jira_client.create_issue(fields=issue_fields)

    def update_issue(self, issue_key, updated_data):
        """
        Update a JIRA issue.

        Args:
            issue_key (str): The JIRA issue key.
            updated_data (dict): A dictionary containing updated issue data.
        """
        issue = self.jira_client.issue(issue_key)
        issue.update(fields=updated_data)

    def get_issue(self, issue_key):
        """
        Get a JIRA issue by its key.

        Args:
            issue_key (str): The JIRA issue key.

        Returns:
            jira.resources.Issue: The fetched JIRA issue.
        """
        return self.jira_client.issue(issue_key)

    def search_issues(self, jql_query, max_results=50):
        """
        Search for JIRA issues using a JQL query.

        Args:
            jql_query (str): The JQL query string.
            max_results (int, optional): The maximum number of results to return.

        Returns:
            list[jira.resources.Issue]: A list of JIRA issues matching the query.
        """
        return self.jira_client.search_issues(jql_query, maxResults=max_results)
