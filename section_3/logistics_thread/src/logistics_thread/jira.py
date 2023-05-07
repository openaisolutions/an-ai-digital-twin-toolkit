class JiraTicket:
    def __init__(self, ticket_id, summary, description, status):
        self.ticket_id = ticket_id
        self.summary = summary
        self.description = description
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Jira Ticket {self.ticket_id} ({self.summary}) - {self.status}"
