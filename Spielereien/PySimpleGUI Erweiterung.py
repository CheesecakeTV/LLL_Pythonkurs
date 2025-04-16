from collections.abc import Iterable
import FreeSimpleGUI as sg
import re
from typing import Self

class BetterElement(sg.Element):
    """
    Beware of MRO, this class should be the last one inherited or it will overwrite __init__
    """

    def event(self, window: "BetterWindow", event, value: dict) -> (any,dict):
        """
        Called, when this Element throws an event
        """
        return event,value

    def other_event(self, window: "BetterWindow", event, value: dict) -> (any,dict):
        """
        Called, when any other event was thrown
        """
        return self.event(window, event, value)

    def __hash__(self):
        return id(self)

    def __eq__(self, other:Self):
        return self.key == other.key

class BetterWindow(sg.Window):

    def __init__(self,*args,**kwargs):
        """
        You can use this like a normal window.
        It has a couple of helpful functionality, but these are not that important.
        Read the docstring of BetterWindow.help for details
        :param args:
        :param kwargs:
        """
        super().__init__(*args,**kwargs)
        self.key = id(self)
        self.better_elements:set[BetterElement|sg.Element] = {elem for elem in self.element_list() if hasattr(elem,"event")}

    def read(self, *args, useful_features=True, **kwargs) -> (any,dict):
        """
        Better read method.

        Key feature:
        When the thrown event corresponds to an Object that has the event-attribute (method), its event-method will be called.
        event, value can be modified inside this method.

        Helpful features:
        - If key is callable, it will be called like this: key(window, event, value)
        -> If a TypeError occurs, the key-Function will also be called like this: key()
        -> If key is a tuple with key[0] being callable, the previous rules will be applied to it

        :param useful_features: True, if you want to use the listed features
        :param args:
        :param kwargs:
        :return:
        """
        event, value = super().read(*args, **kwargs)
        if value is None:
            return None, None

        for elem in self.better_elements:
            if event == elem.key:
                event, value = elem.event(self, event, value)
                continue

            event, value = elem.other_event(self, event, value)

        if useful_features:
            event, value = self._handle_useful_read_features(event, value)

        return event, value

    def _handle_useful_read_features(self,event,value):
        if callable(event):
            try:
                event(self,event,value)
            except TypeError:
                event()

            return event, value

        if isinstance(event,tuple) and callable(event[0]):
            try:
                event[0](self, event, value)
            except TypeError:
                event[0]()

            return event, value

        return event,value

class InputRegex(sg.Input,BetterElement):

    def __init__(self,regex_key:str=r".*",wrong_color:str = "red",*args,**kwargs):
        """
        Input element that only "accepts" inputs matching a regex-pattern.
        If the pattern does not match, the color changes.

        :param regex_key: The regex-pattern. Can not be changed.
        :param wrong_color: Color for no match
        :param args: passed through to the input-element
        :param kwargs: passed through to the input-element
        """
        super().__init__(*args,**kwargs)
        self._regex_key = re.compile(regex_key)
        self.wrong_background_color = wrong_color if wrong_color else self.BackgroundColor

        self._previous_val = self.DefaultText
        self._standard_background_color = self.BackgroundColor

    def event(self, window: BetterWindow, event, value: dict) -> (any, dict):
        if self._regex_key.fullmatch(value[self.key]):
            self._update_color(True)
            self.update(background_color=self._standard_background_color)
            return event,value

        value[self.key] = self._previous_val
        self._update_color(False)
        return event,value

    def _update_color(self,correct:bool):
        self.update(background_color=self._standard_background_color if correct else self.wrong_background_color)

class ToggleButton(sg.Button,BetterElement):

    def __init__(self,button_text="",active_color = "green",active_text:str = None,*args,**kwargs):
        """
        Button that functions simmilar to a toggle-button.
        When "activated", it changes color and/or changes its text.

        :param button_text: Normal (off) text
        :param active_color: Active (on) color. Set to None to disable
        :param active_text: Active (on) text. Leave None to disable
        :param args: Passed through to the Button
        :param kwargs: Passed through to the Button
        """
        super().__init__(button_text,*args,**kwargs)

        self._button_text = button_text

        if active_text is None:
            active_text = button_text

        self.active_text = active_text

        self._normal_color = self.ButtonColor[1]
        if active_color is None:
            active_color = self._normal_color
        self.active_color = active_color

        self.state = False

    def event(self, window: "BetterWindow", event, value: dict) -> (any,dict):
        self.state = not self.state

        self.update(button_color=self.active_color if self.state else self._normal_color)
        self(self.active_text if self.state else self._button_text)

        return event,value

    def other_event(self, window: "BetterWindow", event, value: dict) -> (any,dict):
        value[self.key] = self.state
        return event,value

class RadioGroup(sg.Column,BetterElement):
    group_id = 1

    def __init__(
            self,names:Iterable[str],key:str,*args,radio_args:tuple=(),
            radio_kwargs:dict=None,enable_events:bool=True,
            element_keys:Iterable[str|None]=None,vertical:bool=True,**kwargs
    ):
        """
        Column of radio-buttons.
        value[common_key] contains the currently selected radio-key.
        If no button was selected yet, value[common_key] equals ""

        :param names: Visible names besides the buttons
        :param key: Key for storing which button is selected atm
        :param radio_args: Passed through to all radios
        :param radio_kwargs: Passed through to all radios
        :param args: Passed through to the COLUMN
        :param enable_events: Enables events for EVERY RADIO
        :param element_keys: Use this parameter to set a specific key for single radios. Pass None to apply name as key
        :param vertical: True, if the radios should be arranged vertically
        :param kwargs: Passed through to the COLUMN
        """

        if element_keys is not None:
            element_keys = [
                k1 if k1 is not None else k2 # + common_key
                for k1,k2 in zip(element_keys,names)
            ]
        else:
            #element_keys = map(lambda a:common_key + a,names)
            element_keys = names

        text_len = max(map(len,names))

        self.radios = [
            sg.Radio(
                name,
                *radio_args,
                **radio_kwargs,
                group_id=self.__class__.group_id,
                key=key,
                enable_events=enable_events,
                size=(text_len,0),
            ) for name,key in zip(names,element_keys)
        ]
        self.__class__.group_id += 1

        self.all_keys = tuple(element_keys)
        self.common_key = key

        if vertical:
            my_layout = [[i] for i in self.radios]
        else:
            my_layout = [self.radios]

        super().__init__(my_layout,*args,key=key,**kwargs)

        self.last_selection = ""

    def event(self, window: "BetterWindow", event, value: dict) -> (any,dict):
        if event in self.all_keys:
            self.last_selection = event
            value[self.common_key] = event
            return event, value

        value[self.common_key] = self.last_selection
        return event, value

layout = [
    [
        InputRegex(regex_key=r"(|.+\..+)", key="Test", enable_events=True)
    ],[
        sg.Button("Event"),
        ToggleButton("Toggle",key="Toggle",active_text="An")
    ],[
        RadioGroup(["Hallo", "Was", "Geht"], key="Radio", vertical=False)
    ]
]

w = BetterWindow("Test",layout,finalize=True)

while True:
    e,v = w.read()
    print(e,v)

    if e is None:
        w.close()
        break


