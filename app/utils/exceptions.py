class ContactNotFoundException(Exception):
    """
    ContactNotFoundException is raised when the specified contact is not found in the WhatsApp contact list.
    """

    def __init__(self, contact_name: str):
        super().__init__(
            f"Contact with name '{contact_name}' not found in the WhatsApp contact list. Please provide a valid contact name."
        )