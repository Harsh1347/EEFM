from eefm import PA,PEq,PF,PG,AEq,AF,AG,AP,FA,FP

import streamlit as st

st.title("EEFM")

a = st.number_input("Ao")
b = st.number_input("F or P or G")
c = st.number_input("i in %")
d = st.number_input("n")

f1,f2,f3,f4,f5,f6,f7,f8,f9,f10 = st.beta_columns(10)


if f1.button("PA"):
    st.success(PA(b,c,d))

if f2.button("FA"):
    st.success(FA(b,c,d))

if f3.button("AF"):
    st.success(AF(b,c,d))

if f4.button("PF"):
    st.success(PF(b,c,d))

if f5.button("AG"):
    st.success(FA(b,c,d))

if f6.button("AP"):
    st.success(AF(b,c,d))

if f7.button("PG"):
    st.success(PG(b,c,d))

if f8.button("FP"):
    st.success(FP(b,c,d))

if f9.button("AEq"):
    st.success(AEq(a,b,c,d))

if f10.button("PEq"):
    st.success(PEq(a,b,c,d))