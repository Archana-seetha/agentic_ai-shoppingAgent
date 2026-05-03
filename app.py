import streamlit as st
from agent_graph import run_agent

st.set_page_config(page_title="Shopping Agent", page_icon="🛒")

st.title("🛒 Agentic Shopping AI")

query = st.text_input("What are you looking for?")

if st.button("Search"):

    result = run_agent(query)

    st.success(result.get("recommendation", ""))

    products = result.get("ranked", [])

    if not products:
        st.warning("No products found")
    else:
        cols = st.columns(2)

        for i, p in enumerate(products[:10]):
            with cols[i % 2]:

                if p.get("image"):
                    st.image(p["image"])

                st.write(f"**{p['name']}**")

                if p.get("price"):
                    st.write(f"₹{p['price']}")

                st.write(f"⭐ {p.get('rating', 'N/A')}")

                if p.get("link"):
                    st.markdown(
                        f'<a href="{p["link"]}" target="_blank">🛒 Buy Now</a>',
                        unsafe_allow_html=True
                    )

                st.divider()