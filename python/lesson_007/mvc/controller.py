from statistics import mode
import model
import view

def click_button():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.sum()
    view.view_data(result)