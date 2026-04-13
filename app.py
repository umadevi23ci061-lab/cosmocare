import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# ---------------- CONFIG ----------------
st.set_page_config(page_title="CosmoCare", layout="wide")

# ---------------- MODEL ----------------
@st.cache_resource
def load_model_cached():
    return load_model("skin_model.h5")

model = load_model_cached()
classes = ["dry", "normal", "oily"]

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "skin" not in st.session_state:
    st.session_state.skin = None

# ---------------- PREDICTION ----------------
def predict_skin(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img) / 0.255
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img, verbose=0)
    return classes[np.argmax(pred)]

# ---------------- PREMIUM STYLE (REPLACE OLD STYLE) ----------------
st.markdown("""
<style>

/* 🌟 Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Poppins:wght@300;500;700&display=swap');

/* 🌈 Animated Gradient Background */
.stApp {
    background: linear-gradient(-45deg, #87CEEB, #FF69B4, #ffffff, #ffb6c1);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
    font-family: 'Poppins', sans-serif;
}

/* Background animation */
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* 💎 Title (luxury font + animation) */
.title {
    font-family: 'Playfair Display', serif;
    font-size: 80px;
    text-align: center;
    color: #1a1a1a;
    animation: slideDown 1.2s ease;
}

/* Title animation */
@keyframes slideDown {
    from {
        transform: translateY(-100px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 22px;
    margin-top: 10px;
}

/* 💎 Glass Card */
.card {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(12px);
    border-radius: 25px;
    padding: 25px;
    margin: 15px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}

/* 💄 Premium Button */
.stButton>button {
    background: linear-gradient(45deg, #ff4da6, #ff99cc);
    color: white;
    border-radius: 50px;
    height: 60px;
    width: 280px;
    font-size: 18px;
    font-weight: bold;
    border: none;
    box-shadow: 0 5px 20px rgba(255, 77, 166, 0.4);
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.08);
    box-shadow: 0 10px 30px rgba(255, 77, 166, 0.6);
}

/* 💄 FLOATING SCATTERED ICONS */
.icon {
    position: fixed;
    font-size: 26px;
    opacity: 0.6;
    z-index: 999;
    animation: float 6s infinite ease-in-out;
}

/* Different scattered positions */
.icon1 { top: 10%; left: 5%; animation-delay: 0s; }
.icon2 { top: 20%; right: 8%; animation-delay: 1s; }
.icon3 { bottom: 15%; left: 10%; animation-delay: 2s; }
.icon4 { bottom: 10%; right: 5%; animation-delay: 3s; }
.icon5 { top: 50%; left: 45%; animation-delay: 4s; }
.icon6 { top: 70%; right: 20%; animation-delay: 2.5s; }

/* Floating animation */
@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(40px);}
    100% {transform: translateY(0px);}
}

/* Hide Streamlit UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)
# ---------------- HOME ----------------
# ---------------- HOME ----------------
# ---------------- HOME ----------------
# ---------------- HOME ----------------
if st.session_state.page == "home":

    # 💄 Floating scattered icons
    st.markdown("""
    <div class="icon icon1">💄</div>
    <div class="icon icon2">💋</div>
    <div class="icon icon3">🪞</div>
    <div class="icon icon4">✨</div>
    <div class="icon icon5">💅</div>
    <div class="icon icon6">🧴</div>
    """, unsafe_allow_html=True)

    # 🌟 Title
    st.markdown("<div class='title'>CosmoCare 💄</div>", unsafe_allow_html=True)

    # ✨ Subtitle
    st.markdown("<div class='subtitle'>Glow Smarter with AI ✨</div>", unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

    # 🎯 PERFECT CENTER BUTTON
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        if st.button("💄 Let's Start"):
            st.session_state.page = "welcome"
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- WELCOME ----------------
elif st.session_state.page == "welcome":
    st.markdown("<div class='fancy title'>Welcome to CosmoCare 🌸</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    💖 <b>CosmoCare is your intelligent beauty companion</b><br><br>

    ✨ "Almost everything will work again if you unplug it for a few minutes, including you."<br><br>

    • Personalized skincare routines<br>
    • Product recommendations<br>
    • Makeup guidance<br>
    • Diet plans<br>
    • Problem detection<br>
    • Feedback system<br><br>

    🌿 <b>Why CosmoCare?</b><br>
    Because your skin deserves smart care, not guesswork.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Explore Features ➡"):
        st.session_state.page = "features"

# ---------------- FEATURES ----------------
elif st.session_state.page == "features":
    st.markdown("<div class='fancy title'>Features</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    🧬 Skin Analyzer<br>
    🧴 Products<br>
    🌞 Routine<br>
    💄 Makeup<br>
    🥗 Diet<br>
    ⚠ Problems<br>
    📝 Feedback<br>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Start Skin Analysis ➡"):
        st.session_state.page = "analyzer"

# ---------------- ANALYZER ----------------
elif st.session_state.page == "analyzer":

    st.markdown("<div class='fancy title'>Skin Analyzer</div>", unsafe_allow_html=True)

    file = st.file_uploader("Upload Image", type=["jpg", "png"])

    if file:
        with open("temp.jpg", "wb") as f:
            f.write(file.read())

        st.image("temp.jpg", width=250)

        if st.button("Analyze"):
            st.session_state.skin = predict_skin("temp.jpg")

    if st.session_state.skin:
        skin = st.session_state.skin
        st.success(f"Detected Skin: {skin}")

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        if skin == "oily":
            st.markdown("""### Oily Skin
Excess sebum causes shine & acne.

**Causes:**
- Hormones
- Genetics
- Excess sebum production
- Enlarged pores
- Hot weather
- Overwashing

**Solution:**
Requires oil control and proper cleansing
""")

        elif skin == "dry":
            st.markdown("""### Dry Skin
Lacks moisture leading to flakiness.

**Causes:**
- Lack of natural oil
- cold or dry weather
- Dehydration
- Harsh soaps
- Poor diet

**Solution:**
Use hydrating moisturizer & gentle cleanser.
""")

        else:
            st.markdown("### Normal Skin\nBalanced and healthy skin type.")

        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("Next ➡ Products"):
            st.session_state.page = "products"

# ---------------- PRODUCTS ----------------
elif st.session_state.page == "products":

    st.markdown("<div class='fancy title'>Product Suggestions</div>", unsafe_allow_html=True)

    skin = st.session_state.skin or "normal"

    products = {
        "oily": [
            {"name": "Pond's Pure Detox", "price": "₹150", "desc": "Removes excess oil & dirt, keeps skin fresh"},
            {"name": "Neutrogena Oil-Free Wash", "price": "₹350", "desc": "Deep cleans pores and reduces acne"},
            {"name": "Cetaphil Gentle Cleanser", "price": "₹800", "desc": "Very mild cleanser for sensitive oily skin"},
            {"name": "Mamaearth Neem Face Wash", "price": "₹249", "desc": "Helps fight acne-causing bacteria"},
        ],
        "dry": [
            {"name": "Himalaya Moisturizing Cream", "price": "₹120", "desc": "Basic hydration for dry skin"},
            {"name": "Nivea Soft Cream", "price": "₹350", "desc": "Locks moisture for long hours"},
            {"name": "Clinique Moisture Surge", "price": "₹3000", "desc": "Premium deep hydration therapy"},
            {"name": "Vaseline Intensive Care", "price": "₹220", "desc": "Heals extremely dry and rough skin"},
        ],
        "normal": [
            {"name": "Simple Face Wash", "price": "₹250", "desc": "Gentle cleanser for daily use"},
            {"name": "Garnier Light Moisturizer", "price": "₹180", "desc": "Keeps skin soft and balanced"},
            {"name": "Biotique Morning Nectar", "price": "₹199", "desc": "Natural glow enhancing formula"},
            {"name": "Plum Green Tea Moisturizer", "price": "₹450", "desc": "Controls oil while moisturizing"},
        ]
    }

    for product in products[skin]:
        st.markdown(f"""
**🧴 {product['name']}**
💰 Price: {product['price']}
📝 {product['desc']}
---
""")

    if st.button("Next ➡ Routine"):
        st.session_state.page = "routine"

# ---------------- ROUTINE ----------------
elif st.session_state.page == "routine":

    st.markdown("<div class='fancy title'>Skin Routine</div>", unsafe_allow_html=True)

    skin = st.session_state.skin or "normal"

    if skin == "oily":
        st.write("""Morning:
1. Cleanser (oil-control face wash)
>Use gel or foaming cleanser
>Avoid harsh soaps
>wash 30–40 seconds
Recommended: Simple

2. Toner
>Witch hazel, Green tea, Niacinamide
Recommended: Dermdoc toner
Cost: Rs 199
""")

        st.write("""Night:
1. Cleanser
2. Toner
3. Treatment (Salicylic Acid)
4. Moisturizer (gel-based)
""")

    elif skin == "dry":
        st.write("""Morning:
1. Hydrating cleanser
2. Toner (Hyaluronic Acid)
3. Serum
4. Moisturizer
5. Sunscreen
""")

        st.write("""Night:
1. Cleanser
2. Toner
3. Serum
4. Night cream
5. Face oil (optional)
""")

    else:
        st.write("Basic skincare routine")

    if st.button("Next ➡ Makeup"):
        st.session_state.page = "makeup"

# ---------------- MAKEUP ----------------
elif st.session_state.page == "makeup":

    st.markdown("<div class='fancy title'>Makeup Guidance</div>", unsafe_allow_html=True)

    level = st.selectbox("Level", ["Beginner", "Moderate", "Pro"])

    if level == "Beginner":
        st.write("""1. Skin Prep
2. Primer
3. Foundation
4. Concealer
5. Compact
6. Eyebrows
7. Blush
8. Eyeliner
9. Mascara
10. Lipstick
11. Setting Spray
""")

    elif level == "Moderate":
        st.write("""1. Skin Prep
2. Primer
3. Corrector
4. Foundation
5. Concealer
6. Powder
7. Contour
8. Blush
9. Highlighter
10. Eyes
11. Lips
12. Setting Spray
""")

    else:
        st.write("""Advanced makeup routine:
Full professional steps with contouring, baking, blending, and layering.""")

    if st.button("Next ➡ Diet"):
        st.session_state.page = "diet"

# ---------------- DIET ----------------
elif st.session_state.page == "diet":

    st.markdown("<div class='fancy title'>Diet Plan</div>", unsafe_allow_html=True)

    st.markdown("""
### 🌿 Skin Glow Diet Plan

A proper diet helps improve skin texture, glow, and reduces acne.

---

## ☀ Morning (Empty Stomach)
- Warm water with lemon 🍋
- Soaked almonds (5–6)
- Optional: Green tea

👉 Helps detoxify body and improve skin glow

---

## 🍳 Breakfast
- Oats / Dalia / Poha
- Fruits: Apple, banana, papaya
- Protein: Eggs or sprouts

👉 Gives nutrients for healthy skin repair

---

## 🍱 Lunch
- Rice or roti
- Dal (lentils)
- Vegetables (green leafy preferred)
- Curd (probiotic for gut health)

👉 Improves digestion → clearer skin

---

## 🍵 Evening Snacks
- Green tea / herbal tea
- Nuts (almonds, walnuts)
- Fruits or roasted chana

👉 Prevents skin dullness and acne triggers

---

## 🌙 Dinner (Light Meal)
- Soup / khichdi / light roti sabzi
- Avoid oily & spicy food at night

👉 Helps skin repair during sleep

---

## 🚫 Foods to Avoid
- Junk food (burgers, fries)
- Sugary drinks (cola, soda)
- Excess dairy (if acne-prone)
- Deep fried items

---

## 💧 Extra Tips
- Drink 2–3 liters of water daily
- Sleep 7–8 hours
- Reduce stress (very important for skin)
""")

    if st.button("Next ➡ Problem Solver"):
        st.session_state.page = "problem"
# ---------------- PROBLEM ----------------
elif st.session_state.page == "problem":

    st.markdown("<div class='fancy title'>Problem Solver</div>", unsafe_allow_html=True)

    issue = st.selectbox("Select Your Skin Issue", ["Acne", "Dryness", "Oiliness", "Dark Spots", "Dull Skin"])

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    if issue == "Acne":

        st.write("""
### Acne (Pimples)

**Causes:**
- Excess oil production
- Bacteria buildup
- Hormonal changes
- Poor cleansing routine
- Stress & diet

**Solution:**
- Use salicylic acid face wash (1–2 times daily)
- Apply niacinamide serum
- Avoid touching face frequently
- Keep pillow covers clean

**Home Remedies:**
- Aloe vera gel (calming)
- Ice compress (reduces swelling)
- Tea tree oil (spot treatment only)

**Recommended Routine:**
Morning: Cleanser → Toner → Light Moisturizer → Sunscreen  
Night: Cleanser → Treatment serum → Moisturizer
""")

    elif issue == "Dryness":

        st.write("""
### Dry Skin Issues

**Causes:**
- Lack of moisture
- Cold weather
- Overwashing face
- Harsh soaps

**Solution:**
- Use hydrating cleanser
- Apply hyaluronic acid serum
- Use thick moisturizer
- Avoid hot water wash

**Home Remedies:**
- Honey mask (hydration)
- Milk cream (natural moisture)
- Aloe vera gel

**Recommended Routine:**
Morning: Hydrating cleanser → Toner → Moisturizer → Sunscreen  
Night: Cleanser → Serum → Heavy moisturizer → Face oil (optional)
""")

    elif issue == "Oiliness":

        st.write("""
### Oily Skin Issues

**Causes:**
- Overactive sebaceous glands
- Humidity
- Hormones
- Overwashing face

**Solution:**
- Use gel-based cleanser
- Use salicylic acid toner
- Oil-free moisturizer only
- Blot excess oil during day

**Home Remedies:**
- Multani mitti face pack (1–2 times/week)
- Cucumber mask (cooling effect)
- Lemon + honey (use carefully)

**Recommended Routine:**
Morning: Cleanser → Toner → Gel moisturizer → Sunscreen  
Night: Cleanser → Treatment serum → Light moisturizer
""")

    elif issue == "Dark Spots":

        st.write("""
### Dark Spots / Pigmentation

**Causes:**
- Acne marks
- Sun exposure
- Hormonal changes

**Solution:**
- Use vitamin C serum
- Apply sunscreen daily (very important)
- Use niacinamide or alpha arbutin

**Home Remedies:**
- Aloe vera gel
- Turmeric + honey mask

**Recommended Routine:**
Morning: Cleanser → Vitamin C → Moisturizer → Sunscreen  
Night: Cleanser → Niacinamide serum → Moisturizer
""")

    else:  # Dull Skin

        st.write("""
### Dull Skin

**Causes:**
- Lack of hydration
- Poor sleep
- Dead skin buildup
- Pollution

**Solution:**
- Exfoliate 1–2 times a week
- Use vitamin C serum
- Stay hydrated

**Home Remedies:**
- Coffee scrub (gentle exfoliation)
- Besan + milk mask
- Aloe vera gel

**Recommended Routine:**
Morning: Cleanser → Vitamin C → Moisturizer → Sunscreen  
Night: Cleanser → Exfoliation (2–3x/week) → Serum → Moisturizer
""")

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Next ➡ Feedback"):
        st.session_state.page = "feedback"

# ---------------- FEEDBACK ----------------
elif st.session_state.page == "feedback":

    st.markdown("<div class='fancy title'>Feedback</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    result = st.selectbox("Did your skin improve?", ["Improved", "Same", "Worse"])
    rating = st.slider("Rate CosmoCare Experience", 1, 5, 3)
    review = st.text_area("Write your review")

    st.write("")

    if st.button("Submit Feedback"):

        if result == "Improved":
            st.success("✨ Great! We're happy your skin is improving with CosmoCare.")

        elif result == "Same":
            st.info("💡 We'll adjust recommendations to give better results.")

        else:
            st.warning("⚠ We’re sorry. We will improve your skincare suggestions.")

        st.success(f"⭐ Thank you for rating us {rating}/5")

        if review:
            st.write("📝 Your Review:")
            st.write(review)

    st.markdown("""
    ---
    💖 Thank you for using CosmoCare  
    Your skin journey matters. We’ll keep improving our AI for better results ✨
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)