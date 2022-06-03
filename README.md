# streamlit_test

Having fun with 864 and  [Streamlit](https://streamlit.io)

```
    docker pull lukasblecher/pix2tex:api
    docker run --rm -p 8502:8502 lukasblecher/pix2tex:api
    uvicorn uvicorn backend.api:app --reload
```

and

`streamlit run  streamlit_app.py`
