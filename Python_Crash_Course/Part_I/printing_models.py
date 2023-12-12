# When a list is passed to a function, that function can modify it. Any changes made to the list by the function code
# are permanent. In this way, you gain the ability to work efficiently even when processing huge amounts of data.

def print_models(unprinted_designs, completed_models):
    """We simulate the printing of individual designs as long as there is any design left in the list.
    Each printed model is moved to the completed_models list."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Model printing: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Displays all models that have been printed."""
    print("\nPrinted models:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'icosahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
