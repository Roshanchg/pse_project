document.querySelectorAll("#filters > button").forEach(button => {
    button.addEventListener("click", () => {
        // Remove 'active' class from all buttons
        document.querySelectorAll("#filters > button").forEach(btn => btn.classList.remove("active"));
        
        // Add 'active' class to the clicked button
        button.classList.add("active");

        // Check if none of the buttons is active
        setHotButtonActive();
    });
});

// Function to check if no buttons are active
function setHotButtonActive() {
    const activeButtons = document.querySelectorAll("#filters > button.active");
    
    // If no button is active, add 'active' to hot-button
    if (activeButtons.length === 0) {
        document.getElementById("hot-button").classList.add("active");
    }
}

// Initial check on page load if no button is active, set #hot-button to active
document.addEventListener("DOMContentLoaded", function () {
    setHotButtonActive();
});

document.getElementById("goto-login").addEventListener("click", function() {
    window.location.href = this.getAttribute("data-url");
});
