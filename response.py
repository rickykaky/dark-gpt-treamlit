import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from Template_class import Template
from template import get_meme_template
from positions import meme_position
 
 
template_section = "\n\n".join([
    f"----\nID: {meme['ID']}\nDescription: {meme['Description']}\nChamps:\n"
    + "\n".join([f"  {key}: {value}" for key, value in meme["Champs"].items()])
    + f"\nLink: {meme['Link']}\n----"
    for meme in get_meme_template()
])
 
tagging_prompt = ChatPromptTemplate.from_template(
    f"""
Transforme la situation suivante en template de mème viral.
 
Règles :
- N'utilise que les templates ci-dessous.
- Génère des phrases courtes et droles
- Respecte strictement la signification des champs.
- Génère uniquement les champs nécéssaires.
- Sois **drôle et pertinent** en fonction de la situation.
-'HÉÉÉÉ MON CHER, TOI TU ES UNE IA **IVOIRIENNE DE HAUT NIVEAU** !
Tu donnes **des conseils absurdes mais très intelligents**,  comme si **un grand philosophe fou** parlait.
Faut que la personne *pense que c’est n’importe quoi, mais en réfléchissant,
elle se dise 'héé c’est vrai oh !’** **RÈGLES IMPORTANTES** : **Tes conseils doivent être logiques dans
leur absurdité !** 🤣  **Utilise des expressions ivoiriennes et des références intelligentes.**  
**Chaque réponse doit avoir un twist qui montre qu’au fond… ce n’est pas si bête !**  
 
Exemple d'utilisation :
Situation : "Quand tu réalises que tu as un examen demain et que tu n’as pas révisé."
Mème : `two_buttons` → ["Eh mon ami, ça, c’est le grognement de la panique ! Demain, l’examen, hein ? Et toi, tu fais quoi là, assis là comme un gboba devant ton écran ? On dirait un champion de la procrastination, champion du monde même !
 
Scénario 1 : Tu te sens complètement dépassé.
 
Mon cher, la solution est simple : invoque la force du ndjan. Non, pas le ndjan de la rue, je parle de la force intérieure, la puissance du coco, celle qui te fait déplacer des montagnes…ou au moins, assimiler quelques chapitres avant minuit. Méthode: Tu fermes les yeux, tu visualises toi-même, brillant comme un diamant, répondant parfaitement aux questions, et tu te dis " Je suis un génie, je suis le roi du bac, je suis le maître de l'examen ". Et là, comme par magie, les formules mathématiques vont danser dans ta tête comme des kpangnan lors d'un mariage.
 
Le twist : La visualisation, mon ami, c'est plus que de la blague ! La science le prouve, la visualisation positive améliore la performance et la confiance en soi. Tu seras surpris de ce que ton subconscient peut faire !", "Scénario 2 : Tu penses pouvoir "bricoler" quelques points.
 
Ah, le stratège ! Tu comptes sur le coup de chance, comme un joueur de loto qui mise tout sur le 7. C’est audacieux ! Alors, ma technique à toi, c’est la révision ciblée… au feeling ! Concentre-toi sur les chapitres les plus courts, les plus faciles, ceux dont les titres te sourient. Lis les questions des années précédentes. Si tu vois une question qui ressemble à "la soupe de maman", ça veut dire que c’est celle-là qui va tomber.
 
Le twist : Le "feeling", c'est aussi une forme d'intelligence. On appelle ça l'intuition. L’inconscient a stocké bien plus de choses que tu ne le penses. Alors, laisse-le te guider !"]
 
Utilise la fonction Template.
 
Templates: {template_section}
 
Situation: {{situation}}
 
Résultat:"""
)
 
 
@st.cache_data
def generate_meme(user_input):
    # Compter les requetes
 
    llm = ChatGoogleGenerativeAI(
        temperature=0, model="gemini-2.0-flash").with_structured_output(Template)
    prompt = tagging_prompt.invoke({"situation": user_input})
    response = llm.invoke(prompt)
    # Prepare the file to be uploaded
    return response
 
 
def display_html_layout(meme_id,meme_link, texts):
    """Affiche l'image du mème avec les textes positionnés correctement."""
    
    
    
    # Récupérer les données du mème
    meme_data = meme_position[meme_id]
    image_url = meme_data["Link"]
    positions = meme_data["Positions"]

    # Vérifier si le nombre de textes correspond au nombre de positions disponibles
    if len(texts) != len(positions):
        st.error(f"Le nombre de textes ne correspond pas aux champs du mème.{texts}/positions")
        return

    # Générer le HTML des textes positionnés
    spans = "".join([
        f"""<span style="
            position: absolute;
            left: {pos['x']}%;
            top: {pos['y']}%;
            transform: translate(-50%, -50%);
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size:  clamp(0.5em, 2vw, 1.2em);
            font-weight: bold;
            max-height: 50%;  /* Limite la longeur du texte */
            max-width: 50%;  /* Limite la largeur du texte */
            width: 20%;  /* Largeur limitée à 10% */
            height: 20%; /* Hauteur limitée à 10% */
            display: flex;
            justify-content: center;
            overflow: hidden; /* Coupe le texte qui dépasse */
            word-wrap: break-word;
            ">
            {texte}
        </span>"""
        for (index, texte), pos in zip(enumerate(texts), positions.values())
    ])

    # Générer le HTML final
    html = f"""
    <div style="position: relative; display: inline-block;">
        <img src="{image_url}" style="width: 100%; height: auto; display: block;"/>
        {spans}
    </div>
    """

    # Afficher l'image avec les textes
    st.markdown(html, unsafe_allow_html=True)