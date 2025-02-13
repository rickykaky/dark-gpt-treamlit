def get_meme_template():
    # tableau de memes
    MemeTemplate=[
    {
        "ID": "two_buttons",
        "Description": "Le mème 'Two Buttons' montre une personne face à deux boutons.",
        "Champs": {
            "0": "Le texte du bouton 1",
            "1": "Le texte du bouton 2"
        },
        "Link": "https://imgflip.com/s/meme/Two-Buttons.jpg"
    },
    {
        "ID": "drake_bling",
        "Description": "Le mème 'Drake Bling' montre Drake qui accepte ou refuse un choix.",
        "Champs": {
            "0": "Le texte du choix refusé",
            "1": "Le texte du choix accepté"
        },
        "Link": "https://imgflip.com/s/meme/Drake-Hotline-Bling.jpg"
    },
    {
        "ID": "batman_slapping_robin",
        "Description": "Le mème 'Batman Slapping Robin' montre Batman qui gifle Robin.",
        "Champs": {
            "0": "Ce que Batman reproche à Robin"
        },
        "Link": "https://imgflip.com/s/meme/Batman-Slapping-Robin.jpg"
    },
    {
        "ID": "woman_yelling_at_cat",
        "Description": "Le mème 'Woman Yelling At Cat' montre une femme criant sur un chat assis devant une assiette.",
        "Champs": {
            "0": "Texte crié par la femme",
            "1": "Réponse du chat"
        },
        "Link": "https://imgflip.com/s/meme/Woman-Yelling-At-Cat.jpg"
    },
    {
        "ID": "distracted_boyfriend",
        "Description": "Le mème 'Distracted Boyfriend' montre un homme se retournant pour regarder une autre femme, au grand désarroi de sa copine.",
        "Champs": {
            "0": "Texte pour le petit ami",
            "1": "Texte pour la copine",
            "2": "Texte pour la fille attirante"
        },
        "Link": "https://imgflip.com/s/meme/Distracted-Boyfriend.jpg"
    },
    {
        "ID": "gru_plan",
        "Description": "Le mème 'Gru's Plan' montre Gru en train de présenter un plan en quatre étapes sur un tableau.",
        "Champs": {
            "0": "Texte étape 1",
            "1": "Texte étape 2",
            "2": "Texte étape 3",
            "3": "Texte étape 4 (surprise)"
        },
        "Link": "https://imgflip.com/s/meme/Grus-Plan.jpg"
    },
    {
        "ID": "trump_bill_signing",
        "Description": "Le mème 'Trump Bill Signing' montre Donald Trump signant un document officiel.",
        "Champs": {
            "0": "Texte affiché sur le document"
        },
        "Link": "https://imgflip.com/s/meme/Trump-Bill-Signing.jpg"
    },
    {
        "ID": "waiting_skeleton",
        "Description": "Le mème 'Waiting Skeleton' montre un squelette assis, attendant quelque chose depuis très longtemps.",
        "Champs": {
            "0": "Texte décrivant ce qui est attendu"
        },
        "Link": "https://imgflip.com/s/meme/Waiting-Skeleton.jpg"
    },
    {
        "ID": "clown_applying_makeup",
        "Description": "Le mème 'Clown Applying Makeup' montre une personne se maquillant progressivement en clown, illustrant une évolution d'une idée naïve vers une idée absurde.",
        "Champs": {
            "0": "Première étape",
            "1": "Deuxième étape",
            "2": "Troisième étape",
            "3": "Dernière étape (idée totalement absurde)"
        },
        "Link": "https://imgflip.com/s/meme/Clown-Applying-Makeup.jpg"
    },
    {
        "ID": "bernie_sanders_once_again",
        "Description": "Le mème 'Bernie Sanders Once Again Asking' montre Bernie Sanders en train de demander quelque chose avec insistance.",
        "Champs": {
            "0": "Texte indiquant ce qui est demandé"
        },
        "Link": "https://imgflip.com/s/meme/Bernie-I-Am-Once-Again-Asking-For-Your-Support.jpg"
    },
    {
        "ID": "hide_the_pain_harold",
        "Description": "Le mème 'Hide the Pain Harold' montre un homme avec un sourire forcé, cachant son mal-être.",
        "Champs": {
            "0": "Texte décrivant la situation gênante"
        },
        "Link": "https://imgflip.com/s/meme/Hide-the-Pain-Harold.jpg"
    },
    {
        "ID": "monkey_puppet",
        "Description": "Le mème 'Monkey Puppet' montre une marionnette de singe détournant le regard de manière gênée.",
        "Champs": {
            "0": "Texte décrivant la situation embarrassante"
        },
        "Link": "https://imgflip.com/s/meme/Monkey-Puppet.jpg"
    },
    {
        "ID": "x_x_everywhere",
        "Description": "Le mème 'X, X Everywhere' vient de Toy Story et montre Buzz l'Éclair disant 'X, X partout'.",
        "Champs": {
            "0": "Texte pour 'X' (exemple : Bugs, Bugs partout)"
        },
        "Link": "https://imgflip.com/s/meme/X-X-Everywhere.jpg"
    },
    {
        "ID": "tuxedo_winnie_the_pooh",
        "Description": "Le mème 'Tuxedo Winnie The Pooh' montre Winnie l'Ourson en tenue normale et en smoking, représentant une amélioration d'une idée.",
        "Champs": {
            "0": "Texte pour Winnie normal",
            "1": "Texte pour Winnie en smoking"
        },
        "Link": "https://imgflip.com/s/meme/Tuxedo-Winnie-The-Pooh.jpg"
    },
    {
        "ID": "yall_got_any_more_of_that",
        "Description": "Le mème 'Y'all Got Any More Of That' montre un homme en manque de quelque chose.",
        "Champs": {
            "0": "Texte décrivant ce qui manque"
        },
        "Link": "https://imgflip.com/s/meme/Yall-Got-Any-More-Of-That.jpg"
    },
    {
        "ID": "i_bet_hes_thinking_about_other_women",
        "Description": "Le mème 'I Bet He's Thinking About Other Women' montre une femme imaginant les pensées de son copain, alors qu'il pense à quelque chose d'insignifiant.",
        "Champs": {
            "0": "Texte pour ce que pense la femme",
            "1": "Texte pour ce que pense l'homme"
        },
        "Link": "https://imgflip.com/s/meme/I-Bet-Hes-Thinking-About-Other-Women.jpg"
    },
    {
        "ID": "disaster_girl",
        "Description": "Le mème 'Disaster Girl' montre une fille souriant devant une maison en feu.",
        "Champs": {
            "0": "Texte décrivant la situation"
        },
        "Link": "https://imgflip.com/s/meme/Disaster-Girl.jpg"
    },
    {
        "ID": "left_exit_12_off_ramp",
        "Description": "Le mème 'Left Exit 12 Off Ramp' montre une voiture prenant une sortie brusquement.",
        "Champs": {
            "0": "Texte pour la route principale",
            "1": "Texte pour la sortie"
        },
        "Link": "https://imgflip.com/s/meme/Left-Exit-12-Off-Ramp.jpg"
    },
    {
        "ID": "expanding_brain",
        "Description": "Le mème 'Expanding Brain' montre un cerveau qui devient de plus en plus lumineux pour représenter une prise de conscience ou une progression d'idées.",
        "Champs": {
            "0": "Première idée",
            "1": "Deuxième idée",
            "2": "Troisième idée",
            "3": "Quatrième idée (idée suprême)"
        },
        "Link": "https://imgflip.com/s/meme/Expanding-Brain.jpg"
    }
    ]
    return MemeTemplate
