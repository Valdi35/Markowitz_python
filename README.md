# Le modele de Markowitz (Implementation sous python)

Le modèle de Markowitz, du même nom que son auteur a été introduit à la suite de ses 
travaux dans l’essai Portfolio Selection (1952). Ce modèle donne place à une nouvelle théorie 
dans le monde financier : c’est la théorie moderne du portefeuille. La théorie moderne du 
portefeuille détient pour idée principale la construction d’un portefeuille d’actifs en ayant pour 
critère premier la maximisation du rendement globale du portefeuille pour un risque minimum
encouru par l’investisseur (Mangram, 2013). Markowitz dans son essai nous relate qu’il existe 
deux étapes dans le processus de sélection d’actifs d’un portefeuille (Markowitz, 1952). En 
effet, la première étape consiste en l’observation du comportement actuel des actifs et se 
termine par la mise en place des croyances futures concernant leurs rendements. Tandis que, la 
deuxième étape consiste en la révélation des croyances et la sélection des actifs qui composeront 
le portefeuille. Markowitz quant à lui, s’appuie sur la deuxième étape dans ses travaux. Afin de 
mieux expliquer comment s’engagent les investisseurs dans leur choix d’actifs, Markowitz 
(1952) établit des hypothèses sur les comportements de ses derniers :
H1 : Les investisseurs sont considérés dans le modèle comme étant averse au risque, ce 
qui veut dire que leur choix d’actifs prend en compte l’impact du risque individuel de chaque 
actif dans le rendement espéré du portefeuille ;
H2 : Les investisseurs sont rationnels et font des choix en fonction de leur rationalité, 
ce qui suppose qu’ils ont une certaine connaissance du fonctionnement des marchés, ils ne sont 
d’ailleurs prêts à accepter des risques d’actifs plus élevés à condition d’obtenir un rendement 
plus élevé ; 
H3 : Les investisseurs ont accès à des capitaux à des taux sans risques et peuvent prêter 
ou emprunter des montants illimités.
Les hypothèses imposées dans le modèle par Markowitz ne se limitent pas qu’à 
l’explication du comportement des investisseurs. En effet, on retrouve dans le modèle de 
Markowitz certaines hypothèses sur le marché ainsi que sur le comportement des actifs 
financiers : 
11
H4 : Les marchés sont parfaitement efficaces, ils n’incluent pas de frais supplémentaires 
sur les transactions ni de taxes ;
H5 : Ils existent des actifs financiers possible d’être sélectionné dont la performance ne 
dépend pas d’autres actifs présents dans le portefeuille, soit une non-corrélation totale des actifs, 
tout rendement d’actifs est donc une variable aléatoire et suit une loi normale défini par son 
espérance mathématique ainsi que son écart-type.
Bien que critiquer du fait de présenter des imperfections, ces hypothèses constituent le 
socle de la théorie moderne du portefeuille et nous permettent d’élaborer un cadre simple afin 
de constituer une meilleure analyse. Les limites de cette théorie seront cependant exposées plus 
loin dans ce travail.
Markowitz (1952) recherche à travers ses travaux un portefeuille dit « efficace », qui répondrait 
aux attentes de l’investisseur. Un portefeuille est cependant dit efficace au sens de Markowitz 
lorsqu’il détient un maximum de rendement pour un niveau de risque minimum. Afin de 
parvenir à ce portefeuille dit « efficace », Markowitz adopte donc un concept clé : la 
diversification.
