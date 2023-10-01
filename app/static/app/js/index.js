const openModalButton = document.querySelector('#openModalButton');
const modal = document.querySelector('#deleteModal');
const closeModalButton = document.querySelector('#closeModalButton')

openModalButton.addEventListener('click', () => {
    modal.show();
})

closeModalButton.addEventListener('click', () => {
    modal.close();
})
