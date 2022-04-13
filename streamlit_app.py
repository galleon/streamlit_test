from turtle import onclick
from requests import session
import streamlit as st
from copy import copy
import random
import time

s_nouns = [
    "A dude",
    "My mom",
    "The king",
    "Some guy",
    "A cat with rabies",
    "A sloth",
    "Your homie",
    "This cool guy my gardener met yesterday",
    "Superman",
]
p_nouns = [
    "These dudes",
    "Both of my moms",
    "All the kings of the world",
    "Some guys",
    "All of a cattery's cats",
    "The multitude of sloths living under your bed",
    "Your homies",
    "Like, these, like, all these people",
    "Supermen",
]
s_verbs = [
    "eats",
    "kicks",
    "gives",
    "treats",
    "meets with",
    "creates",
    "hacks",
    "configures",
    "spies on",
    "retards",
    "meows on",
    "flees from",
    "tries to automate",
    "explodes",
]
p_verbs = [
    "eat",
    "kick",
    "give",
    "treat",
    "meet with",
    "create",
    "hack",
    "configure",
    "spy on",
    "retard",
    "meow on",
    "flee from",
    "try to automate",
    "explode",
]
infinitives = [
    "to make a pie.",
    "for no apparent reason.",
    "because the sky is green.",
    "for a disease.",
    "to be able to make toast explode.",
    "to know more about archeology.",
]


def _part1(title: str):
    compute_time = time.time()
    st.session_state.part1["data"] = "\n".join(
        [f"- {i+1}" for i in range(random.randint(0, 4))]
    )
    st.session_state.part1["validated"] = False
    st.session_state.part1["time"] = time.time() - compute_time


def _part3():
    """Makes a random sentence from the different parts of speech. Uses a SINGULAR subject"""
    return f"{random.choice(s_nouns)} {random.choice(s_verbs)} {random.choice(s_nouns).lower() or random.choice(p_nouns).lower()} {random.choice(infinitives)}"


def click_form(line:str=""):
    st.session_state.part3[line]["data"] = _part3()

def main():
    st.title("Test")

    for part in ["part1", "part2", "part3"]:
        if part not in st.session_state:
            st.session_state[part] = None
            if part == "part1":
                st.session_state["part1"] = {"title": "Test"}

    form1 = st.form(key="form1")
    with form1:
        title = st.text_input(
            "Title",
            value=st.session_state.part1["title"],
        )
        if title and form1.form_submit_button("Random"):
            _part1(title)
            if st.session_state.part2:
                st.session_state.part2["validated"] = False

    if "validated" in st.session_state.part1:
        form2 = st.form(key="form2")
        with form2:
            part2 = st.text_area("TOC", st.session_state.part1["data"], 200)
            st.markdown(
                f"<span style='background-color:lightgrey'>Generated in {st.session_state.part1['time']:.3} s.</span>",
                unsafe_allow_html=True,
            )
            if part2 and form2.form_submit_button(
                "Go",
            ):
                st.session_state.part2 = {"data": part2, "validated": True}

    if st.session_state.part2 and st.session_state.part2["validated"]:
        lines = st.session_state.part2["data"].split("\n")

        if st.session_state.part3 is None:
            st.session_state.part3 = {}
            for line in lines:
                st.session_state.part3[line] = { "data": _part3()}
        else:
            # part3 does exist but might be smaller or bigger than # lines
            tmp = copy(st.session_state.part3)
            st.session_state.part3 = {}
            for line in lines:
                if line in tmp:
                    st.session_state.part3[line] = tmp[line]
                else:
                    st.session_state.part3[line] = { "data": _part3()}

        form3 = [st.form(key=f"form3_{i}") for i in range(len(lines))]
        for i, line in enumerate(lines):
            with form3[i]:
                _ = st.text_area(f"{line}", st.session_state.part3[line]["data"], 200, disabled=True)
                if form3[i].form_submit_button("Change", on_click=click_form, args=(line,)):
                    pass
                    # Need a form_submit_button to trigger the on_click callback

    st.write(st.session_state)


if __name__ == "__main__":
    main()
