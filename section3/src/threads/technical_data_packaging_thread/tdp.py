import jira
import teamcenter

class TechnicalDataPackage:
    """
    A Technical Data Package (TDP) contains the data necessary to
    define, produce, inspect, and maintain an item.
    """
    def __init__(self, tdp_number, title, author, date, description, requirements):
        self.tdp_number = tdp_number
        self.title = title
        self.author = author
        self.date = date
        self.description = description
        self.requirements = requirements

    def create_jira_ticket(self):
        """
        Creates a JIRA ticket for the TDP.
        """
        jira.create_ticket(self.tdp_number, self.title, self.author, self.date, self.description)

    def create_teamcenter_dataset(self):
        """
        Creates a new dataset in Teamcenter for the TDP.
        """
        teamcenter.create_dataset(self.tdp_number, self.title, self.author, self.date, self.description)
