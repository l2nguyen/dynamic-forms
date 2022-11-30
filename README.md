# Dynamic forms examples

## password_recover_form
Dyanmically add slots to password recover form based on user response.

This also has an example of:

- [conditional response variation](https://rasa.com/docs/rasa/responses#conditional-response-variations) for `utter_submit_password_recover_form`
- multi intent such as `recover_password+dont_know_question`


## example_flow_form
Dynamically add slots to the example flow form form based on user response. If the user selects the `/affirm` button, then the next question in the flow will be added to the form.

This also has an example of:

- [conditional response variation](https://rasa.com/docs/rasa/responses#conditional-response-variations) for `utter_submit_example_flow_form`

## How to use this example?

1. Train a Rasa model containing the Rasa NLU and Rasa Core models by running:
    ```
    rasa train
    ```
    The model will be stored in the `models/` directory as a zipped file


2. Start your action server
   ```
   rasa run actions
   ```

3. Test the assistant by running:
    ```
    rasa shell --debug
    ```
    This will load the assistant in your command line for you to chat.

For more information about the individual commands, please check out our
[documentation](http://rasa.com/docs/rasa/command-line-interface).

4. Activate the relevant form
To activate the `password_recover_form`, say `recover_password` by saying "I lost my password" or `/recover_password` to the bot.

To activate the 