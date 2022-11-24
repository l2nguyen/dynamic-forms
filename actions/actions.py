from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher


class ValidateRecoverPassword(FormValidationAction):
    """Example of a form validation action."""

    def name(self) -> Text:
        return "validate_password_recover_form"

    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Text]:
        # see: https://rasa.com/docs/rasa/forms/#dynamic-form-behavior

        additional_slots = ["known_question"]
        if tracker.slots.get("known_question") is False:
            # If the user doesn't know the answer to the safety question, ask
            # if they know the associated email
            additional_slots.append("known_email")

        return additional_slots + domain_slots
