
function deceder(decision) {
    // Demander à l'utilisateur s'il souhaite envoyer une remarque
    if(decision === "remarque"){
        var confirmation = confirm("Êtes-vous sûr de vouloir envoyer votre remarque ?");
        // Si l'utilisateur clique sur OK, exécuter la fonction remarque()
        if (confirmation) {
            alert("Votre remarque a été envoyée avec succès !");
        }
    }
    else if(decision==="modification"){
        var confirmation = confirm("Êtes-vous sûr de vouloir modifier ces informations ?");
        // Si l'utilisateur clique sur OK, exécuter la fonction remarque()
        if (confirmation) {
            alert("Vos informations ont été modifiées avec succès !");
            return true
        }
        return false
    }else if(decision==="supprimer"){
        var confirmation = confirm("Êtes-vous sûr de vouloir supprimer ce cours ?");
        // Si l'utilisateur clique sur OK, exécuter la fonction remarque()
        if (confirmation) {
            alert("Votre cours a été supprimé avec succès !");
            return true;
        }
        return false ;
    }else if(decision === "lancerAbsence"){
        var confirmation = confirm("Êtes-vous sûr de vouloir lancé l'absence de ce cours ?");
        // Si l'utilisateur clique sur OK, exécuter la fonction remarque()
        if(confirmation){
            return true
        }
        return false
    }else if(decision === "ajouterCours"){
        var confirmation = confirm("Êtes-vous sûr de vouloir ajouter ce cours ?");
        // Si l'utilisateur clique sur OK, exécuter la fonction remarque()
        if (confirmation) {
            alert("Votre cours a été ajouté avec succès !");
            return true;
        }
        return false ;
    }
}

