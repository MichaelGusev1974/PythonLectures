# controller.py - будет связующим звеном между model и view
import model_sub as model
import view
def button_clik():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    view.view_data(result, 'result')