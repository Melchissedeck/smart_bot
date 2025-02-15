import streamlit as st
from mistralai import Mistral

# Configuration de l'API

api_key = st.secrets["Mistral"]["mistral_key"]
model = "mistral-large-latest"

# Initialisation du client Mistral
client = Mistral(api_key= api_key)

# Fonction pour générer une réponse à partir de l'API Mistral
def generate_response(user_input):
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": user_input,
            },
        ]
    )
    return chat_response.choices[0].message.content

# Créer l'interface de l'application avec Streamlit
st.title("Chatbot avec Streamlit")
st.write("Bienvenue sur l'interface de chatbot. Posez-moi des questions !")

# Stocker l'historique des conversations
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Créer un formulaire pour saisir la question
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Vous :", key="input")
    submit_button = st.form_submit_button(label='Envoyer')

# Afficher la réponse du bot
if submit_button and user_input:
    response = generate_response(user_input)
    # Ajouter l'entrée utilisateur et la réponse à l'historique
    st.session_state.chat_history.append(("Vous", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Affichage de l'historique des échanges
for sender, message in st.session_state.chat_history:
    if sender == "Vous":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"*{sender}:* {message}")

# Intégrer une mémoire au bot 
# Protéger la clé API 
# Donner un style au Bot pour qu'il parle uniquement en alexandrin