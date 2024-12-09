"""# Warning

Solara has 4 types of alerts:

 * [Success](/documentation/components/status/success)
 * [Info](/documentation/components/status/info)
 * Warning (this page)
 * [Error](/documentation/components/status/error)



"""

import solara
from solara.website.utils import apidoc


@solara.component
def Page():
    state = solara.use_reactive(
        {
            "icon": True,
            "dense": False,
            "outlined": True,
            "text": True,
        }
    )

    with solara.GridFixed(4):
        solara.Checkbox(label="Use icon", value=state.value["icon"], on_value=lambda val: state.value.update({"icon": val}))
        solara.Checkbox(label="Show dense", value=state.value["dense"], on_value=lambda val: state.value.update({"dense": val}))
        solara.Checkbox(label="Show as text", value=state.value["text"], on_value=lambda val: state.value.update({"text": val}))
        solara.Checkbox(label="Show outlined", value=state.value["outlined"], on_value=lambda val: state.value.update({"outlined": val}))

    solara.Warning(
        f"This is solara.Warning(label='...', text={state.value['text']}, dense={state.value['dense']}, outlined={state.value['outlined']}, icon={state.value['icon']})",
        text=state.value["text"],
        dense=state.value["dense"],
        outlined=state.value["outlined"],
        icon=state.value["icon"],
    )


__doc__ += apidoc(solara.Warning.f)  # type: ignore
