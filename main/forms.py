from django import forms
from django.forms import ModelForm

from main.models import Recherche, Comment


class RechercheForm(ModelForm):
    class Meta:
        model = Recherche
        exclude = ["id", "linked_id_user", "is_valid"]
        widgets = {
            'date_but_proj': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'date_publ_proj': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]
        labels = {"message": "Message"}


# Formulaires de classification
class CQuestion1(forms.Form):
    question_1 = forms.BooleanField(
        label="Question 1 : Participation patient : La recherche nécessite-t-elle la participation du patient hors "
              "des soins "
              "habituels ? (Exemples: prise de sang additionnelle, questionnaire, recueil de données physiologiques)",
        required=False, initial=False)


class CQuestion2(forms.Form):
    question_2_choices = [
        ("A", "Un médicament avec ou sans AMM"),
        ("B", "Un dispositif médical non marqué CE ou utilisé selon des conditions hors notice d’utilisation"),
        ("C", "Un produit de santé autre que médicament (produits biologiques, produits sanguins labiles, etc.)"),
        ("D", "Un produit « hors produit de santé » (complément alimentaire, ...)"),
        ("E", "Cosmétique hors conditions normales d'utilisation"),
        ("F", "Aucune de ces réponses")
    ]

    question_2 = forms.ChoiceField(label="Question 2 : Votre recherche évalue-t-elle ?",
                                   choices=question_2_choices)


class CQuestion3(forms.Form):
    question_3 = forms.BooleanField(
        label="Question 3 : Utilisation selon les recommandations / normes du fabricant",
        required=False, initial=False)


class CQuestion4(forms.Form):
    question_4_choices = [
        ("A", "Un capteur ou une imagerie ou une exploration fonctionnelle par imagerie"),
        ("B", "Une randomisation (tirage au sort) simple"),
        ("C", "Une analyse sanguine"),
        ("D", "Un prélèvement biologique non sanguin"),
        ("E", "Une administration, une utilisation de produit / dispositif médical mis sur le marché de l'UE"),
        ("F", "Une administration de médicaments auxiliaires"),
        ("G", "Un entretien et/ou un questionnaire"),
        ("H", "Des techniques de psychothérapie et / ou de thérapie cognitivo-comportementale"),
        ("I", "Un enregistrement audio / vidéo / photo hors imagerie médicale"),
        ("J", "Des mesures anthropométriques sans intervention invasive"),
        ("K", "Le recueil de données électrophysiologiques sur un matériel implanté ou en cours d'implémentation pour "
              "le soin"),
        ("L", "L'usage de capteurs extra-corporels non invasifs"),
        ("M", "Un acte invasif non réalisé dans la pratique habituelle"),
        ("N", "Un acte non médical (Osthéopathie, hypnose, ...)"),
    ]

    question_4 = forms.ChoiceField(label="Question 4 : Type d’intervention : Votre recherche ajoute-t-elle ?",
                                   choices=question_4_choices)


class CQuestion5(forms.Form):
    question_5 = forms.BooleanField(
        label="Question 5 : Y-a-t-il utilisation d’un produit de contraste ou d’un médicament radiopharmaceutique ?",
        required=False, initial=False)


class CQuestion6(forms.Form):
    question_6 = forms.BooleanField(
        label="Question 6 : Y-a-t-il franchissement de la barrière cutanée ou muqueuse ?",
        required=False, initial=False)


class CQuestion7(forms.Form):
    question_7_choices = [
        ("A", "Au moins un prélèvement additionnel"),
        ("B", "Un tube supplémentaire obtenu lors d’un prélèvement sanguin déjà prévu")
    ]

    question_2 = forms.ChoiceField(label="Question 7 : Précisez le type d’analyse sanguine ajoutée ?",
                                   choices=question_7_choices)


class CQuestion8(forms.Form):
    question_8_choices = [
        ("A", "Au moins un prélèvement additionnel"),
        ("B", "Un tube supplémentaire obtenu lors d’un prélèvement sanguin déjà prévu")
    ]

    question_2 = forms.ChoiceField(label="Question 8 : Le prélèvement est-il parmi la liste suivante ?",
                                   choices=question_8_choices)
