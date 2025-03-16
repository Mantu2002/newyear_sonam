// Function to show a modal
function showGreeting() {
    document.getElementById("greetingModal").style.display = "flex";
}

function showInspiration() {
    document.getElementById("inspirationModal").style.display = "flex";
}

function showJokes() {
    document.getElementById("jokesModal").style.display = "flex";
}

// Function to close a modal
function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

// Close modal when clicking outside
window.onclick = function(event) {
    let modals = document.querySelectorAll(".modal");
    modals.forEach(modal => {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
};
