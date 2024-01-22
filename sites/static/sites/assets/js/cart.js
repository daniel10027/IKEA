var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        if(user == "AnonymousUser" ){
            
        }else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId,action){
    
    fetch(
        url, {
            
        method: 'POST',
        headers : {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken
        }, 
        body: JSON.stringify({'productId': productId,'action': action})
    })
    .then(response => response.json())
    .then(data => {
        // Afficher un message pop-up
        if (data === 'added') {
            showMessage('Produit ajouté avec succès!');
        } else if (data === 'remove') {
            showMessage('Produit retiré avec succès!');
        } else if (data === 'deleted') {
            showMessage('Produit supprimé avec succès!');
        }

        // Ajouter un délai de 5 secondes avant de recharger la page
        setTimeout(function() {
            location.reload();
        }, 2000);
    });
}

function showMessage(message) {
    // Code pour afficher un message pop-up, par exemple avec une bibliothèque comme SweetAlert
    // Vous devez inclure SweetAlert dans votre projet pour utiliser cette fonctionnalité
    // https://sweetalert2.github.io/
    Swal.fire({
        title: 'Succès!',
        text: message,
        icon: 'success',
    
    });
}