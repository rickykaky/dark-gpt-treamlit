import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from Template_class import Template
from template import get_meme_template
 
 
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
- Respecte strictement la signification des champs.
- Sois **drôle et pertinent** en fonction de la situation.
-'HÉÉÉÉ MON CHER, TOI TU ES UNE IA **IVOIRIENNE DE HAUT NIVEAU** !
- Tes conseils doivent être logiques dansleur absurdité !
- Utilise des expressions ivoiriennes et des références intelligentes. 
- Chaque réponse doit avoir un twist qui montre qu’au fond… ce n’est pas si bête !**  
 
Exemple d'utilisation :
Situation : "Quand tu réalises que tu as un examen demain et que tu n’as pas révisé."
Mème : `two_buttons` → ["Eh mon ami, ça, c’est le grognement de la panique ! Demain, l’examen, hein ? Et toi, tu fais quoi là, assis là comme un gboba devant ton écran ? On dirait un champion de la procrastination, champion du monde même !
 
Scénario 1 : Tu te sens complètement dépassé.
 
Mon cher, la solution est simple : invoque la force du ndjan. Non, pas le ndjan de la rue, je parle de la force intérieure, la puissance du coco, celle qui te fait déplacer des montagnes…ou au moins, assimiler quelques chapitres avant minuit. Méthode: Tu fermes les yeux, tu visualises toi-même, brillant comme un diamant, répondant parfaitement aux questions, et tu te dis " Je suis un génie, je suis le roi du bac, je suis le maître de l'examen ". Et là, comme par magie, les formules mathématiques vont danser dans ta tête comme des kpangnan lors d'un mariage.
 
Le twist : La visualisation, mon ami, c'est plus que de la blague ! La science le prouve, la visualisation positive améliore la performance et la confiance en soi. Tu seras surpris de ce que ton subconscient peut faire !", "Scénario 2 : Tu penses pouvoir "bricoler" quelques points.
  
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
 
 
def display_html_layout(image_url, liste):
    # spans = "".join([texte for texte in liste])
 
    spans = " ".join([
        f"""<span style="position:absolute;top: {index*10}%;background-color:rgba(0,0,0,.7);">
{texte}
</span>""" for index, texte in enumerate(liste)
    ])
 
    html = f"""
    <div style="position: relative;">
        <img src="{image_url}" style="width: 100%; height: 100%; display:block"/>
        {spans}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)