from streamlit_drawable_canvas import st_canvas

import streamlit as st

from PIL import Image

import requests

BASE_URI = "http://127.0.0.1:8502"

def latex():
    st.markdown("#LaTeX")

    data = st_canvas(
        fill_color="rgba(255, 255, 255, 0.3)",
        stroke_width=3,
        stroke_color="#000000",
        background_color="rgba(255, 255, 255, 0.3)",
        background_image=None,
        update_streamlit=True,
        height=150,
        drawing_mode='freedraw',
        point_display_radius=2,
        key="canvas",
    )

    if st.button("Translate"):

        st.image(data.image_data)

        file_path = f"/tmp/plop.jpg"

        img_data = data.image_data
        im = Image.fromarray(img_data.astype("uint8"), mode="RGBA")
        im.save(file_path, "PNG")

        # buffered = BytesIO()
        # im.save(buffered, format="PNG")
        # img_data = buffered.getvalue()
        # try:
        #     # some strings <-> bytes conversions necessary here
        #     b64 = base64.b64encode(img_data.encode()).decode()
        # except AttributeError:
        #     b64 = base64.b64encode(img_data).decode()

        files = {"file": open(file_path)}

        response = requests.post(
            f"{BASE_URI}/predict",
            files=files,
        )
        if response.status_code == 200:
            d = response.json()
            st.write(d)
