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


class CQuestion9(forms.Form):
    question_9 = forms.BooleanField(
        label="Question 9 :  Touche la face et/ou les plis ?",
        required=False, initial=False)


class CQuestion10(forms.Form):
    question_10 = forms.BooleanField(
        label="Question 10 :  Est-elle obtenue dans le cadre du soin ou d’une intervention déjà prévue?",
        required=False, initial=False)


class CQuestion11(forms.Form):
    question_11_choices = [
        ("A", "Oui avec un volume total du soin et de la recherche < 5 ml"),
        ("B", "Oui avec un volume total du soin et de la recherche >= 5 ml"),
        ("C", "Non")]

    question_11 = forms.ChoiceField(
        label="Question 11 : Le prélèvement de liquide amniotique est-il déjà prévu dans le cadre du soin ? ",
        choices=question_11_choices)


class CQuestion12(forms.Form):
    question_12_choices = [
        ("A", "Oui avec un volume total du soin et de la recherche < 5 ml"),
        ("B", "Oui avec un volume total du soin et de la recherche >= 5 ml"),
        ("C", "Non")]

    question_12 = forms.ChoiceField(
        label="Question 12 : Le prélèvement de liquide céphalorachidien est-il déjà prévu dans le cadre du soin ?",
        choices=question_12_choices)


class CQuestion13(forms.Form):
    question_13_choices = [
        (
            "A",
            "Salive, glaire, urine, selle, sperme, méconium, lait maternel, colostrum, poils, cheveux, ongles, sueur"),
        ("B",
         "Ecouvillonnage superficiel de la peau, du nez, du conduit auditif, de la cavité buccale (incluant "
         "l'oropharynx), de l'orifice anal, des stomies"),
        ("C",
         "Volume supplémentaire minime de tout épanchement (Exemples : Liquide d'ascite, Epanchement pleural, etc.)"),
        ("D", " Il ne s’agit d’aucun de ces prélèvements non invasifs")]

    question_13 = forms.ChoiceField(
        label="Question 13 : Prélèvement non invasif: Le prélèvement est-il dans la liste suivante ? (plusieurs choix "
              "possibles)",
        choices=question_13_choices)


class CQuestion14(forms.Form):
    question_14_choices = [
        ("A", "Conforme à leur destination et conditions d’utilisation"),
        ("B", "Non conforme à leur destination et/ou conditions d’utilisation")]

    question_14 = forms.ChoiceField(label="Question 14 :  L’utilisation est-elle ? ", choices=question_14_choices)


class CQuestion15(forms.Form):
    question_15_choices = [
        ("A", "Administration conforme à leur autorisation de mise sur le marché"),
        ("B",
         "L'entretien et/ou le questionnaire sont susceptibles de modifier la prise en charge et / ou les contraintes "
         "et inconvénients apportés à la personne qui se prête à la recherche sont considérés comme non négligeables"),
        ("C", " Administration sans preuve de santé et/ou d'efficacité suffisante")]

    question_15 = forms.ChoiceField(
        label="Question 15 :  Précisez l’ajout de médicament auxiliaire : il s’agit ici d’un médicament qui est "
              "utilisé pour les besoins de l’essai clinique mais non comme médicament expérimental. Il n’est donc pas "
              "l’objet de la recherche. ",
        choices=question_15_choices)


class CQuestion16(forms.Form):
    question_16_choices = [
        ("A",
         "L'entretien et/ou le questionnaire ne modifient pas la prise en charge et les contraintes et inconvénients "
         "apportés à la personne qui se prête à la recherche sont négligeables"),
        ("B",
         "L'entretien et/ou le questionnaire sont susceptibles de modifier la prise en charge et / ou les contraintes "
         "et inconvénients apportés à la personne qui se prête à la recherche sont considérés comme non négligeables")]

    question_16 = forms.ChoiceField(label="Question 16 :   Précisez l'usage de l'entretien ou du questionnaire",
                                    choices=question_16_choices)


class CQuestion17(forms.Form):
    question_17_choices = [
        ("A", "Recueil de données du dossier médical (en rétrospectif ou en prospectif) "),
        ("B", "Requalification d'échantillons biologiques collectés pour le soin (hors cellules et tissus germinaux) "),
        ("C", "Déchets opératoires "),
        ("D", "Changement de finalité de prélèvements déjà réalisés pour une recherche "),
        ("E", "Randomisation de 2 pratiques de soins habituelles"),
        ("F", "Analyse de données PMSI et/ou RPU"),
        ("G", "Autres bases de données de santé médico-administratives")]

    question_17 = forms.ChoiceField(
        label="Question 17 :  Précisez le type (plusieurs choix possibles). Il s'agit de : RPU: Résumé de passage aux "
              "urgences",
        choices=question_17_choices)


class CQuestion18(forms.Form):
    question_18_choices = [
        ("A", "Anonymisées "),
        ("B", "Pseudonymisées"),
        ("C", "Identifiantes")]

    question_18 = forms.ChoiceField(label="Question 18 :  Comment les données seront-elles collectées ?",
                                    choices=question_18_choices)


class CQuestion19(forms.Form):
    question_19 = forms.BooleanField(
        label="Question 19 :  S’agit-il d’une recherche « interne » ? Usage exclusif de l’équipe de soins",
        required=False, initial=False)


class CQuestion20(forms.Form):
    question_20 = forms.BooleanField(
        label="Question 20 :  Y-a-t-il une possibilité d’informer tous les participants et d’obtenir "
              "l’accord/opposition écrit des participants ?",
        required=False, initial=False)


class CQuestion21(forms.Form):
    question_21 = forms.BooleanField(
        label="Question 21 :  Types de données recueillies: souhaitez-vous recueillir des données autres que celles "
              "présentées ci - dessous?",
        required=False, initial=False)
