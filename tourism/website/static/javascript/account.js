document.getElementById('delete-account').addEventListener("click", function(event) {
    event.preventDefault(); // Prevent default navigation

    if (confirm("This will permanently DELETE your account, continue?")) {
        window.location.href = this.href; // Proceed with navigation
    }
});