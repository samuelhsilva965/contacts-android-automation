from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

def click_and_hold(driver, element, duration=2000):
    finger = PointerInput("touch", "finger")
    actions = ActionBuilder(driver, mouse=finger)

    actions.pointer_action.move_to(element)
    actions.pointer_action.pointer_down()
    actions.pointer_action.pause(duration / 1000)  # segundos
    actions.pointer_action.pointer_up()

    actions.perform()