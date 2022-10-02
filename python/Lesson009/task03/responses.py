import creator
import reader
import action
import remover
import updater
import constants
import searcher

show_contacts_command = "/showcontacts"
add_contact_command = "/addcontact"
remove_contact_command = "/removecontact"
update_contact_command = "/updatecontact"
find_contact_command = "/findcontact"
do_not_understand = "Я вообще ничего не понял!"


def sample_responses(input_text):

    user_message = str(input_text).lower()
    global_action = action.get_action()

    # Show contacts
    if user_message == show_contacts_command:
        return reader.show_items(constants.db_file_name)

    # Create a new contact
    if user_message == add_contact_command or global_action in ["add_last_name",
                                                                "add_phone_number",
                                                                "create_contact"]:
        response = creator.create_item(constants.db_file_name, global_action, user_message)
        return response

    # Delete contact
    if user_message == remove_contact_command or global_action == "get_contact_id":
        response = remover.delete(constants.db_file_name, global_action, user_message)
        return response

    # Update contact
    if user_message == update_contact_command or global_action in ["update_first_name",
                                                                   "update_last_name",
                                                                   "update_phone_number",
                                                                   "update_contact"]:
        response = updater.update(constants.db_file_name, global_action, user_message)
        return response

    # Find contact
    if user_message == find_contact_command or global_action in ["find_first_name",
                                                                 "find_last_name",
                                                                 "find_phone_number",
                                                                 "find_contact"]:
        response = searcher.search(constants.db_file_name, global_action, user_message)
        return response

    return do_not_understand
